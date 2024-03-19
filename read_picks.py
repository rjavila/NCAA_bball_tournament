'''
Code to load xls file. This will read the entire file and manipulate it so it can be used further down the analysis. 
'''
import sys
import pandas as pd 

def read_madness(xlfilename):
    '''
    Read xls spreadsheet.
    '''
   
    xl = pd.read_excel(xlfilename,sheet_name=None,skiprows=3,index_col=0)

    pickstab = pd.DataFrame({},index=xl['Round 1'].index)

    for round in xl.keys():

        match round:

            case 'Round 1':

                colnames = [str(i) for i in range(1,33)]

            case 'Round 2':

                colnames = [str(i) for i in range(33,49)]

            case 'Sweet 16':

                colnames = [str(i) for i in range(49,57)]

            case 'Elite 8':
                
                colnames = [str(i) for i in range(57,61)]

            case 'Final Four':

                colnames = [str(i) for i in range(61,63)]

            case 'Championship':

                colnames = ['64']

        rd = pd.DataFrame(xl[round].values,index=list(xl[round].index),
                          columns=colnames)
        pickstab = pickstab.join(rd)

    return pickstab



if __name__ == "__main__":

    xlfilename = sys.argv[1]
    pickstab = read_madness(xlfilename)
