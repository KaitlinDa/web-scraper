import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    citations_needed = soup.find_all('span', text='citation needed')
    
    return len(citations_needed)

def get_citations_needed_report(url):
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    citations_needed = soup.find_all('span', text='citation needed')
    
    report = ""
    
    for citation in citations_needed:
        parent_paragraph = citation.find_parent('p')
        if parent_paragraph:
            paragraph_text = parent_paragraph.text.strip()
            report += paragraph_text + "\n\n"
    
    return report.strip()

url = 'https://en.wikipedia.org/wiki/Video_game'
print(get_citations_needed_count(url))
print(get_citations_needed_report(url))
