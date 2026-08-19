import pandas as pd
df_games = pd.read_csv('games.csv')
df_platforms = pd.read_csv('platform_summary.csv')
df_platforms.reset_index(inplace=True)
df_games['platform'] = df_games['platform'].map(df_platforms.set_index('platform')['index'])

df_games = df_games.drop(columns=['platform_type','platform_maker','platform_generation'])
print(df_games.info())
df_sales = pd.DataFrame()
colunas_desejadas = ['game_id','na_sales_million','eu_sales_million','jp_sales_million','other_sales_million','global_sales_million','estimated_revenue_million_usd']
df_sales= df_games[colunas_desejadas].copy()
print(df_sales.head())
# 0 idx do game
# 1 na_sales_million                    
# 2  eu_sales_million                   
# 3  jp_sales_million                    
# 4  other_sales_million                 
# 5  global_sales_million                
# 6  estimated_revenue_million_usd       