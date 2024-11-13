import json
import boto3

client = boto3.client('bedrock-runtime')

def handler(event, context):

    body = json.loads(event.get('body', '{}'))
    #setting defult prompt if none provided
    prompt = body.get('prompt', 'Write a text to be posted on my social media channels about how Amazon Bedrock works')
    
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "temperature": 0.7,
        "messages": [
            {"role": "user", "content": prompt}
    ]
    }) #all parameters (except for prompt) are set to default values

    modelId = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
    accept = 'application/json'
    contentType = 'application/json'

    response = client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    return {
        'statusCode': 200,
        'body': json.dumps({
            'generated-text': response_body
        })
    }