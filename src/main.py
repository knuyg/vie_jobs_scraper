import requests
import boto3
import json
from dotenv import load_dotenv
import os

from api_client import fetch_all_jobs

def main():

    load_dotenv()
    API_URL = os.environ['API_URL']
    BUCKET_NAME = os.environ['S3_BUCKET_NAME']
    headers = {'Content-Type': 'application/json'}

    all_jobs, jobs_count = fetch_all_jobs(API_URL, headers)

    print(f'Fetched {len(all_jobs)} jobs out of {jobs_count}.')

if __name__ == '__main__':
    main()