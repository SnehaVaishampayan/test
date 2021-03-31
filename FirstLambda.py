
import json
def lambda_handler(event, context):
    message = 'Hello from local eclipse'
    a = {
        'statusCode': 200,
        'body': json.dumps({'input': message})
        }
    print(a)
    return {
        'statusCode': 200,
        'body': json.dumps({'input': message})
    }