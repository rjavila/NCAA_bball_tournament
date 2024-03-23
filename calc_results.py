'''
Script to calculate results of bracket predictions. Needs to read in 
predictions table (from `read_picks`), results table, and seeds table.
'''
# Global
import sys
import argparse
from datetime import datetime 
from itertools import product

# Dependencies
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import transforms

# Local
from read_picks import read_madness

def main(year):

    #Reading in some static data to figure out points.
    pickstab = read_madness(f'data/{year}/{year} MarsMadness picks list.xlsx')
    year = f'{datetime.now():%Y}'

    seeds = pd.read_csv(f'data/{year}/{year}_seeds.csv',index_col='School')
    results = pd.read_csv(f'data/{year}/{year}_results.txt')

    winners_list = ['']*63
    winners_list[:len(results['Winner'])] = results['Winner'].to_list()

    winners_seeds = [0]*63
    seeds_list = [seeds.loc[school].values[0] for school in results['Winner']]
    winners_seeds[:(games_played := len(seeds_list))] = seeds_list

    match int(year):

        case 2019 | 2020 | 2021:

            pass 

        case 2024:

            awarded_points = formula3(winners_seeds)

    awarded_points[games_played:] = np.nan
    pointstab = pd.DataFrame().reindex_like(pickstab)
    
    
    for i,row in pointstab.iterrows():
        
        row.where(pickstab.loc[i]!=winners_list,awarded_points,
                  inplace=True)
        idx = row[:games_played].isna()
        row[:games_played][idx] = 0
        
    return pointstab,results.values[-1][0],games_played
    
def make_plot(pointstab,latest_winner,games_played,year):
    '''
    Function to generate cumulative points plot.
    '''

    # Setting up plot
    plt.style.use('fivethirtyeight')
    plt.close('all')

    fig,ax = plt.subplots(1,1,figsize=(14,7),num='cumulative')

    colorstuple = plt.get_cmap('tab20').colors
    colorstuple += colorstuple
    #lslist = ['-','--']

    #linelist = []
    #for i in product(colorstuple,lslist):
    #    linelist.append(i)

    colordict = {}
    for i,player in enumerate(pointstab.index):

        colordict[player] = colorstuple[i]


    xaxis = np.arange(1,64)
    trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)

    players = pointstab.sum(axis=1).sort_values(ascending=False).index
    for player in players:

        match player:

            case 'Chalk':

                ax.plot(xaxis,pointstab.loc[player].cumsum(),
                        c='k',lw=2,
                        label=f'{player}: {int(pointstab.loc[player].sum())}'
                        )

            case other:

                ax.plot(xaxis,pointstab.loc[player].cumsum(),
                        c=colordict[player],
                        lw=2,
                        label=f'{player}: {int(pointstab.loc[player].sum())}'
                        )

    # Finishing up plot.
    ax.set_xticks(xaxis)
    ax.set_xticklabels(xaxis,size='x-small',rotation=90)
    ax.set_xlabel('Game number',fontsize='large')
    ax.set_ylabel('Points won',fontsize='large')
    ax.set_xlim(1,games_played)
    ax.set_title(f'After {latest_winner} win',
                 fontsize='large')


    ax.axvspan(1,32,facecolor='k',alpha=0.05)
    ax.text(32,0.015,'Round 1',ha='right',rotation=90,
            transform=trans)

    ax.text(48,0.015,'Round 2',ha='right',rotation=90,
            transform=trans)

    ax.axvspan(48,56,facecolor='k',alpha=0.05)
    ax.text(56,0.015,'Sweet 16',ha='right',rotation=90,
            transform=trans)

    ax.text(60,0.015,'Elite 8',ha='right',rotation=90,
            transform=trans)

    ax.axvspan(60,62,facecolor='k',alpha=0.05)
    ax.text(62,0.015,'Final Four',ha='right',rotation=90,
            transform=trans)

    ax.text(63,0.015,'CHAMPIONSHIP',ha='right',rotation=90,color='green',
            transform=trans)

    plt.legend(ncol=2,fontsize='small')

    plt.savefig(f'{year}_cumulative.png',dpi=300)
    
def formula3(winners_seeds):
    
    awarded_points = np.full(63,np.nan)

    for i,winner_seed in enumerate(winners_seeds):

        if i < 48: # Round 1 & 2: 3 X seed

            awarded_points[i] = winner_seed * 3 

        elif (i>=48) & (i<56) & (winner_seed!=0): # Sweet 16: seed + 16
            
            awarded_points[i] = winner_seed + 16

        elif (i>=56) & (i<60) & (winner_seed!=0): # Elite 8: seed + 32

            awarded_points[i] = winner_seed + 32

        elif (i>=60) & (i<62) & (winner_seed!=0): # Final Four: 48

            awarded_points[i] = 48

        elif (i==62) & (winner_seed!=0): # Championship: 64

            awarded_points[i] = 64


    return awarded_points






if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--year',type=str,default='',
                        help='Year you wish to process. If empty will\
                        default to current year.')
    parser.add_argument('--plot',action='store_true',default=False,
                        help='Make plot')
    args = parser.parse_args()
    
    if args.year == '':

        year = f'{datetime.now():%Y}'

    print(f'Processing {year}')
    pointstab,latest_winner,games_played = main(year)

    if args.plot:

        make_plot(pointstab,latest_winner,games_played,year)
    
