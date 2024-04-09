import re
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import glob
from astropy.time import Time

round_id = 2
games = 2

def find_pick_list(person):

    #This section pulls out the JSON
    with open(person) as f1:
        soup = BeautifulSoup(f1,'html.parser')

    a = re.findall('({.+})',soup.text)

    for i in np.arange(len(a)):

        if 'DUKE' in a[i]:

            tab = pd.read_json(a[i])

    #Now we can dig into the table and extract the information 
    #we want.
    person_name = tab.loc['pick_data']['game_and_pick_list']['team_name'] 
    pick_list = []
    game_date = []

    for i in range(4):

        for j in range(games):
            pick_list.append(tab.loc['regions'][0][i]['rounds'][round_id]['games'][j]['user_pick']['pick'])
            game_date.append(tab.loc['regions'][0][i]['rounds'][round_id]['games'][j]['game_date'][:-4])
    game_dates = Time(game_date,format='iso')
    pick_list = np.array(pick_list)

    return person_name,pick_list[game_dates.argsort()],tab

def game_list(person):

    #This section pulls out the JSON
    with open(person) as f1:
        soup = BeautifulSoup(f1,'html.parser')

    a = re.findall('({.+})',soup.text)

    for i in np.arange(len(a)):

        if 'DUKE' in a[i]:

            tab = pd.read_json(a[i])

    #Now we can dig into the table and extract the information 
    #we want.
    person_name = tab.loc['pick_data']['game_and_pick_list']['team_name'] 
    gameteam = []
    gamedate = []

    for i in range(4):

        for j in range(games):
            home = tab.loc['regions'][0][i]['rounds'][round_id]['games'][j]['home_abbr']
            away = tab.loc['regions'][0][i]['rounds'][round_id]['games'][j]['away_abbr']
            gamedate.append(tab.loc['regions'][0][i]['rounds'][round_id]['games'][j]['game_date'][:-4])
            gameteam.append('{} vs {}'.format(home,away))
        
        gamedates = Time(list(gamedate),format='iso')
        idx = gamedates.argsort()
        gameteams = np.array(gameteam)

    return gameteams[idx],gamedates[idx]

def build_table():

    df = pd.DataFrame()
    people = glob.glob('raw_html/*html')

    for person in people:
    
        person_name,picks,tab = find_pick_list(person) 

        tbrow = pd.Series(name=person_name,data=picks)
        df = df.append(tbrow)

    header,dates = game_list(person)
    df.columns = header
    print(df)
    
    return df


if __name__ == "__main__":

    result = build_table()
