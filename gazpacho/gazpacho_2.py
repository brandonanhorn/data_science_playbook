from gazpacho import get, Soup


url = "https://www.baseball-reference.com/players/a"
html = get(url)
soup = Soup(html)

name = soup.find("div", {"id": "div_players_"}).text
name
names = soup.find("a", {"href": "/players/a"})
names
