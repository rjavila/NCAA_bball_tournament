import requests
import getpass
from astropy.table import Table

#This is where the html files for each user are going to be 
#stored.
tab = Table.read('user_urls.txt',format='ascii.basic')
outpath = 'raw_html_files/'


#This is the stuff for loggin in to the CBS website
loginurl = 'https://www.cbssports.com/login'

values = {'userid':input('login: '),
          'password':getpass.getpass()
         }

mysesh = requests.Session()

print('Logging in')
r = mysesh.post(loginurl,data=values)

#Here's where we're gonna loop through each player and scrape the
#raw html of their bracket.

for i in range(len(tab)):

    outfile = '{}{}.html'.format(outpath,tab['player'][i])
    print('Saving {}'.format(outfile))
    rawhtml = mysesh.get(tab['url'][i])
    
    with open(outfile,'w') as f1:
        f1.write(rawhtml.text)

print('Done')
