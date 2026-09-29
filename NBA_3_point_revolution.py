import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO
import time

# Config 
START_YEAR = 2006   # this is the END year of the season, e.g. 2006 = 2005-06 season
END_YEAR = 2025      # 2025 = 2024-25 season (most recently completed)
YEARS = list(range(START_YEAR, END_YEAR + 1))

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Pull data year by year 
all_seasons_data = []

for year in YEARS:
    print(f"Fetching {year-1}-{str(year)[-2:]} season...")
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # The "Team Per Game Stats" table has id="per_game-team"
        tables = pd.read_html(StringIO(response.text), attrs={"id": "per_game-team"})
        df = tables[0]
        df["SEASON"] = f"{year-1}-{str(year)[-2:]}"
        all_seasons_data.append(df)

    except Exception as e:
        print(f"  Failed for {year}: {e}")

    time.sleep(3)   # Basketball-Reference is stricter about scraping pace — keep this gap

# Combine into one DataFrame
full_df = pd.concat(all_seasons_data, ignore_index=True)

# Drop the "League Average" row that Basketball-Reference includes in each table
full_df = full_df[full_df["Team"] != "League Average"]

print(full_df[["SEASON", "Team", "3PA"]].head())

# Groupby: average 3PA per game, by season 
season_avg = full_df.groupby("SEASON")["3PA"].mean()
print(season_avg)

# Save the data 
full_df.to_csv("nba_team_stats_raw.csv", index=False)
season_avg.to_csv("nba_3pa_by_season.csv")

# 7. Plot
plt.figure(figsize=(10, 6))
season_avg.plot(marker="o")
plt.title("NBA Average 3-Point Attempts per Team per Game")
plt.xlabel("Season")
plt.ylabel("3PA per Game")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("three_point_trend.png", dpi=200, bbox_inches="tight")
plt.show()

# One-sentence finding
start_val = season_avg.iloc[0]
end_val = season_avg.iloc[-1]
pct_change = ((end_val - start_val) / start_val) * 100

print(
    f"Between {season_avg.index[0]} and {season_avg.index[-1]}, average NBA team "
    f"3-point attempts per game rose from {start_val: .1f} to {end_val:.1f}, "
    f"an increase of {pct_change:.0f}%."
)