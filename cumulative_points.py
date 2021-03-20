import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
from datetime import datetime

year = f'{datetime.now():%Y}'

#Reading in some static data to figure out points. 
seeds = pd.read_csv(f'data/{year}_seeds.csv',index_col='School')
results = pd.read_csv(f'data/{year}_results.txt')
rd1_pts = 3*seeds.loc[results.Winner.values]


#Set up column names for players table and then read in players table.
colnames = ['Player']
colnames = colnames + list(range(1,33))

players = pd.read_csv(f'data/{year}_spreadsheet_rd1.csv',
                      skiprows=5,
                      names=colnames,
                      index_col='Player',
                      comment='#'
                      )

players = players.T

plt.style.use('fivethirtyeight')
fig,ax = plt.subplots(1,1,figsize=(12,7),num='cumulative')
ax.set_prop_cycle(cycler(color=plt.get_cmap('tab20').colors))
xaxis = np.arange(1,results.size+1,dtype=int)

for player in players.columns:

    goodidx = players[player][:results.size].to_list()==results.Winner
    points_won = rd1_pts.Seed.where(goodidx.to_list(),other=0) 

    ax.plot(xaxis,
            points_won.cumsum(),
            lw=3,
            label=f'{player}: {points_won.sum()}')

ax.set_xticks(xaxis)
ax.set_xticklabels(xaxis)
ax.set_xlabel('Game number',fontsize='large')
ax.set_ylabel('Points won',fontsize='large')
ax.set_title(f'After {results.Winner.to_list()[-1]} win',fontsize='large')
plt.legend()
plt.tight_layout()

plt.savefig('2021_cumulative.png',dpi=300)
