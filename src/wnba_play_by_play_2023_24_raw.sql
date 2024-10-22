CREATE EXTERNAL TABLE IF NOT EXISTS wnba_db.wnba_play_by_play_2023_24_raw (
    record_number STRING,
    game_play_number INT,
    id STRING,
    sequence_number STRING,
    type_id STRING,
    type_text STRING,
    text STRING,
    away_score INT,
    home_score INT,
    period_number INT,
    period_display_value STRING,
    clock_display_value STRING,
    scoring_play BOOLEAN,
    score_value INT,
    team_id STRING,
    athlete_id_1 STRING,
    athlete_id_2 STRING,
    athlete_id_3 STRING,
    wallclock STRING,
    shooting_play BOOLEAN,
    coordinate_x_raw DOUBLE,
    coordinate_y_raw DOUBLE,
    game_id STRING,
    season INT,
    season_type STRING,
    home_team_id STRING,
    home_team_name STRING,
    home_team_mascot STRING,
    home_team_abbrev STRING,
    home_team_name_alt STRING,
    away_team_id STRING,
    away_team_name STRING,
    away_team_mascot STRING,
    away_team_abbrev STRING,
    away_team_name_alt STRING,
    game_spread DOUBLE,
    home_favorite BOOLEAN,
    game_spread_available BOOLEAN,
    home_team_spread DOUBLE,
    qtr INT,
    time STRING,
    clock_minutes INT,
    clock_seconds DOUBLE,
    home_timeout_called STRING,
    away_timeout_called STRING,
    half INT,
    game_half STRING,
    lead_qtr STRING,
    lead_half STRING,
    start_quarter_seconds_remaining STRING,
    start_half_seconds_remaining STRING, 
    start_game_seconds_remaining STRING,
    end_quarter_seconds_remaining STRING,
    end_half_seconds_remaining STRING,
    end_game_seconds_remaining STRING,
    period INT,
    lag_qtr STRING,
    lag_half STRING,
    coordinate_x DOUBLE,
    coordinate_y DOUBLE,
    game_date STRING,
    game_date_time STRING,
    type_abbreviation STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '\"'
)
LOCATION 's3://wnbadata/play-by-play/2023-24/'
TBLPROPERTIES (
    'skip.header.line.count'='1',
    'has_encrypted_data'='false'
);