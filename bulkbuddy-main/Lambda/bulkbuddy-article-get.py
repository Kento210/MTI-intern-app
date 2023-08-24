import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('team1_sns_test')

def lambda_handler(event, context):
    try:
        # DynamoDBから最大100件のデータを取得
        response = table.scan(Limit=100)
        
        articles = []
        
        for item in response['Items']:
            article = {
                'userId': item['userId'],
                'name': item['name'],
                'text': item['text'],
                'category': item.get('category', 0),  # categoryがない場合は0を設定
                'reply': item.get('reply', []),  # replyがない場合は空配列を設定
                'likepost': item.get('likepost', 0)  # likepostがない場合は0を設定
            }
            articles.append(article)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'articles': articles})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

