'This script creates an S3 bucket using the Boto3 library'
import sys
import boto3

def main():
    'Main function executed to create the bucket'
    create_s3bucket(bucket_name)

def create_s3bucket(bucket_name):
    'This function sets up S3 bucket creation with the name, location, and ACL'
    s3_bucket = boto3.client(
        's3',
    )

    s3_bucket.create_bucket()(
        Bucket = bucket_name,
        CreateBucketConfiguration = {
            'LocationConstraint': 'us-west-1'
        },
        ACL = 'private'
    )

bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()
