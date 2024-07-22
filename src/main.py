import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
import streamlit as st
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import boto3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, Rectangle, Circle

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

# Helper function to draw the court in left/right direction
def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    if ax is None:
        ax = plt.gca()
    # hoop
    hoop_left = Circle((-45, 0), radius=0.75, linewidth=lw, color=color, fill=False)
    hoop_right = Circle((45, 0), radius=0.75, linewidth=lw, color=color, fill=False)
    # backboard
    backboard_left = Rectangle((-46, -3), 0.1, 6, linewidth=lw, color=color)
    backboard_right = Rectangle((45, -3), 0.1, 6, linewidth=lw, color=color)
    # paint
    outer_box_left = Rectangle((-45, -8), 19, 16, linewidth=lw, color=color, fill=False)
    outer_box_right = Rectangle((26, -8), 19, 16, linewidth=lw, color=color, fill=False)
    inner_box_left = Rectangle((-45, -6), 19, 12, linewidth=lw, color=color, fill=False)
    inner_box_right = Rectangle((26, -6), 19, 12, linewidth=lw, color=color, fill=False)
    # free throw top arc
    top_free_throw_left = Arc((-26, 0), 12, 12, theta1=90, theta2=270, linewidth=lw, color=color, fill=False)
    top_free_throw_right = Arc((26, 0), 12, 12, theta1=270, theta2=90, linewidth=lw, color=color, fill=False)
    # free throw bottom arc
    bottom_free_throw_left = Arc((-26, 0), 12, 12, theta1=270, theta2=90, linewidth=lw, color=color, linestyle='dashed')
    bottom_free_throw_right = Arc((26, 0), 12, 12, theta1=90, theta2=270, linewidth=lw, color=color, linestyle='dashed')
    # restricted zone
    restricted_left = Arc((-45, 0), 8, 8, theta1=270, theta2=90, linewidth=lw, color=color)
    restricted_right = Arc((45, 0), 8, 8, theta1=90, theta2=270, linewidth=lw, color=color)
    # three point line
    corner_three_a_left = Rectangle((-45, -22), 14, 0, linewidth=lw, color=color)
    corner_three_b_left = Rectangle((-45, 22), 14, 0, linewidth=lw, color=color)
    corner_three_a_right = Rectangle((31, -22), 14, 0, linewidth=lw, color=color)
    corner_three_b_right = Rectangle((31, 22), 14, 0, linewidth=lw, color=color)
    
    three_arc_left = Arc((-38, 0), 44.6, 44.6, theta1=270, theta2=90, linewidth=lw, color=color)
    three_arc_right = Arc((38, 0), 44.6, 44.6, theta1=90, theta2=270, linewidth=lw, color=color)
    
    # center court
    center_outer_arc = Arc((0, 0), 12, 12, theta1=0, theta2=360, linewidth=lw, color=color)
    center_inner_arc = Arc((0, 0), 4, 4, theta1=0, theta2=360, linewidth=lw, color=color)
    court_elements = [hoop_left, hoop_right, backboard_left, backboard_right, outer_box_left, outer_box_right,
                      inner_box_left, inner_box_right, top_free_throw_left, top_free_throw_right, 
                      bottom_free_throw_left, bottom_free_throw_right, restricted_left, restricted_right, 
                      corner_three_a_left, corner_three_b_left, corner_three_a_right, corner_three_b_right,
                      three_arc_left, three_arc_right, center_outer_arc, center_inner_arc]
    if outer_lines:
        outer_lines = Rectangle((-50, -25), 100, 50, linewidth=lw, color=color, fill=False)
        court_elements.append(outer_lines)
    for element in court_elements:
        ax.add_patch(element)
    return ax

# Create the plot
fig, ax = plt.subplots(figsize=(15, 8))

# Draw the court
draw_court(ax, outer_lines=True)

# Plot the shots
ax.scatter(game_shots_df['coordinate_x'], game_shots_df['coordinate_y'], c=game_shots_df['scoring_team'].map({'home': 'blue', 'away': 'orange'}), s=100, alpha=0.6, edgecolors='k')

# Customize plot
ax.set_title('Basketball Shot Chart')
ax.set_xlim(-50, 50)
ax.set_ylim(-25, 25)
ax.set_aspect('equal')  # Set the aspect ratio to make the court proportional
ax.set_xlabel('Court Length')
ax.set_ylabel('Court Width')
ax.legend(loc='upper right')

# Display the plot in Streamlit
st.pyplot(fig)