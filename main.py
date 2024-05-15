from flask import Flask, request, jsonify 
import boto3
import json
import os
app = Flask(__name__)
server_token="notsecured"   # todo: change it to get from env
sqs_client = boto3.client("sqs",
    region_name="us-east-1",#os.environ.get('AWS_DEFAULT_REGION'),
    endpoint_url="http://localhost:4566",#os.environ.get('AWS_ENDPOINT'),
    aws_access_key_id="my_access_key", #os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key="my_secret_key")#os.environ.get('AWS_SECRET_ACCESS_KEY'))
queue_url = sqs_client.get_queue_url(
        QueueName="checkpoint-SQS",
    )["QueueUrl"]
@app.route('/api/add_message', methods=['POST'])
def add_message():
    content = request.json
    content_valid=validate_content(content)
    if(validate_content(content)!=""):
        return content_valid,400
    send_message_to_sqs(content)
    return "",200

def send_message_to_sqs(content):
    message = content
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )
    print(response)





def validate_content(content):
        try: 
            if not (isinstance(content["data"],dict)):
                return "there is no data in the request or it is not a valid json"
        except:
            return "there is no data in the request or it is not a valid json"
        try:
            if( not isinstance(content["data"]["email_subject"],str)):
                return "data: email_subject is not valid"
        except:
            return "return there is no email_subject under data"
        try:
            if( not isinstance(content["data"]["email_sender"],str)):
                return "data: email_sender is not valid"
        except:
            return "return there is no email_sender under data"
        try:
            if( not isinstance(content["data"]["email_content"],str)):
                return "data: email_s is not valid"
        except:
            return "return there is no email_content under data"
        try:
            if( not isinstance(content["data"]["email_timestream"],str)):
                return "data: email_timestream is not in json"
        except:
            return "return there is no email_timestream under data"
        
        try:
            if( not isinstance(content["token"],str)):
                return "the token is not a string"
            
            if(content["token"]!=server_token):
                return "token is not correct"             
        except:
            return "there is no token or it is not valid json"
        
        return ""
        

        

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)

    
    
   