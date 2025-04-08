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

# Champions

## List of yearly top 3 

| Year | 🏅 | 🥈 | 🥉 |
| ---- | -- | -- | -- |
| 2025 | Tyler | J. Ro | Roberto |
| 2024 | J. Ro | Conner | James |
| 2023 | Kevin | Nate | James |
| 2022 | Cara | Deep | Elaine |
| 2021 | Conner | Tyler | J. Ro |
| 2020 | 🦠 | 🦠 | 🦠 |
| 2019 | J. Ro | Nate | Elaine |
| 2018 | Conner | J. Ro | James |
| 2017 | Elaine | James | Barack |
| 2016 | Roberto | Jo | J. Ro |
| 2015 | Miranda | Ariel | Roberto |

## Most successful players 

| Player | 🏅 | 🥈 | 🥉 |
| ---- | -- | -- | -- |
| J. Ro    | 2 (2019, 2024) | 2 (2018, 2025) | 2 (2016, 2021)       |
| Conner   | 2 (2018, 2021) | 1 (2024)       |                      |
| 🦠       | 1 (2020)       | 1 (2020)       | 1 (2020)             |
| Tyler    | 1 (2025)       | 1 (2021)       |                      |
| Elaine   | 1 (2017)       |                | 1 (2019, 2022)       |
| Roberto  | 1 (2016)       |                | 1 (2015, 2025)       |
| Kevin    | 1 (2023)       |                |                      |
| Cara     | 1 (2022)       |                |                      |
| Miranda  | 1 (2015)       |                |                      |
| Nate     |                | 2 (2019, 2023) |                      |
| James    |                | 1 (2021)       | 3 (2018, 2023, 2024) |
| Deep     |                | 1 (2022)       |                      |
| Jo       |                | 1 (2016)       |                      |
| Ariel    |                | 1 (2015)       |                      |
| Barack   |                |                | 1 (2017)             |
