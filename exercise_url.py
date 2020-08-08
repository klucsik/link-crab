import requests
from urllib.request import urljoin, urlparse


def exercise_url(session, url):
    if not check_url_validity(url):
        print(f"invalid link: {url}")
        return False
    resp = session.get(url)
    accessible = resp.ok and resp.url == url
    if not accessible:
        print(f"    not accessible: statuscode: {resp.status_code}, url: {resp.url}")
    print(f"[*] link: {url} - {resp.status_code} - {resp.elapsed.total_seconds()*1000} ms - accessible: {accessible}")
    outcome=[url,resp.status_code, int(resp.elapsed.total_seconds()*1000), accessible]
    return outcome


def check_url_validity(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


