import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

get_url = requests.get(url)

soup = BeautifulSoup(get_url.text,'lxml')

# print(soup.prettify())
print(soup.title)

#d =soup.find_all('div',class_="css-1j836f9 esl82me3")
print(soup.find('div', attrs={'class': 'balancedHeadline'}))
#print(d.text)
