import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv

url = "https://www.thehindu.com/"

try:
    header = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    all_news = soup.find('section',class_="top-section").find_all(['li','h3'])

    #print(all_news)
    unwanted_link = ['https://www.thehindu.com/hindi/editorial/']
    
    news_data=[]
    for news in all_news:
        link_tag = news.find('a')
        for span in link_tag.find_all(["span","i"]):
            span.decompose()
        if news.a:
            news_title = news.a.get_text(strip=True)
            news_link = news.a['href']

            if news_link in unwanted_link:
                continue

            news_data.append([news_title,news_link])
            
    print(tabulate(news_data, headers=["Headline", "Link"], tablefmt="fancy_grid"))

    

    with open("hindu_headlines.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline", "Link"]) 
        writer.writerows(news_data)


except Exception as e:
    print(e)