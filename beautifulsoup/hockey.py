from gazpacho import Soup, get
import pandas as pd

html = get('https://www.hockey-reference.com/leagues/NHL_2020_games.html')
soup = Soup(html)
table = soup.find('table', {'id': "games"})
df = pd.read_html(table.html)[0]
df = df.dropna(subset=['G'])
df.to_csv('nhl.csv')
