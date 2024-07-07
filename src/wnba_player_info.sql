create table wnba_player_info as (select
athlete_id,
athlete_name,
athlete_birthdate,
athlete_college,
CAST((CASE WHEN career_GP IN ('NA', '','--') THEN NULL ELSE career_GP END) AS double) AS career_GP,
CAST((CASE WHEN career_MIN IN ('NA', '','--') THEN NULL ELSE career_MIN END) AS double) AS career_MIN,
CAST((CASE WHEN career_PTS IN ('NA', '','--') THEN NULL ELSE career_PTS END) AS double) AS career_PTS,
CAST((CASE WHEN career_REB IN ('NA', '','--') THEN NULL ELSE career_REB END) AS double) AS career_REB,
CAST((CASE WHEN career_AST IN ('NA', '','--') THEN NULL ELSE career_AST END) AS double) AS career_AST,
CAST((CASE WHEN career_STL IN ('NA', '','--') THEN NULL ELSE career_STL END) AS double) AS career_STL,
CAST((CASE WHEN career_BLK IN ('NA', '','--') THEN NULL ELSE career_BLK END) AS double) AS career_BLK,
CAST((CASE WHEN career_TO IN ('NA', '','--') THEN NULL ELSE career_TO END) AS double) AS career_TO,
CAST((CASE WHEN career_FG_perc IN ('NA', '','--') THEN NULL ELSE career_FG_perc END) AS double) AS career_FG_perc,
CAST((CASE WHEN career_ThreeP_perc IN ('NA', '','--') THEN NULL ELSE career_ThreeP_perc END) AS double) AS career_ThreeP_perc,
CAST((CASE WHEN career_FT_perc IN ('NA', '','--') THEN NULL ELSE career_FT_perc END) AS double) AS career_FT_perc,
CAST((CASE WHEN career_PF IN ('NA', '','--') THEN NULL ELSE career_PF END) AS double) AS career_PF
from wnba_player_info_1);
