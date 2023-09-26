import requests
from bs4 import BeautifulSoup
import math

filtered_job_links = []
external_link_comp = []

def input_to_scrape(argument):
    match argument:
        case 1:
            # This is the request we are making for available software engineering positions in the United States 
            # that have been posted for the past 24 hours.
            
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
            target_url = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineering%20Intern&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&f_E=1&position=1&pageNum=0"
            res = requests.get(target_url)
            soup = BeautifulSoup(res.text, 'html.parser')   
            
            # Here, we create the query to scrape our links 

            job_count = soup.find(class_="results-context-header__job-count")
            iterator_query = (int(job_count.text))
            if iterator_query == 0:
                return "There are no available jobs for today."
            job_cards = soup.find_all('div', class_='base-card')
            for card in job_cards:
                if card['data-column'] == '1' and card['data-row'] == '1':
                    initial_job_id = ''.join(filter(str.isdigit, card['data-entity-urn'])) # Allows us to grab first job ID            

            # Now we have to target a new URL, and add these listings to our initialized array

            target_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Software%20Engineering%20Intern&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&f_E=1&currentJobId=" + initial_job_id + "&start={}"
            for i in range(0, math.ceil(iterator_query/25)):
                res = requests.get(target_url.format(i))
                soup = BeautifulSoup(res.text, 'html.parser')
                alljobs_on_this_page = soup.find_all("li")

            # Here we filter our jobs to ensure we obtain only software engineering roles. No filter would likely
            # give the user "excess" roles not related to software.
           
            for job in alljobs_on_this_page:
                job_title = job.find('h3', class_='base-search-card__title')
                if job_title:
                    job_title_text = job_title.text.lower()  # Convert to lowercase for case-insensitive matching
                    if 'software' in job_title_text and 'intern' in job_title_text:
                        job_link = job.find('a', class_='base-card__full-link')['href']
                        filtered_job_links.append(job_link)

                if len(filtered_job_links) >= 10:  # Stop after collecting 10 links
                    break
            
            # We scrape the modal for the external links and place them in our array

            for link in filtered_job_links:
                target_url = link
                res = requests.get(target_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                external_link = soup.find(class_="sign-up-modal__direct-apply-on-company-site")
                external_link_comp.append(external_link)

            #   We can now print the external links!

            for div_element in external_link_comp:
                if div_element is not None:
                    link = div_element.find('a', class_='sign-up-modal__company_webiste')
                    if link is not None:
                        print(link['href'],"\n")
        
        case 2:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
            target_url = "https://www.linkedin.com/jobs/search?keywords=IT%20Intern&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&f_E=1&position=1&pageNum=0"
            res = requests.get(target_url)
            soup = BeautifulSoup(res.text, 'html.parser') 

            job_count = soup.find(class_="results-context-header__job-count")
            iterator_query = (int(job_count.text))
            if iterator_query == 0:
                return "There are no available jobs for today."
            job_cards = soup.find_all('div', class_='base-card')
            for card in job_cards:
                if card['data-column'] == '1' and card['data-row'] == '1':
                    initial_job_id = ''.join(filter(str.isdigit, card['data-entity-urn']))

            target_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=IT%20Intern&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&f_E=1&currentJobId=" + initial_job_id + "&start={}"
            for i in range(0, math.ceil(iterator_query/25)):
                res = requests.get(target_url.format(i))
                soup = BeautifulSoup(res.text, 'html.parser')
                alljobs_on_this_page = soup.find_all("li")

            for job in alljobs_on_this_page:
                job_title = job.find('h3', class_='base-search-card__title')
                if job_title:
                    job_title_text = job_title.text.lower()  # Convert to lowercase for case-insensitive matching
                    if 'it' or 'information technology' in job_title_text and 'intern' in job_title_text:
                        job_link = job.find('a', class_='base-card__full-link')['href']
                        filtered_job_links.append(job_link)

                if len(filtered_job_links) >= 10:  # Stop after collecting 10 links
                    break            

            for link in filtered_job_links:
                target_url = link
                res = requests.get(target_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                external_link = soup.find(class_="sign-up-modal__direct-apply-on-company-site")
                external_link_comp.append(external_link)

            for div_element in external_link_comp:
                if div_element is not None:
                    link = div_element.find('a', class_='sign-up-modal__company_webiste')
                    if link is not None:
                        print(link['href'],"\n")

        case 3:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
            target_url = "https://www.linkedin.com/jobs/search?keywords=Product%20Management%20Intern&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&f_E=1&position=1&pageNum=0"
            res = requests.get(target_url)
            soup = BeautifulSoup(res.text, 'html.parser') 

            job_count = soup.find(class_="results-context-header__job-count")
            iterator_query = (int(job_count.text))
            if iterator_query == 0:
                return "There are no available jobs for today."
            job_cards = soup.find_all('div', class_='base-card')
            for card in job_cards:
                if card['data-column'] == '1' and card['data-row'] == '1':
                    initial_job_id = ''.join(filter(str.isdigit, card['data-entity-urn']))

            target_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Product%20Management%20Intern&location=United%20States&locationId=&geoId=103644278&f_TPR=r86400&f_E=1&currentJobId=" + initial_job_id + "&start={}"
            for i in range(0, math.ceil(iterator_query/25)):
                res = requests.get(target_url.format(i))
                soup = BeautifulSoup(res.text, 'html.parser')
                alljobs_on_this_page = soup.find_all("li")

            for job in alljobs_on_this_page:
                job_title = job.find('h3', class_='base-search-card__title')
                if job_title:
                    job_title_text = job_title.text.lower()  # Convert to lowercase for case-insensitive matching
                    if 'product management' in job_title_text and 'intern' in job_title_text:
                        job_link = job.find('a', class_='base-card__full-link')['href']
                        filtered_job_links.append(job_link)

                if len(filtered_job_links) >= 10:  # Stop after collecting 10 links
                    break            

            for link in filtered_job_links:
                target_url = link
                res = requests.get(target_url)
                soup = BeautifulSoup(res.text, 'html.parser')
                external_link = soup.find(class_="sign-up-modal__direct-apply-on-company-site")
                external_link_comp.append(external_link)

            for div_element in external_link_comp:
                if div_element is not None:
                    link = div_element.find('a', class_='sign-up-modal__company_webiste')
                    if link is not None:
                        print(link['href'],"\n")         
        case _:
            return "Not a valid command!"

terminal_input = input("Welcome to this CS internship scraper! This tool returns the top 10 LinkedIn application"
+ " links for the niche in CS you're looking for. Enter the number corresponding to your desired query." + 
" Here are your options:\n1. Software Engineering\n2. IT\n3. Product Management\n")

result = input_to_scrape(int(terminal_input))
