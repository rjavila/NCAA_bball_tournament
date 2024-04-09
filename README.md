# 2024 changes

The code `read_picks.py` is now used to read in the excel spreadsheets. 
Use `calc_results.py` to compute points and make plots. There are options in there to use different formulae.

# Introduction

This directory contains two scripts and a data directory that are used to 
calculate the cumulative points for MarsMadness bracket players. 

## Requirements

Python >= 3.10. You will also need 3 files in the data directory (YYYY corresponds
to the year in question):

YYYY MarsMadness picks list.xlsx
: Excel file containing a table of picks for every player for every game. The spreadsheet should contain one sheet per round, in addition to the table having a specific format. Look at one of the old files to figure out what this file should look like. 

YYYY_seeds.csv
: Simple text file containing a list of schools and their seed. (Seed,School)

YYYY_results.csv
: Text file containing a list of the winner of each game. The order of the games must match the order used in the excel spreadsheet. 


# Execution

All you need to run is the `calc_results.py` script. It has several command line
options, listed below.  

```
❯ python calc_results.py -h
usage: calc_results.py [-h] [--formula FORMULA] [--year YEAR] [--plot]

options:
  -h, --help         show this help message and exit
  --formula FORMULA  Formula to use.
  --year YEAR        Year you wish to process. If empty will default to
                     current year.
  --plot             Make plot
```

