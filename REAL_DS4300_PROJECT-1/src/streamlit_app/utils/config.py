import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
EC2_INSTANCE_ID = os.getenv("EC2_INSTANCE_ID")
LAMBDA_FUNCTION_NAME = os.getenv("LAMBDA_FUNCTION_NAME")
S3_BUCKET_PROCESSED = "ds4300-final-guthrie-processed"