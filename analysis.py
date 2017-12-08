import json #For JSON parsing
import urllib2 #Query the internet...
import csv #CSV format parsing
import StringIO #Writing out our csv files
from random import * #Random file names
import time #Sleep function so we can give API servers some relief
import os #Directory creation
import sys #For parsing args

print('Input file id for analysis')
fileId = raw_input()


with open('results_career/' + fileId + ' - data.csv', 'rb') as csvfile:

    #Array of career stats
    career_wl = []
    weekly_spm = []


    #Array of weekly KDRs
    weekly_tdm_wl = []
    weekly_tdm_kdr = []
    tdm_time_played = []


    #Declare our file read/write lib
    reader = csv.reader(csvfile)

    #Iterate through each stat and organize into usable data
    for row in reader:
        _career_wl = row[3]
        _weekly_spm = row[4]

        career_wl.append(_career_wl)
        weekly_spm.append(_weekly_spm)

    for i in range(0, len(career_wl)):
        print('Career W/L: ' + career_wl[i] + '\r\nWeekly SPM: ' + weekly_spm[i] + '\r\n\r\n')



    #Iterate through each stat and organize into usable data
    if 1 == 0:
    #for row in reader:


        _weekly_tdm_kdr = row[2]
        _weekly_wl_ratio = row[3]
        _tdm_time_played = row[4]

        #print(_weekly_kdr)
        weekly_tdm_kdr.append(_weekly_tdm_kdr)
        weekly_tdm_wl.append(_weekly_wl_ratio)
        tdm_time_played.append(_tdm_time_played)

    #for data in weekly_tdm_wl:
        #print(data)
