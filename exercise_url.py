import requests
from urllib.request import urljoin, urlparse


def exercise_url(session, url):
    if not check_url_validity(url):
        print(f"invalid link: {url}")
        return False
    resp = session.get(url)
    print(f"[*] link: {url} - {resp.status_code} - {resp.elapsed.total_seconds()} s")
    outcome=[url,resp.status_code, resp.elapsed.total_seconds()]
    return outcome


def check_url_validity(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


