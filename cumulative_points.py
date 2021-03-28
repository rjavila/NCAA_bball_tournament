'''
Script to make plot of cumulative points won as the tournament 
progresses.

Takes one argument, an integer signifying what round you are in.
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from cycler import cycler
from datetime import datetime


def get_rd1_points(results,seeds):

    rd1_factor = 3
    
    if results.size <= 32:
        rd1_pts = rd1_factor*seeds.loc[results.Winner.values]

    else:
        rd1_pts = rd1_factor*seeds.loc[results.Winner.values][:32]

    return rd1_pts


def get_rd2_points(results,seeds):

    rd2_factor = 2
    
    if results.size <= 48:
        rd2_pts = rd2_factor*seeds.loc[results.Winner.values][32:]

    else:
        rd2_pts = rd2_factor*seeds.loc[results.Winner.values][32:48]

    return rd2_pts

def get_rd3_points(results,seeds):

    rd3_const = 8
    
    if results.size <= 48:
        rd3_pts = rd3_const+seeds.loc[results.Winner.values][48:]

    else:
        rd3_pts = rd3_const+seeds.loc[results.Winner.values][48:56]

    return rd3_pts


def main(rnd):

    #Reading in some static data to figure out points. 
    year = f'{datetime.now():%Y}'

    seeds = pd.read_csv(f'data/{year}_seeds.csv',index_col='School')
    results = pd.read_csv(f'data/{year}_results.txt')

    rnd1_pts = get_rd1_points(results,seeds)
   
    all_points = rnd1_pts.copy()

    #Set up column names for players table and then read in players table.
    colnames = ['Player']
    colnames = colnames + list(range(1,33))

    readcsv_opts = {'skiprows':4,
                    'index_col':'Player',
                    'comment':'#'}

    players = pd.read_csv(f'data/{year}_spreadsheet_rd1.csv',names=colnames,
                          **readcsv_opts)
    players = players.T

    #Here we do further rounds when necessary.
    if rnd >= 2:
        colnames = ['Player']
        colnames = colnames + list(range(32,48))
        players = players.append(pd.read_csv(f'data/{year}_spreadsheet_rd2.csv',
                                 names=colnames,**readcsv_opts).T)
        all_points = all_points.append(get_rd2_points(results,seeds))

    if rnd >= 3:
        colnames = ['Player']
        colnames = colnames + list(range(48,56))
        players = players.append(pd.read_csv(f'data/{year}_spreadsheet_rd3.csv',
                                 names=colnames,**readcsv_opts).T)
        all_points = all_points.append(get_rd3_points(results,seeds))

    if rnd >= 4:
        players = players.append(pd.read_csv(f'data/{year}_spreadsheet_rd4.csv',
                                 **readcsv_opts).T)
        all_points = all_points.append(get_rd4_points(results,seeds))

    if rnd >= 5:
        players = players.append(pd.read_csv(f'data/{year}_spreadsheet_rd5.csv',
                                 **readcsv_opts).T)
        all_points = all_points.append(get_rd5_points(results,seeds))

    if rnd >= 6:
        players = players.append(pd.read_csv(f'data/{year}_spreadsheet_rd6.csv',
                                 **readcsv_opts).T)
        all_points = all_points.append(get_rd6_points(results,seeds))

    players.reset_index(drop=True,inplace=True)
    players = players.apply(lambda x: x.str.rstrip(' ][1234567890'))

    #We now have all the data we need. 
    #Settng up plot.
    plt.style.use('fivethirtyeight')
    fig,ax = plt.subplots(1,1,figsize=(12,7),num='cumulative')
    ax.set_prop_cycle(cycler(color=plt.get_cmap('tab20').colors))
    xaxis = np.arange(1,results.size+1,dtype=int)

    #This is where the work gets done, each player's data gets added
    #to the plot.
    for player in players.columns:

        goodidx = players[player][:results.size].to_list()==results.Winner
        points_won = all_points.Seed.where(goodidx.to_list(),other=0) 

        ax.plot(xaxis,
                points_won.cumsum(),
                lw=3,
                label=f'{player}: {points_won.sum()}')

    
    #Finishing up plot.
    ax.set_xticks(xaxis)
    ax.set_xticklabels(xaxis,size='x-small',rotation=90)
    ax.set_xlabel('Game number',fontsize='large')
    ax.set_ylabel('Points won',fontsize='large')
    ax.set_title(f'After {results.Winner.to_list()[-1]} win',
                 fontsize='large')
    ax.axvspan(1,32,facecolor='k',alpha=0.05)
    ax.text(31.9,10,'Round 1',ha='right',rotation=90)
    ax.text(47.9,10,'Round 2',ha='right',rotation=90)
    ax.axvspan(48,56,facecolor='k',alpha=0.05)
    ax.text(55.9,10,'Sweet 16',ha='right',rotation=90)
    plt.legend()
    plt.tight_layout()

    plt.savefig('2021_cumulative.png',dpi=300)

    return players


if __name__ == '__main__':

    rnd = int(sys.argv[1])
    tab = main(rnd)
