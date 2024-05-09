from datetime import datetime
import numpy as np
import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

nba_players = pd.read_csv('nba_players_is_active.csv')
current_nba_player_info = pd.read_csv('all_players_career_stats.csv')
def process_user_answers(user_answers):
    

    nba_player_info_list = []
    career_info_list = []
    for x in range(4):  
      nba_player_info, career_info = get_player(x)
      nba_player_info_list.append(nba_player_info)
      career_info_list.append(career_info)

    main_player_info, main_career_info = get_player(-1)
    for index in range(4):
       for stat in ['PTS','REB','AST','STL','BLK']:
          a=float(career_info_list[index].iloc[0][stat])
          b=float(career_info.iloc[0][stat])
      
          if  a > b:
            if user_answers[stat.lower()+str(index)] == "Over":
               user_answers[stat.lower()+str(index)] = "T"
            else:
               user_answers[stat.lower()+str(index)] = "F"
   
          else:
            if user_answers[stat.lower()+str(index)] == "Over":
               user_answers[stat.lower()+str(index)] = "F"
            else:
               user_answers[stat.lower()+str(index)] = "T"
  
    return user_answers



def get_player(i):
    
    today = datetime.now().strftime('%Y%m%d')
    
    random_state = np.random.RandomState(seed=int(today)+i)
    
    nba_player_info = nba_players.sample(1, random_state=random_state)
    player_id = nba_player_info['id'].values[0]

   
    get_player_info=current_nba_player_info[current_nba_player_info['PLAYER_ID'] == player_id]

 
    career_info = get_player_info[['PLAYER_AGE', 'GP', 'FG_PCT', 'REB', 'AST', 'STL',
       'BLK', 'TOV', 'PF', 'PTS','TEAM_ABBREVIATION','GP',"SEASON_ID"]].sample(1, random_state=random_state)
    
    return nba_player_info['full_name'].values[0], career_info


get_player(1)
