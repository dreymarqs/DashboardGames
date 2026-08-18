import pandas as pd
df_games = pd.read_csv('games.csv')
df_platforms = pd.read_csv('platform_summary.csv')
df_platforms.sort_index()
length = len(df_platforms)
print(length)
df_platforms.index = range(length)
print(df_platforms.head())