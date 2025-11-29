import requests

def send_slack_notification(message, webhook_url=os.environ.get('SLACK_WEBHOOK')):
    if webhook_url:
        payload = {'text': message}
        requests.post(webhook_url, json=payload)
    print(f"Slack: {message}")  # Fallback