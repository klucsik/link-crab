from session_manager import make_session
from url_gatherer import get_all_website_links
from exercise_url import exercise_url
from reporting import save_linkdb_to_csv
from urllib.request import urlparse
import colorama

# Colorama init https://pypi.org/project/colorama/
colorama.init()
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET


#for development tests
from tests.test_app import generate_mock_app
generate_mock_app()

# setup:
print('----------------setup---------------------')

session = make_session()
starting_url = 'http://127.0.0.1:5000'
total_urls_visited = 0
checked_domain = urlparse(starting_url).netloc
links = set()
crawled_links= set()
link_db = []

# gathering:
print('----------------gather links---------------------')

def crawl(url):
    print (f'currently checked page: {url}')
    global crawled_links
    global links
    global total_urls_visited

    parsed = urlparse(url)
    if not (parsed.netloc == checked_domain):
        print(f'    skip: out of domain: {parsed.netloc}')
        return
        
    if  url in crawled_links :
        print(f'    skip: already visited: {url}')
        return
    
    total_urls_visited += 1
    links = get_all_website_links(session, url, links)
    crawled_links.add(url)
    links_to_crawl= links-crawled_links
    links_to_crawl.discard(url) #FIXME: There is a lot of duplicants in links_to_crawl
    for link in links_to_crawl:
        crawl(link)

crawl(starting_url)


# excresizing:
print('----------------Excercise links---------------------')

for link in links:
    link_db.append(exercise_url(session, link)) #TODO: error handling


# reporting:
print('----------------Report---------------------')

for link in link_db:
    print(f"[*] {link[0]} - {GREEN if link[1]==200 else RED} {link[1]} {RESET}- {link[2]} s")

save_linkdb_to_csv(link_db)


