import boto3
import argparse

def check_restore_status(bucket_name, prefix):
    s3 = boto3.client('s3')

    paginator = s3.get_paginator('list_objects_v2')
    iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    for page in iterator:
        for obj in page.get('Contents', []):
            key = obj['Key']

            response = s3.head_object(Bucket=bucket_name, Key=key)
            restore_status = response.get('Restore')

            if restore_status:
                if 'ongoing-request="true"' in restore_status:
                    print(f"{key} is being restored.")
                elif 'ongoing-request="false"' in restore_status:
                    print(f"{key} is restored and available.")
            else:
                print(f"{key} is not being restored or not from Glacier.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check AWS S3 Glacier Restore Status")
    parser.add_argument("-b", "--bucket", required=True, help="S3 bucket name")
    parser.add_argument("-p", "--prefix", required=True, help="Prefix (folder) to check restore status")

    args = parser.parse_args()

    check_restore_status(args.bucket, args.prefix)
