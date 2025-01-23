import requests

apiKey = '6935364D6B69734F596A695339625358356645392F33504A467638666167367144697A776F4433424651773D'
url = 'https://api.kavenegar.com/v1/%s/sms/send.json' %apiKey
params = {
    'receptor': '9309108322',
    'message': 'Hello World!',
    'sender': '2000660110'
}
respons = requests.post(url, data=params)
print(respons)
