from bs4 import BeautifulSoup
import requests
import time

print(f"\nWelcome to this program. It will pick up some jobs from timesjobs.com which were posted recently and dont require a skillset that you dont have :-)\n")
print('It also refreshes  itself every 10 minutes(which is actually illogical). I am a dumb programmer. Please bear with me.\n')

print('Type some skill that you are not familiar with (eg.-django)')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text,'lxml')

    jobs = soup.find_all('li',class_= 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            # used replace to remove empty spaces

            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')

            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:

                with open(f'posts/{index}.txt','w') as f:
                    # print(f"Company Name:  {company_name.strip()}")
                    # print(f"Required skills: {skills.strip()}")
                    # print(f'More Info: {more_info}')
                    # print('') 

                    f.write(f"Company Name:  {company_name.strip()} \n")
                    f.write(f"Required skills: {skills.strip()} \n")
                    f.write(f'More Info: {more_info} \n')
                print(f'File Saved {index} !!')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_to_wait = 10
        print(f'Waiting for {time_to_wait} minutes...')
        time.sleep(time_to_wait * 60) #10 minutes