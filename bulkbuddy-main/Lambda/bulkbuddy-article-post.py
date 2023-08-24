import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('team1_sns_test')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        # 必須パラメータのチェック
        if 'userId' not in body or 'name' not in body or 'text' not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'userId, name, and text are required fields'})
            }
        
        userId = body['userId']
        name = body['name']
        text = body['text']
        
        category = body.get('category', '')
        reply = body.get('reply', [])
        likepost = 0  # 固定
        
        timestamp = int(datetime.datetime.now().timestamp() * 1000)  # ミリ秒単位のタイムスタンプ
        
        # DynamoDBにデータを保存
        table.put_item(
            Item={
                'userId': userId,
                'likepost': likepost,
                'name': name,
                'text': text,
                'category': category,
                'reply': reply,
                'timestamp': timestamp
            }
        )
        
        # レスポンスを作成
        response = {
            'userId': userId,
            'name': name,
            'text': text,
            'category': category,
            'timestamp': str(timestamp)
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
