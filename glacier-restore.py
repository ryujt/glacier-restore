import boto3
import argparse
import time

def restore_from_glacier(bucket_name, prefix, days):
    s3 = boto3.client('s3')

    paginator = s3.get_paginator('list_objects_v2')
    iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    for page in iterator:
        for obj in page.get('Contents', []):
            key = obj['Key']

            response = s3.head_object(Bucket=bucket_name, Key=key)
            storage_class = response.get('StorageClass')

            if storage_class in ["GLACIER", "DEEP_ARCHIVE"]:
                try:
                    print(f"Restoring: {key}")
                    s3.restore_object(
                        Bucket=bucket_name,
                        Key=key,
                        RestoreRequest={
                            'Days': days,
                            'GlacierJobParameters': {
                                'Tier': 'Standard'
                            }
                        }
                    )
                    time.sleep(0.1)
                except boto3.exceptions.botocore.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == "RestoreAlreadyInProgress":
                        print(f"Restore already in progress for: {key}")
                    else:
                        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AWS S3 Glacier Restore Utility")
    parser.add_argument("-b", "--bucket", required=True, help="S3 bucket name")
    parser.add_argument("-p", "--prefix", required=True, help="Prefix (folder) to start restoration")
    parser.add_argument("-d", "--days", type=int, default=1, help="How many days to keep restored files. Default is 1 day.")

    args = parser.parse_args()

    restore_from_glacier(args.bucket, args.prefix, args.days)
