# Introduction

This directory contains two scripts that can be used to produce a table of
predictions by players in the NCAA bracket game.  

## Requirements

*user_urls.txt*:  This file contains a table (formatted as *ascii.basic*) 
that contains the name of the player and the URL where that player's bracket 
can be found. 

# Execution

The two scripts should be run from an ipython session. 

The first script, `scrape_website.py` will prompt you for a username and
password for the CBS Sports website (https://www.cbssports.com). Once logged in,
the code will download the raw html for each of the URLs in the *user_urls.txt* 
table.

*Change the round_id and games variables at the top of daily_picks.py*
The second script will search for the html files that the previous script 
downloaded and then process the information into a more useful format. It 
returns a pandas dataframe called *results*. Use this dataframe to create and 
write out the desired tables in whatever format you like.

