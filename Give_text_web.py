import requests
import re

result = requests.get('http://www.ipap.ru')
text=result.text
phones = re.findall(r'\b\d\d\d\d\d\d\d\b|\b\d\d\d\d\d\d\d\d\d\d\d\b',text) # подобрать нужное \d поможет сайт https://nadejnei.net
                                                                        # https://regex101.com/
print(phones)

emails = re.findall(r'\w+@\w+.\w+', text)               # поиск почты W+ (одна и более букв) + @ \  W+ (одна и более букв) потом (точка . ) потом W+ (одна и более букв)
print(emails)