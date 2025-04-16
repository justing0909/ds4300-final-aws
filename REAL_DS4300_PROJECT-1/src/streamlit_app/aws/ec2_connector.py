import os
import boto3

def create_ec2_client():
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_REGION", "us-east-1")

    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )
    return ec2_client

def get_instance_status(instance_id):
    ec2_client = create_ec2_client()
    response = ec2_client.describe_instance_status(InstanceIds=[instance_id])
    return response['InstanceStatuses'] if 'InstanceStatuses' in response else None

def start_instance(instance_id):
    ec2_client = create_ec2_client()
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    return response

def stop_instance(instance_id):
    ec2_client = create_ec2_client()
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    return response

def terminate_instance(instance_id):
    ec2_client = create_ec2_client()
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    return response