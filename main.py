from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

job_names = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')
for job in job_names:
    time_posted=job.find('span',class_ ='sim-posted').text.strip()
    if'few' in time_posted:
        company_name = job.find('h3', class_ ='joblist-comp-name').text.strip()
        skills= job.find('span', class_ = 'srp-skills').text.strip()
        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        Age: {time_posted}
        ''')
        print('')