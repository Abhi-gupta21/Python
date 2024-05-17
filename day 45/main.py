from bs4 import BeautifulSoup
import requests


articletext = []
articlepoints = []
articlelinks = []
response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find_all(name='span', class_ = 'titleline')

for tag in title:
    articletext.append(tag.getText())



points = soup.find_all(name='span', class_='score')

articlepoints = [int(p.getText().split()[0]) for p in points]



links = soup.select(".titleline a")

for link in links:
    articlelinks.append(link.get("href"))


maxpointsindex = articlepoints.index(max(articlepoints))

print(maxpointsindex)

print(articlepoints[maxpointsindex])
print(articletext[maxpointsindex])
print(articlelinks[maxpointsindex])





