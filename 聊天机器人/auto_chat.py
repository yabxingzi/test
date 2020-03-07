import requests, json, time, random

feature_text = '''
大家好！我是你的聊天机器人吴小枫。
>'''
    # user1 = input(feature_text)
while True:
    user1 = input('>')
    time.sleep(1)
    userid = str(random.randint(1, 1000000000000000000000))
    apikey = 'd81c0b99c260440980a140440be200ec'
    tulingdata1 = json.dumps({
        "perception": {
            "inputText": {
                "text": user1
            },

        },
        "userInfo": {
            "apiKey": apikey,
            "userId": userid
        }
    })
    robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
    jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
    print(jsrobot1)
