import boto3
import sys

def upload_file_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    s3_client.upload_file(file_name, bucket, object_name)
    url = f"https://{bucket}.s3.amazonaws.com/{object_name}"
    return url

def main():
    if len(sys.argv) < 2:
        print("⚠ Usage: python upload_and_generate.py <file_name>")
        return

    file_name = sys.argv[1]   # take file name from command line
    bucket = "secure-file-portal-yourname"  # change this to your bucket name

    try:
        url = upload_file_to_s3(file_name, bucket)
        print(f"✅ File uploaded successfully!\nDownload Link: {url}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()