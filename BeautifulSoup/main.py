from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')

jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
#print(jobs)

for job in (jobs):
    heading=job.find('h3',class_='joblist-comp-name').text
    experience=job.find('ul',class_='top-jd-dtl clearfix').li.text
    location=job.find('ul',class_='top-jd-dtl clearfix').span.text
    key_skills=job.find('span',class_="srp-skills").text.replace("  ",'')
    more_info=job.h2.a["href"]

  # <-- for printing in terminal -->

    print(f'COMPANY NAME: {heading.strip()}')
    print(f'LOCATION: {location}')
    print(f'EXP.YEAR : {experience[-6:].strip()}')
    print(f'KeySkills: {key_skills.strip()}')
    print(more_info)

    print()



