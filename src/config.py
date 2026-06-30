"""
Centralized configuration loaded from environment variables.
"""

from dotenv import load_dotenv
import os

load_dotenv()

# API config
API_URL = os.environ['API_URL']
HEADERS = {"Content-Type": "application/json"}
PAGE_LIMIT = 1000

# S3 Bucket config
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_BUCKET_KEY = os.environ['S3_BUCKET_KEY']