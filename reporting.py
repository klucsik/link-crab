
from urllib.request import urljoin, urlparse
from datetime import datetime
import os
delimiter=','

def save_linkdb_to_csv(link_db):
    parsed_first_url = urlparse(link_db[0][0])
    domain_name = parsed_first_url.netloc
    if not os.path.exists('reports'):
        os.makedirs('reports')
    with open(f"reports/{domain_name}_{datetime.now()}_excersized_links.csv", "w") as f:
        print(f"url{delimiter}status_code{delimiter}response_time(ms){delimiter}accessible?", file=f)
        for link in link_db:
            print(f"{link[0]}{delimiter}{link[1]}{delimiter}{link[2]}{delimiter}{link[3]}", file=f)