CREATE TABLE wnba_teambox AS (
SELECT
    CAST(game_id AS BIGINT) AS game_id,
    CAST(season AS INT) AS season,
    CAST(season_type AS INT) AS season_type,
    CAST(game_date AS DATE) AS game_date,
    CAST(game_date_time AS TIMESTAMP) AS game_date_time,
    CAST(team_id AS INT) AS team_id,
    team_uid,
    team_slug,
    team_location,
    team_name,
    team_abbreviation,
    team_display_name,
    team_short_display_name,
    team_color,
    team_alternate_color,
    team_logo,
    team_home_away,
    CAST(team_score AS INT) AS team_score,
    CAST(team_winner AS BOOLEAN) AS team_winner,
    CAST(assists AS INT) AS assists,
    CAST(blocks AS INT) AS blocks,
    CAST(defensive_rebounds AS INT) AS defensive_rebounds,
    CAST(0 AS INT) as fast_break_points,
    CAST(field_goal_pct AS DOUBLE) AS field_goal_pct,
    CAST(field_goals_made AS INT) AS field_goals_made,
    CAST(field_goals_attempted AS INT) AS field_goals_attempted,
    CAST(flagrant_fouls AS INT) AS flagrant_fouls,
    CAST(fouls AS INT) AS fouls,
    CAST(free_throw_pct AS DOUBLE) AS free_throw_pct,
    CAST(free_throws_made AS INT) AS free_throws_made,
    CAST(free_throws_attempted AS INT) AS free_throws_attempted,
    largest_lead,
    CAST(offensive_rebounds AS INT) AS offensive_rebounds,
    CAST(0 AS INT) as points_in_paint,
    CAST(steals AS INT) AS steals,
    CAST(team_turnovers AS INT) AS team_turnovers,
    CAST(technical_fouls AS INT) AS technical_fouls,
    CAST(three_point_field_goal_pct AS DOUBLE) AS three_point_field_goal_pct,
    CAST(three_point_field_goals_made AS INT) AS three_point_field_goals_made,
    CAST(three_point_field_goals_attempted AS INT) AS three_point_field_goals_attempted,
    CAST(total_rebounds AS INT) AS total_rebounds,
    CAST(total_technical_fouls AS INT) AS total_technical_fouls,
    CAST(total_turnovers AS INT) AS total_turnovers,
    CAST(0 AS INT) as turnover_points,
    CAST(turnovers AS INT) AS turnovers,
    CAST(opponent_team_id AS INT) AS opponent_team_id,
    opponent_team_uid,
    opponent_team_slug,
    opponent_team_location,
    opponent_team_name,
    opponent_team_abbreviation,
    opponent_team_display_name,
    opponent_team_short_display_name,
    opponent_team_color,
    opponent_team_alternate_color,
    opponent_team_logo,
    opponent_team_score
FROM wnba_db.wnba_teambox_2018_22_raw
UNION ALL
SELECT
    CAST(game_id AS BIGINT) AS game_id,
    CAST(season AS INT) AS season,
    CAST(season_type AS INT) AS season_type,
    CAST(game_date AS DATE) AS game_date,
    CAST(game_date_time AS TIMESTAMP) AS game_date_time,
    CAST(team_id AS INT) AS team_id,
    team_uid,
    team_slug,
    team_location,
    team_name,
    team_abbreviation,
    team_display_name,
    team_short_display_name,
    team_color,
    team_alternate_color,
    team_logo,
    team_home_away,
    CAST(team_score AS INT) AS team_score,
    CAST(team_winner AS BOOLEAN) AS team_winner,
    CAST(assists AS INT) AS assists,
    CAST(blocks AS INT) AS blocks,
    CAST(defensive_rebounds AS INT) AS defensive_rebounds,
    CAST(fast_break_points AS INT) AS fast_break_points,
    CAST(field_goal_pct AS DOUBLE) AS field_goal_pct,
    CAST(field_goals_made AS INT) AS field_goals_made,
    CAST(field_goals_attempted AS INT) AS field_goals_attempted,
    CAST(flagrant_fouls AS INT) AS flagrant_fouls,
    CAST(fouls AS INT) AS fouls,
    CAST(free_throw_pct AS DOUBLE) AS free_throw_pct,
    CAST(free_throws_made AS INT) AS free_throws_made,
    CAST(free_throws_attempted AS INT) AS free_throws_attempted,
    largest_lead,
    CAST(offensive_rebounds AS INT) AS offensive_rebounds,
    CAST(points_in_paint AS INT) AS points_in_paint,
    CAST(steals AS INT) AS steals,
    CAST(team_turnovers AS INT) AS team_turnovers,
    CAST(technical_fouls AS INT) AS technical_fouls,
    CAST(three_point_field_goal_pct AS DOUBLE) AS three_point_field_goal_pct,
    CAST(three_point_field_goals_made AS INT) AS three_point_field_goals_made,
    CAST(three_point_field_goals_attempted AS INT) AS three_point_field_goals_attempted,
    CAST(total_rebounds AS INT) AS total_rebounds,
    CAST(total_technical_fouls AS INT) AS total_technical_fouls,
    CAST(total_turnovers AS INT) AS total_turnovers,
    CAST(turnover_points AS INT) AS turnover_points,
    CAST(turnovers AS INT) AS turnovers,
    CAST(opponent_team_id AS INT) AS opponent_team_id,
    opponent_team_uid,
    opponent_team_slug,
    opponent_team_location,
    opponent_team_name,
    opponent_team_abbreviation,
    opponent_team_display_name,
    opponent_team_short_display_name,
    opponent_team_color,
    opponent_team_alternate_color,
    opponent_team_logo,
    opponent_team_score
FROM wnba_db.wnba_teambox_2023_24_raw
);