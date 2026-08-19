import pandas as pd
df_games = pd.read_csv('games.csv')
df_platforms = pd.read_csv('platform_summary.csv')
df_publisher = pd.read_csv('publisher_summary.csv')
df_genres = pd.read_csv('genre_summary.csv')
df_platforms = pd.read_csv('platform_summary.csv')

df_platforms.reset_index(inplace=True)
df_games['platform'] = df_games['platform'].map(df_platforms.set_index('platform')['index'])
df_games = df_games.drop(columns=['platform_type','platform_maker','platform_generation'])