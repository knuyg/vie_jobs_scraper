import requests

def main():

    api_url = 'https://civiweb-api-prd.azurewebsites.net/api/Offers/search'
    headers = {'Content-Type': 'application/json'}
    
    # I need to make a first API call to the count attribute, that will be used in the loop
    r = requests.post(api_url, json={'limit': 0}, headers=headers)
    
    if r.status_code != 200:
        print(f'Error {r.status_code}!')
        return
    
    else:
        jobs_count = r.json().get('count')

        all_jobs = []
        skip = 0
        limit = 1000

        while (skip < jobs_count): # an error can be raised here, need to handle that
            body = {
                "limit": limit,
                "skip": skip,
                "sort": ["0"]
            }
            
            r = requests.post(api_url, json=body, headers=headers)

            if r.status_code == 200:
                all_jobs.extend(r.json().get("result")) # Since result is already a list, I use the extend() method here instead of append()
            else:
                print(f'Error {r.status_code} at skip={skip}.')
                break
            skip += limit
        
        print(f'Fetched {len(all_jobs)} jobs out of {jobs_count}.')

if __name__ == '__main__':
    main()
