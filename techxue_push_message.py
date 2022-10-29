import requests
import json
def get_message():
    url="http://172.18.107.64:16667/api/list_users_status_from_memory"
    url_get=requests.get(url)
    message_list=[]
    for i in json.loads(url_get.text)['data']:
        message_list.append(i['status'])
    return(message_list)    
# print(get_message())
class SendWeiXinWork():
    def __init__(self):
        self.CORP_ID = "ww5d5473e647d3021f"  # 企业号的标识
        self.SECRET = "sod3EQCUh6QB6vYnk_pIwsFF0RKAUSr2KG-gqvmIeMI"  # 管理组凭证密钥
        self.AGENT_ID = 1000002  # 应用ID
        self.token = self.get_token()
 
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {
            "corpid": self.CORP_ID,
            "corpsecret": self.SECRET
        }
        req = requests.get(url=url, params=data)
        res = req.json()
        if res["errmsg"] == "ok":
            return res["access_token"]
        else:
            return res
 
    def send_message(self, to_user, content):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % self.token
        data = {
            "touser": to_user,  # 发送个人就填用户账号
            # "toparty": to_user,  # 发送组内成员就填部门ID
            "msgtype": "text",
            "agentid": self.AGENT_ID,
            "text": {"content": content},
            "safe": "0"
        }
 
        req = requests.post(url=url, json=data)
        res = req.json()
        if res["errmsg"] == "ok":
            print("send message sucessed")
            return "send message sucessed"
        else:
            return res
 
 

SendWeiXinWork = SendWeiXinWork()
list_message=get_message()
str_message="\n\n".join(list_message)
SendWeiXinWork.send_message('@all', str_message)
# SendWeiXinWork.send_message("GaoXiangShang", str_message)
