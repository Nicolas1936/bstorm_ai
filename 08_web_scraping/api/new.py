import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_players.csv')
data.to_csv('data.csv', index=False)

print(data.head(2))

