# Nba_3point_revolution
How have three-point attempts per team per game changed in the NBA over the last 20 seasons?
Where I am getting the data?
- Basketball-Reference: the team per-game stats table have a 3PA column for each season. Export to CVS.
- nba_api (Python packeage): pulls team stats programmatically
# Step 1: Imports

import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO
import time

Description of each Library
pandas -- the core library for working with tabular data (rows and columns, like spreadsheets)

matplotlib -- drawing charts

request-- lets Python act like a web browser and fetch a webpage's raw content

StringIO -- a small utility that lets pandas read text(like the HTML I downloaded) as if it were a file, without actually saving anything to disk fist.

time -- gives you time.sleep(), which pauses code for a few seconds. Use this to avoid hammering the website with request to fast.

<img width="268" height="95" alt="image" src="https://github.com/user-attachments/assets/a155bb71-411b-44a9-a6d0-06331a08110b" />

# Step 2: Config

<img width="708" height="165" alt="image" src="https://github.com/user-attachments/assets/06cfb78b-f574-4d8f-abae-08e872f4e7cd" />

Build list of numbers: the +1 is needed because  range stops before its second number) and  list(...) turns into a list we can loop over

Next we create the dictionary. When the script requests a webpage, it identifies itself to the server. By default, request announces itself as a Python script, and some sites block that. This header disguises your request as comming from a normal Chrome browser instead.

# Section 3: The main loop -- fetching data

<img width="208" height="43" alt="image" src="https://github.com/user-attachments/assets/cc8deb06-dcb2-4372-bea5-ab1d7f89e8c1" />

An empty list. Fill it with one table (DataFrame) per season, then glue them together later

<img width="148" height="20" alt="image" src="https://github.com/user-attachments/assets/95bde9c4-4d03-4e7e-819e-99894574c6e6" />

This runs everything indented below it once for each year in our list - so 20 times total, once per season.

The next line is just a progress massage so you can see it working,. There is a f-string that lets you drop variable directly in the text. str(year)[-2:] tales the last two characters of the year as text (eg. "2024' -> '24')

A try/execpt block. Python attempts everyting inside try:. If anything goes wrong (site down, pare format changed, network hiccup), instead of crashing the script, it jumps to the except, prints what went wrong, and moves on to the next season. This is so one bad season does not ruin the entire code.

<img width="467" height="34" alt="image" src="https://github.com/user-attachments/assets/4ff7cb42-bf0f-424a-9d9c-3133a52936c6" />

'requests.get()' actually fetches the webpage -- 'response' now holds everything that cam back ( the HTML, status code, etc.). 'timeout=30' means "give up if this takes longer than 30 seconds." 'raise_for_status()' checks: did the server return an error. If so , it triggers the except block instead of silently continuing with broken data.

<img width="618" height="41" alt="image" src="https://github.com/user-attachments/assets/ffeef830-4cc4-4d37-b65e-d7989aa90ba7" />

'response.text' is the raw HTML of the page. 
'pd.read_html()'  scans it and finds <table>  elements converting each into a pandas DataFrame.
'attrs={"id": "per_game-team"}' tell pandas "only give me the one table with this specific ID," which is the exact table with per-game team stats. It still return a list of matches (usually just one), so 'table[0]' grabs that single table out of the list.




