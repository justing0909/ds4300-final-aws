def upload_json_to_s3(s3_client, json_data, bucket_name, object_name):
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=json_data,
            ContentType='application/json'
        )
        print(f"Successfully uploaded {object_name} to S3 bucket {bucket_name}")
    except Exception as e:
        print(f"Error uploading to S3: {str(e)}")


def create_json_file(data):
    import json
    return json.dumps(data)


def get_s3_client(aws_credentials):
    return boto3.client(
        "s3",
        aws_access_key_id=aws_credentials["aws_access_key_id"],
        aws_secret_access_key=aws_credentials["aws_secret_access_key"],
        region_name=aws_credentials["aws_region"],
    )