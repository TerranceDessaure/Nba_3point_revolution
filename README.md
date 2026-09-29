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
