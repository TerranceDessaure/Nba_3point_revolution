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


