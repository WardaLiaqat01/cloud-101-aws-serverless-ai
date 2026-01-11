import json
import boto3

comprehend = boto3.client('comprehend')  # uses Lambda's role and region

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    text = params.get("text", "")
    if not text:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Provide ?text=your+sentence"})
        }

    try:
        # Detect dominant language first (Comprehend needs language code)
        lang_resp = comprehend.detect_dominant_language(Text=text)
        lang_code = lang_resp['Languages'][0]['LanguageCode'] if lang_resp.get('Languages') else 'en'

        # Detect sentiment
        resp = comprehend.detect_sentiment(Text=text, LanguageCode=lang_code)
        sentiment = resp.get('Sentiment')
        sentiment_score = resp.get('SentimentScore', {})

        body = {
            "text": text,
            "language": lang_code,
            "sentiment": sentiment,
            "scores": sentiment_score
        }
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps(body)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
