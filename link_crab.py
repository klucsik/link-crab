from session_manager import make_session
from url_gatherer import get_all_website_links
from exercise_url import exercise_url

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

session = make_session()
starting_url = 'http://127.0.0.1:5000'
total_urls_visited = 0

links = set()
crawled_links= set()
link_db = []

def crawl(url):

    global total_urls_visited
    total_urls_visited += 1
    global links
    links = get_all_website_links(session, url, links)
    crawled_links.add(url)
    links_to_crawl= links-crawled_links

    for link in links_to_crawl:
        crawl(link)

crawl(starting_url)

for link in links:
    link_db.append(exercise_url(session, link)) #TODO: error handling
print('--------------------------------')
for link in link_db:
    print(f"[*] {link[0]} - {GREEN if link[1]==200 else RED} {link[1]} {RESET}- {link[2]} s")