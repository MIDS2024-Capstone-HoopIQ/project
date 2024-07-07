CREATE EXTERNAL TABLE IF NOT EXISTS wnba_db.wnba_player_info_1 (
    athlete_id INT,
    athlete_name STRING,
    athlete_birthdate STRING,
    athlete_college STRING,
    career_GP STRING,
    career_MIN STRING,
    career_PTS STRING,
    career_REB STRING,
    career_AST STRING,
    career_STL STRING,
    career_BLK STRING,
    career_TO STRING,
    career_FG_perc STRING,
    career_ThreeP_perc STRING,
    career_FT_perc STRING,
    career_PF STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '\"'
)
LOCATION 's3://wnbadata/player-info/'
TBLPROPERTIES (
    'skip.header.line.count'='1',
    'has_encrypted_data'='false'
);