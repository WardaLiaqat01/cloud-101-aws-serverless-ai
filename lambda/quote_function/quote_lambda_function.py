import json
import random

QUOTES = [
    "Cloud = freedom.",
    "Build more, manage less.",
    "Serverless means zero servers to think about.",
    "Ship early, iterate fast.",
    "Code + Cloud = Ship products."
]

def lambda_handler(event, context):
    # Support optional ?q=<text> to return a custom message
    params = event.get("queryStringParameters") or {}
    custom = params.get("q")
    if custom:
        message = custom
    else:
        message = random.choice(QUOTES)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"   # CORS for browser demos
        },
        "body": json.dumps({"message": message})
    }