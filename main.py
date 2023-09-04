#coding:gbk

from fastapi import FastAPI, Request
import requests

BASEURL = 'http://127.0.0.1:5700'
# r = requests.get(url='http://127.0.0.1:5700/get_login_info')
# print(r.json())


def sendGroupMsg(gid: int, text: str):
    # print('进入sendGroupMsg')
    d = {'message': text,
         'group_id': gid}
    print(requests.post(f'{BASEURL}/send_group_msg', data=d))

def getMsg(id: int):
    d = {'message_id': id}
    return requests.post(f'{BASEURL}/get_msg', data=d)

app = FastAPI()

@app.post('/')
async def handle(request: Request):
    try:
        data = await request.json()
        # print('打印输出data：', data, '\n', '='*40)
        if data['post_type'] == 'meta_event':
            return 'a'
        msgid = data['message_id']
        # print('打印输出msgid=', msgid, '\n', '='*40)

        msg = getMsg(msgid).json()
        # print(msg)
        print(msg['data']['sender']['nickname'], (msg['data']['sender']['user_id']), '：', msg['data']['message'])
        msgtext = msg['data']['message']
        # print('打印输出msg=', msg, '\n', '='*40)
        if msgtext == '原神':
            # print('进入’原神‘if', '\n', '='*40)
            gid = msg['data']['group_id']
            # print(f'打印输出gid：{gid}', '\n', '='*40)
            sendGroupMsg(gid=gid, text='启动你麻痹')
        return 'ts'
    except Exception as ec:
        print(f'报错信息：{ec}')
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=5701, host='0.0.0.0')

