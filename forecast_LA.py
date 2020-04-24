import pandas as pd 
import requests 
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.099695000000054&lon=-118.33539999999999#.Xo7oOIgzZPY')
soup = BeautifulSoup(page.content , 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_ = 'tombstone-container')
period_names = [item.find(class_='period-name').get_text() for item in items]
descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_report = pd.DataFrame({
    'period' : period_names,
    'short_descriptions' : descriptions,
    'temperatures' : temperatures,
})
print(weather_report)

weather_report.to_csv('weather.csv')
# for item in items:
#     p_name = item.find(class_ = 'period-name').text
#     desc = item.find(class_ = 'short-desc').text
#     temp = item.find(class_ = 'temp').text

#     print(p_name, desc,temp ,'--\n')

