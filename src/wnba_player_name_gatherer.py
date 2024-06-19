from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


WNBA_PLAYER_URL_PREFIX = "https://www.espn.com/wnba/player/_/id/"


def extract_athlete_name(athlete_id):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
	}
	
	response = requests.get(WNBA_PLAYER_URL_PREFIX + str(athlete_id), headers=headers)
	
	if response.status_code == 200:
	
		html_content = response.text
		soup = BeautifulSoup(html_content, 'html.parser')
		
		h1_tag = soup.find('h1', class_='PlayerHeader__Name')
		first_name = h1_tag.find('span', class_='fw-light').get_text(strip=True)
		last_name = h1_tag.find_all('span')[1].get_text(strip=True)
		
		birthdate = None
		if (soup.find('div', text='Birthdate') != None):
			birthdate = soup.find('div', text='Birthdate').find_next_sibling('div').text.strip()
			birthdate = re.sub(r'\s*\(.*?\)', '', birthdate)
			birthdate = birthdate.replace(" ", "").replace("\t", "").replace("\n", "")
		
		college = None
		if (soup.find('div', text='College') != None):
			college = soup.find('div', text='College').find_next_sibling('div').text.strip()
		
		career_stats_tup = (None, None, None, None, None, None, None, None, None, None, None, None)
		player_stats = soup.find('section', class_='Card PlayerStats')
		if player_stats:
			career_row = player_stats.find_all('tbody', class_='Table__TBODY')[-1].find_all('tr', class_='Table__TR Table__TR--sm Table__even')[-1]
			if career_row:
				values = [td.text.strip() for td in career_row.find_all('td')]
				GP = values[0]
				MIN = values[1]
				PTS = values[2]
				REB = values[3]
				AST = values[4]
				STL = values[5]
				BLK = values[6]
				TO = values[7]
				FG_perc = values[8]
				ThreeP_perc = values[9]
				FT_perc = values[10]
				PF = values[11]
				career_stats_tup = (GP, MIN, PTS, REB, AST, STL, BLK, TO, FG_perc, ThreeP_perc, FT_perc, PF)
		
		return (first_name + " " + last_name, birthdate, college, career_stats_tup)
					
	else:
		return None


df = pd.read_csv("Data/athlete_ids.csv")

athlete_ids = df['athlete_id']
athlete_names = [extract_athlete_name(athlete_id)[0] for athlete_id in athlete_ids]
athlete_birthdates = [extract_athlete_name(athlete_id)[1] for athlete_id in athlete_ids]
athlete_colleges = [extract_athlete_name(athlete_id)[2] for athlete_id in athlete_ids]
GP = [extract_athlete_name(athlete_id)[3][0] for athlete_id in athlete_ids]
MIN = [extract_athlete_name(athlete_id)[3][1] for athlete_id in athlete_ids]
PTS = [extract_athlete_name(athlete_id)[3][2] for athlete_id in athlete_ids]
REB = [extract_athlete_name(athlete_id)[3][3] for athlete_id in athlete_ids]
AST = [extract_athlete_name(athlete_id)[3][4] for athlete_id in athlete_ids]
STL = [extract_athlete_name(athlete_id)[3][5] for athlete_id in athlete_ids]
BLK = [extract_athlete_name(athlete_id)[3][6] for athlete_id in athlete_ids]
TO = [extract_athlete_name(athlete_id)[3][7] for athlete_id in athlete_ids]
FG_perc = [extract_athlete_name(athlete_id)[3][8] for athlete_id in athlete_ids]
ThreeP_perc = [extract_athlete_name(athlete_id)[3][9] for athlete_id in athlete_ids]
FT_perc = [extract_athlete_name(athlete_id)[3][10] for athlete_id in athlete_ids]
PF = [extract_athlete_name(athlete_id)[3][11] for athlete_id in athlete_ids]

new_df = pd.DataFrame({'athlete_id': athlete_ids,
					   'athlete_name': athlete_names,
					   'athlete_birthdate': athlete_birthdates,
					   'athlete_college': athlete_colleges,
					   'career_GP': GP,
					   'career_MIN': MIN,
					   'career_PTS': PTS,
					   'career_REB': REB,
					   'career_AST': AST,
					   'career_STL': STL,
					   'career_BLK': BLK,
					   'career_TO': TO,
					   'career_FG_perc': FG_perc,
					   'career_ThreeP_perc': ThreeP_perc,
					   'career_FT_perc': FT_perc,
					   'career_PF': PF
					  })

new_df.to_csv("Data/athlete_id_name_mapping.csv", index=False)
