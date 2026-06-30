"""
Client functions for interacting with the CiviWeb Offers API.
"""

import requests

def get_jobs_count(api_url: str, headers: dict[str, str]) -> int:
    r = requests.post(api_url, json={'limit': 0}, headers=headers)
    r.raise_for_status()
    return r.json().get('count')

def fetch_all_jobs(api_url: str, headers: dict[str, str], limit=1000) -> tuple[list[dict], int]:
    # Get the overall jobs count for the loop
    jobs_count = get_jobs_count(api_url, headers)

    all_jobs = []
    skip = 0

    while (skip < jobs_count): # an error can be raised here, need to handle that
        body = {"limit": limit, "skip": skip, "sort": ["0"]}
        
        r = requests.post(api_url, json=body, headers=headers)

        if r.status_code == 200:
            all_jobs.extend(r.json().get("result")) # all_jobs and r are both lists, extend() merges them together
        else:
            print(f'Error {r.status_code} at skip={skip}.')
            break
        skip += limit

    return all_jobs, jobs_count