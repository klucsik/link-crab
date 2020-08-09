import requests
from bs4 import BeautifulSoup
from urllib.request import urljoin, urlparse


def get_all_website_links(session, url, links):
    """
    Returns URLs that is found on `url` in which belongs to the website
    """
    # all URLs of `url`
    


    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc

    try:
        soup = BeautifulSoup(session.get(url).content, "html.parser")

        for a_tag in soup.findAll():
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue

            href = urljoin(url, href)
            parsed_href = urlparse(href)

            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        
            if href in links:
                print(f"[ ] link already gathered: {href}")
            else:
                links.add(href)
                print(f"[+] link found: {href}")
    except:
        print("An exception occurred")
    return links