from session_manager import make_session
from url_gatherer import get_all_website_links

from tests.test_app import generate_mock_app
generate_mock_app()

session = make_session()
starting_url = 'http://127.0.0.1:5000'
total_urls_visited = 0

links = set()
crawled_links= set()
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
    print(f"[*] {link}")