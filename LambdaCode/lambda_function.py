import boto3
import json

s3 = boto3.client('s3')
def lambda_handler(event, context):
    response = s3.list_buckets()
    
    # Output the bucket names
    print('Existing buckets:')
    result=""
    for bucket in response['Buckets']:
        result=result+bucket["Name"]+"\n"
    #print(result)
        #print(f'  {bucket["Name"]}')
    return {"statusCode": 200, "body": json.dumps(result)}