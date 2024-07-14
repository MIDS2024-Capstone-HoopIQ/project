import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import boto3
from courtCoordinates import CourtCoordinates
from basketballShot import BasketballShot

# Define constants
AWS_REGION = "us-east-1"
SCHEMA_NAME = "wnba_db"
S3_STAGING_DIR = "s3://wnbadata/"

st.set_page_config(layout="wide")

# Connect to the database
connect_str = "awsathena+rest://athena.{region_name}.amazonaws.com:443/{schema_name}?s3_staging_dir={s3_staging_dir}"
engine = create_engine(connect_str.format(
        region_name=AWS_REGION,
        schema_name=SCHEMA_NAME,
        s3_staging_dir=quote_plus(S3_STAGING_DIR)
))

# Define color mapping for shot paths
color_mapping = {
    'home': '#1f77b4',
    'away': '#ff7f0e'
}

# Build the court
# draw court lines
court = CourtCoordinates()
court_lines_df = court.get_court_lines()


# Display a Plotly 3D Line plot on Streamlit
fig = px.line_3d(
   data_frame=court_lines_df, x='x', y='y', z='z', line_group='line_group', color='color',
   color_discrete_map={
       'court': '#000000',
       'hoop': '#e47041'
   }
)
fig.update_traces(hovertemplate=None, hoverinfo='skip', showlegend=False)

# Execute the custom query to get shot chart data
query = """
SELECT pbp.sequence_number,
       pbp.coordinate_x,
       pbp.coordinate_y,
       pbp.team_id,
       pbp.text,
       pbp.scoring_play,
       pbp.score_value,
       CASE WHEN team_id = home_team_id
            THEN 'home' 
            ELSE 'away' 
            END AS scoring_team
FROM wnba_schedule ws, wnba_play_by_play pbp 
WHERE ws.id = '401578572'
  AND pbp.game_id = ws.id
  AND pbp.scoring_play = true
  AND pbp.score_value != 1;
"""
game_shots_df = pd.read_sql(query, engine)

# Each row in the DataFrame is one attempted shot
game_coords_df = pd.DataFrame()

# Generate coordinates for shot paths
for index, row in game_shots_df.iterrows():
    shot = BasketballShot(
        shot_start_x=row['coordinate_x'],
        shot_start_y=row['coordinate_y'],
        shot_id=row['sequence_number'],
        play_description=row['text'],
        shot_made=row['scoring_play'],
        team=row['scoring_team']
    )
    shot_df = shot.get_shot_path_coordinates()
    game_coords_df = pd.concat([game_coords_df, shot_df])

# Pass the coordinates DataFrame to a Plotly 3D Line plot
shot_path_fig = px.line_3d(
   data_frame=game_coords_df,
   x='x',
   y='y',
   z='z',
   line_group='line_id',
   color='team',
   color_discrete_map=color_mapping,
   custom_data=['description']
)
hovertemplate='Description'
fig.update_traces(opacity=0.55, hovertemplate=hovertemplate, showlegend=False)

# shot start scatter plots
game_coords_start = game_coords_df[game_coords_df['shot_coord_index'] == 0]
shot_start_fig = px.scatter_3d(
    data_frame=game_coords_start,
    x='x',
    y='y',
    z='z',
    custom_data=['description'],
    color='team',
    color_discrete_map=color_mapping,
    symbol='shot_made',
    symbol_map={'made': 'circle', 'missed': 'x'}
)

shot_start_fig.update_traces(marker_size=4, hovertemplate=hovertemplate)

# add shot scatter plot to court plot
for i in range(len(shot_start_fig.data)):
    fig.add_trace(shot_start_fig.data[i])

# add shot line plot to court plot
for i in range(len(shot_path_fig.data)):
    fig.add_trace(shot_path_fig.data[i])

# graph styling
fig.update_traces(line=dict(width=5))
fig.update_layout(    
    margin=dict(l=20, r=20, t=20, b=20),
    scene_aspectmode="data",
    height=600,
    scene_camera=dict(
        eye=dict(x=1.3, y=0, z=0.7)
    ),
    scene=dict(
        xaxis=dict(title='', showticklabels=False, showgrid=False),
        yaxis=dict(title='', showticklabels=False, showgrid=False),
        zaxis=dict(title='',  showticklabels=False, showgrid=False, showbackground=True, backgroundcolor='#f7f0e8'),
    ),
    legend=dict(
        yanchor='bottom',
        y=0.05,
        x=0.2,
        xanchor='left',
        orientation='h',
        font=dict(size=15, color='black'),
        bgcolor='white',
        title='',
        itemsizing='constant'
    ),
    legend_traceorder="reversed"
)

st.plotly_chart(fig, use_container_width=True)