import json
import uuid
import os
from datetime import datetime

import boto3

s3 = boto3.client("s3")
polly = boto3.client("polly")
dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ["TABLE_NAME"]
BUCKET_NAME = os.environ["BUCKET_NAME"]
VOICE_ID = os.environ.get("VOICE_ID", "Joanna")

table = dynamodb.Table(TABLE_NAME)

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Methods": "*"
}


def lambda_handler(event, context):

    print("Received Event:")
    print(json.dumps(event))

    try:

        body = json.loads(event["body"])

        file_name = body["fileName"]
        text = body["text"].strip()

        if not file_name.endswith(".txt"):
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({
                    "error": "Only .txt files are allowed."
                })
            }

        if len(text) == 0:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps({
                    "error": "Text file is empty."
                })
            }

        text_key = f"uploads/{file_name}"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=text_key,
            Body=text,
            ContentType="text/plain"
        )

        polly_response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=VOICE_ID
        )

        audio_stream = polly_response["AudioStream"].read()

        base_name = os.path.splitext(file_name)[0]
        audio_key = f"audio/{base_name}.mp3"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=audio_key,
            Body=audio_stream,
            ContentType="audio/mpeg"
        )

        item = {
            "id": str(uuid.uuid4()),
            "fileName": file_name,
            "text": text,
            "audioKey": audio_key,
            "uploadedAt": datetime.utcnow().isoformat(),
            "voice": VOICE_ID
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(item)
        }

    except Exception as e:

        print(str(e))

        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({
                "error": str(e)
            })
        }
