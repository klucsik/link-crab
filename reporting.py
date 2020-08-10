from datetime import datetime

import os
delimiter=','

def save_linkdb_to_csv(link_db, domain_name):
    if not os.path.exists(f'reports/{domain_name}'):
        os.makedirs(f'reports/{domain_name}')
    with open(f"reports/{domain_name}/{domain_name}_{datetime.now()}_excersized_links.csv", "w") as f:
        print(f"url{delimiter}status_code{delimiter}response_time(ms){delimiter}accessible?", file=f)
        for link in link_db:
            print(f"{link[0]}{delimiter}{link[1]}{delimiter}{link[2]}{delimiter}{link[3]}", file=f)

def save_links(links, domain_name):
    if not os.path.exists(f'reports/{domain_name}'):
        os.makedirs(f'reports/{domain_name}')
    with open(f"reports/{domain_name}/{domain_name}_links.txt", "w") as f:
        for link in links:
            print(f"{link}", file=f)