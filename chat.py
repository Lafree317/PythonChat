import itchat

# 回复用userId
userId = ''

# 获取好友消息
@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE])
def text_reply(msg):
    # 让小冰回答
    global userId
    userId = msg['FromUserName']
    xbAnswer(msg)
    print(getUserNickName(msg) + "发来的消息:\n" + getText(msg))

# 群信息
@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE], isGroupChat = True)
def group_reply(msg):
    fromUserName = msg['FromUserName'];
    group = itchat.search_chatrooms(userName=fromUserName)
    print(group['NickName'] + "群的 " + msg['ActualNickName'] + " 发来的消息\n" + getText(msg) )

    if msg['isAt'] == True :
        global userId
        userId = msg['FromUserName']
        xbAnswer(msg)

# 群信息
@itchat.msg_register(itchat.content.PICTURE, isGroupChat = True)
def group_pic(msg):
    msg['Text'](msg['FileName'])
    itchat.send_image(msg['FileName'])

# 公众号消息
@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE], isMpChat = True)
def map_reply(msg):
    text = getText(msg)
    global userId
    if msg['Type'] == 'Picture':
        msg['Text'](msg['FileName'])
        itchat.send_image(msg['FileName'],userId)
        itchat.send_msg('上图为微软小冰回答', userId)
    else:
        itchat.send_msg(text + " 微软小冰的智能回复", userId)

# 获取昵称
def getUserNickName(msg):
    fromUserName = msg['FromUserName']
    fromUser = itchat.search_friends(userName=fromUserName)
    nickName = fromUser['NickName']
    return nickName

# 获取文字
def getText(msg):
    if msg['Type'] == 'Text':
        return msg['Text']
    else:
        return "发送的其他类型回复"

# 向智能小冰提问
def xbAnswer(msg):
    xb = itchat.search_mps(name='小冰')[0]
    quest = getText(msg)
    if msg['Type'] == 'Picture':
        msg['Text'](msg['FileName'])
        itchat.send_image(msg['FileName'],xb['UserName'])
    else:
        itchat.send_msg(quest, xb['UserName'])

itchat.auto_login()
itchat.run()