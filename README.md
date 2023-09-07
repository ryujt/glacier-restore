# AWS S3 Glacier Restore Utility

Utility scripts to manage and restore files on AWS S3 that have the GLACIER storage class.

## Installation

### Prerequisites

- Python (3.6 or newer is recommended)
- pip (Python package installer)

### Steps

1. Install the required `boto3` library using pip:

```
pip3 install boto3
```

2. Download or clone the `glacier-restore.py` and `restore-status.py` scripts from the repository to your local machine.

## Usage

### glacier-restore.py

To use the `glacier-restore.py` script, navigate to the directory where you saved the script and execute the following command:

```
python3 glacier-restore.py --bucket YOUR_BUCKET_NAME --prefix YOUR_PREFIX --days=NUMBER_OF_DAYS
```

Replace `YOUR_BUCKET_NAME` with the name of your S3 bucket, `YOUR_PREFIX` with the prefix (or folder) from which you want to start the restoration, and `NUMBER_OF_DAYS` with the number of days you want to keep the restored files (default is 1 day if not specified).

For example:

```
python3 glacier-restore.py --bucket ryujt --prefix backup/music --days=7
```

### restore-status.py

To check the restoration status of objects in an S3 bucket, use the `restore-status.py` script:

```
python3 restore-status.py --bucket YOUR_BUCKET_NAME --prefix YOUR_PREFIX
```

Replace `YOUR_BUCKET_NAME` with the name of your S3 bucket and `YOUR_PREFIX` with the prefix (or folder) for which you want to check the restoration status.

For example:

```
python3 restore-status.py --bucket ryujt --prefix backup/music
```

## Troubleshooting

If the scripts terminate immediately or don't seem to be working as expected:

1. Ensure that the AWS credentials are correctly set up. The scripts use the same authentication and endpoint configuration as the AWS CLI.
2. Double-check the bucket name and prefix for typos or errors.
3. Add print statements or logs in the scripts to trace their execution and pinpoint any issues.
