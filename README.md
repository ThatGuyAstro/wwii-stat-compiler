# CoD WWII Stat Compiler and Analyzer

![program-screenshot](https://im4.ezgif.com/tmp/ezgif-4-141d0e0620.gif)

This is a tool designed to collect (and later analyze) stats that may hold influence over SBMM in CoD WWII

For the time being, SBMM is **not proven**, **nor disproven**, but this tool hopefully will aid in the process of coming to an accurate conclusion over the matter. During this state of uncertainty, please do not skip to conclusions as to whether or not SMBB exists.

# Disclaimer

#### Do not spam API calls or the resources supplied by Activision/Sledgehammer
It's been years since we've been able to accurately (let alone officially) collect stats from a CoD game. The fact this API doesn't require an API-key and is publicly accessible should be viewed as a priviledge.

#### I am not associated with Sledgehammer or Activision in anyway
Just mentioning this so there's no confusion.

# CSV Formatting
This project uses a few CSV files all with their own formatting.

These files include: accounts.csv, results_career.csv, and results_tdm.csv

#### accounts.csv
By default there are two accounts already implemented into the file, those being:
- DRIFT0R_actual,psn
- xclusiveace,psn

Formatting of these entries are as follows:
*gamertag*,*platform*

If there are spaces in the gamertag, replace them with underscores. (I will automate this later when I have time)

Platforms include:
- psn
- xbl
- steam

# Usage
Download or clone the repo onto your system, input the accounts you would like to query into **accounts.csv**, and then execute **main.py** via Python.
