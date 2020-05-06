import requests
import json
from  bs4 import BeautifulSoup

main_url = "https://www.accupass.com"
url = "https://www.accupass.com/?area=center"
d = {'area': 'center'}
headers = {'referer': 'www.accupass.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
r = requests.post(url, data=json.dumps(d), headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
print(r)
