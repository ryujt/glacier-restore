# AWS S3 Glacier Restore Utility

Utility script to restore files on AWS S3 that have the GLACIER storage class.

## Installation

### Prerequisites

- Python (3.6 or newer is recommended)
- pip (Python package installer)

### Steps

1. Install the required `boto3` library using pip:

```
pip install boto3
```

2. Download or clone the `glacier-restore.py` script from the repository to your local machine.

## Usage

To use the `glacier-restore.py` script, navigate to the directory where you saved the script and execute the following command:

```
python3 glacier-restore.py --bucket YOUR_BUCKET_NAME --prefix YOUR_PREFIX --days=NUMBER_OF_DAYS
```

Replace `YOUR_BUCKET_NAME` with the name of your S3 bucket, `YOUR_PREFIX` with the prefix (or folder) from which you want to start the restoration, and `NUMBER_OF_DAYS` with the number of days you want to keep the restored files (default is 1 day if not specified).

For example:

```
python3 glacier-restore.py --bucket ryujt --prefix backup/music --days=7
```

## Troubleshooting

If the script terminates immediately or doesn't seem to be working as expected:

1. Ensure that the AWS credentials are correctly set up. The script uses the same authentication and endpoint configuration as the AWS CLI.
2. Double-check the bucket name and prefix for typos or errors.
3. Add print statements or logs in the script to trace its execution and pinpoint any issues.
