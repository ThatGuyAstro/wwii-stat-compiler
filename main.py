'''

Author: @ThatGuyAstro, or /u/thatguyastro
Any modifications are welcomed, credit is appreciated but not necessary.

CSV format (career):
platform,gamertag,career_kdr,career_w/l (percentage),weekly_spm

CSV format (tdm):
platform,gamertag,weekly_tdm_kdr,weekly_tdm_w/l (percentage),tdm_time_played

DISCLAIMER:

Please do not spam the Sledgehammer API server with requests. We are finally able to access
player-data through an official avenue, in this case it's an API. Do not abuse this API
or the systems Activision/Sledgehammer have put in place.

I as the author of this script am not affiliated nor in any way associated with Activition/Sledgehammer.

Example API url: https://my.callofduty.com/api/papi-client/crm/cod/v2/title/wwii/platform/psn/gamer/drift0r_actual/profile

'''

import json #For JSON parsing
import urllib2 #Query the internet...
import csv #CSV format parsing
import StringIO #Writing out our csv files
from random import * #Random file names
import time #Sleep function so we can give API servers some relief
import os #Directory creation

def safe_div(x,y):
    if y == 0:
        return 0
    return x / y

#Create our directories for holding stats
if not os.path.exists('results_career'):
    os.makedirs('results_career')

if not os.path.exists('results_tdm'):
    os.makedirs('results_tdm')

#Set every thing up under an umbrella try-statement
try:

    #Iterate through our entries under accounts.csv
    with open('accounts.csv', 'rb') as csvfile:

        #Our UID (unique identifier) prefix for results (helps w/ cross referencing data)
        rand_prefix = str(randint(1000, 9999)) #Prefix on our random file name

        #Variables for career-based stats
        filePath_career = 'results_career/' + rand_prefix + " - data.csv" #Path for our career-based data

        #Variables for tdm-based stats
        filePath_tdm = 'results_tdm/' + rand_prefix + " - data.csv" #Path for our tdm-based data

        #Declare our file read/write lib
        reader = csv.reader(csvfile)
        for row in reader:


            #----------------------
            #Fetch our career stats
            #----------------------

            #Keep the user in the loop
            print('Fetching and recording data for: ' + row[0] + ' on platform: ' + row[1])

            #API url with the profile parameters
            url = "https://my.callofduty.com/api/papi-client/crm/cod/v2/title/wwii/platform/{}/gamer/{}/profile".format(row[1], row[0])

            #Hold our return data in a variable
            data = json.load(urllib2.urlopen(url))

            #Parse our career data and hold it in its own variable
            data_lifetime = data['data']['mp']['lifetime']['all']

            #Declare the data we are looking for as variables...
            career_kdr = data_lifetime['kdRatio']
            career_wins = data_lifetime['wins']
            career_losses = data_lifetime['losses']


            career_wl = (safe_div(career_wins, career_losses)) * 100 #Our winloss ratio as a percentage

            weekly_spm = data['data']['mp']['weekly']['all']['scorePerMinute']

            #Open our data file in append-mode
            f=open(filePath_career, "a+")

            #Write/append our data to the file
            f.write('{},{},{},{},{}\r\n'.format(row[1], row[0], career_kdr, career_wl, weekly_spm))





            #-------------------------------
            #Now we fetch our stats for TDM
            #-------------------------------

            #Parse our tdm data and hold it in its own variable
            data_tdm = data['data']['mp']['lifetime']['mode']['dm']

            #Declare the data we are looking for as variables...
            tdm_kills = data_tdm['kills']
            tdm_deaths = data_tdm['deaths']

            tdm_kdr = safe_div(tdm_kills, tdm_deaths) #Calculate our kill-death ratio

            tdm_wins = data_tdm['wins']
            tdm_losses = data_tdm['losses']

            #Set our default w/l to 0 in case we discover a 0 value during division
            tdm_wl = 0


            tdm_wl = (safe_div(tdm_wins, tdm_losses)) * 100 #Calculate our win-loss ratio as a percentage


            tdm_timeplayed = data_tdm['timePlayed'] #Our time played in seconds

            #Open our data file in append-mode
            f=open(filePath_tdm, "a+")

            #Write/append our data to the file
            f.write('{},{},{},{},{}\r\n'.format(row[1], row[0], tdm_kdr, tdm_wl, tdm_timeplayed))

            #Let the user know we've collected and recorded our results
            print('... done. \r\n\r\n')

            #Pause our script for 5 seconds so we don't overload API servers
            time.sleep(1)

        #Let our user know that we're done with current iteration
        print('Finished recording stats. \r\nFile id: ' + rand_prefix)

except Exception as e:
    print('oops... looking like we encountered an error')
    print(e)
