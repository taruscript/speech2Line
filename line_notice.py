import requests
import dotenv_loader


def sendToLine(notification_message):
    line_notify_token = dotenv_loader.token
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    text = "test"
    sendToLine(text)