# NBA 3 point revolution

from nba_api.stats.endpoints import leaguedashteamstats

stats = leaguedashteamstats.LeagueDashTeamStats(season="2023-24")
df = stats.get_data_frames()[0]
print(df.head())