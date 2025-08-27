import boto3
from botocore.exceptions import NoCredentialsError
import os

BUCKET_NAME = "secure-file-portal-yourname"

s3 = boto3.client("s3")

def upload_file(file_name):
    try:
        s3.upload_file(file_name, BUCKET_NAME, os.path.basename(file_name))
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET_NAME, "Key": os.path.basename(file_name)},
            ExpiresIn=3600
        )
        print("✅ File uploaded successfully!")
        print("🔗 Shareable link:", url)
    except FileNotFoundError:
        print("❌ File not found")
    except NoCredentialsError:
        print("❌ AWS credentials not available")

if __name__ == "__main__":
    file_path = input("Enter file path to upload: ")
    upload_file(file_path)