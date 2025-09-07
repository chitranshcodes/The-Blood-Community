import requests
from bs4 import BeautifulSoup
import json

url="https://sbtcup.org/LicencedBloodCenter.aspx/Web/WebDoc/Web/WebDoc/SBTC_NBTC_Guideline/BloodBank.aspx"
response= requests.get(url)
data=[]
if response.status_code==200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table=soup.find("table")
    for tr in table.find_all("tr")[1:]:
        col=[td.text.strip() for td in tr.find_all("td")]
        if col:
            entry={
                "district":col[1],
                "name":col[2],
                "type":col[3],
                "contact":col[4],
                "number":col[5],
            }
            data.append(entry)
    

with open("blood_bank.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)