import boto3

from config import API_URL, HEADERS, PAGE_LIMIT, S3_BUCKET_NAME, S3_BUCKET_KEY
from api_client import fetch_all_jobs
from s3_uploader import upload_jobs_to_s3

def main() -> None:

    all_jobs, jobs_count = fetch_all_jobs(API_URL, HEADERS, PAGE_LIMIT)
    print(f'Fetched {len(all_jobs)} jobs out of {jobs_count}.')

    s3 = boto3.client("s3")
    upload_jobs_to_s3(s3, S3_BUCKET_NAME, S3_BUCKET_KEY, all_jobs)

if __name__ == '__main__':
    main()