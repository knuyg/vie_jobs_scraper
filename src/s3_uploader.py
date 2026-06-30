import json

def upload_jobs_to_s3(s3_client, bucket_name: str, bucket_key: str, jobs: list[dict]) -> None:
    s3_client.put_object(
        Bucket=bucket_name,
        Key=bucket_key,
        Body=json.dumps(jobs),
        ContentType="application/json",
    )