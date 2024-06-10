import requests
import pandas as pd
from bs4 import BeautifulSoup

Match_records = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/match-schedule-fixtures-and-results"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}

response = requests.get(Match_records, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

matches = soup.find_all('div',class_="ds-text-compact-xxs")
teams = soup.find_all('div',class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
match_classes = soup.find_all('span', class_="ds-text-tight-s ds-font-medium ds-text-typo")
summary = soup.find_all('p',class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
scores = soup.find_all('div',class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap")
match_overview = soup.find_all('span', class_='ds-text-compact-xs ds-mr-0.5')
match_results = soup.find_all('p', class_="ds-text-tight-s ds-font-medium ds-line-clamp-2 ds-text-typo")

teams_country = []
match_class = []
scores_match = []
match_result = []

for ms in summary:
        teams_country.append(ms.text)
       
for match_cls in match_classes:
        match_class.append(match_cls.text)
        
for score in scores:
    scores_match.append(score.text)
    print(score.text)
    
for result in match_results:
    match_result.append(result.text)
    
df = pd.DataFrame()
df['Summary'] = [match for i, match in enumerate(match_class)]
df['Team1'] = [team for i, team in enumerate(teams_country) if i % 2 == 0]
#df['score'] = [score for i, score in enumerate(scores_match) if i % 2 == 0 and i>19]
df['Team2'] = [team for i, team in enumerate(teams_country) if i % 2 != 0]
df['result'] = [result for i, result in enumerate(match_result)]
df['matcchId'] = [i for i in range(1298135,1298180)]
df['matcchId'] = df['matcchId'].astype(str)
def remove_char(text, char,rreplace):
    return text.replace(char, rreplace)


df['matchLink'] = df['Summary'].apply(lambda x: remove_char(x, "(D/N)",""))
df['matchLink'] = df['matchLink'].apply(lambda x: remove_char(x, "(N)",""))
df['matchLink'] = df['matchLink'].apply(lambda x: remove_char(x, ",",""))

df['match_link'] = df['Team1']+'-'+'vs'+'-'+df['Team2']+'-'+df['matchLink']
df['match_link'] = df['match_link'].apply(lambda x: remove_char(x, " ","-"))
df['match_link'] = df['match_link'].str[:-1]
df['match_link']  = df['match_link']+df['matcchId']
df.drop(columns=['matchLink'])

scorecard = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/ireland-vs-zimbabwe-4th-match-first-round-group-b-1298138/full-scorecard"

response = requests.get(scorecard, headers=headers)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')
batsmen = soup.find_all('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center')
bowler = soup.find_all('td',class_='ds-flex ds-items-center')
wickets = soup.find_all('span',class_='ds-flex ds-items-center ds-cursor-pointer ds-justify-end ds-relative ds-text-typo ds-left-[15px]')
out_notout = soup.find_all('td',class_='ds-min-w-max !ds-pl-[100px]')
#scored = soup.fina_all('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right ds-text-typo')
balls_faced = soup.find_all('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right')
trr = soup.find_all('tr')[0]
#for bat in batsmen:
#    print(bat.text)
for bat in wickets:
    print(bat.text)
#for o_n in out_notout:
#    print(o_n.text)
for index, ball in enumerate(balls_faced):
    print(index, ball.text)
    



        
#for i in range(len(df['match_link'])):
#    print(df['match_link'][i])
    