def invoke_lambda_function(lambda_client, function_name, payload):
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response['Payload'].read())
        return response_payload
    except Exception as e:
        print(f"Error invoking Lambda function: {str(e)}")
        return None