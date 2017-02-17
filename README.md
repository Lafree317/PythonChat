最近发现一个Python的微信轮子,于是随后搞出了个玩具..
从来没学过Python,一边谷歌一遍写出来的...求轻喷

现在的功能有:
- 群里有人@你 自动回复
- 朋友私聊 自动回复
<!-- more -->
## 截图
- 两个小冰之间的pk:
![](https://dn-mhke0kuv.qbox.me/795b7a1707bbb7781188.PNG)
![](https://dn-mhke0kuv.qbox.me/ee64d1ca70e56b6722d5.PNG)
- 辣鸡智能毁我婚姻...:
![](https://dn-mhke0kuv.qbox.me/43f062e9460bb3ffd507.PNG)

## Code

### 安装库
自行安装Python3
下载轮子 - [Python微信接口库](http://itchat.readthedocs.io/zh/latest/)
按照文档安装可能会有些问题使用这个:
`sudo pip3 install itchat`

### 接入小冰
![](https://dn-mhke0kuv.qbox.me/0075ab040d63edd335f9)本来是用图灵机器人来回复的,而且有Api调用起来很方便,但是图灵机器人太傻了...就选择了微软小冰..
[微软小冰地址](http://www.msxiaoice.com/)
之后关注小冰的微信公众号
因为小冰没有Api所以回复流程大概是:
1.A发给我
2.我转发给小冰 
3.小冰回复了我 
4.我转发给A 

### 一些经验
```
@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE], isGroupChat = True)
def group_reply(msg):
```
上面这个方法
`itchat.content.TEXT`代表接收文本,`itchat.content.PICTURE]`代表接收图片,`itchat.content`还有很多类型不写代表不接收
后面的`isGroupChat = True`代表接收群消息,如果写成`isMpChat = True`就代表接收公众号消息,小冰的回复属于公众号消息所以用下面代码接收
```
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
```

我设置了一个全局变量`userId`用来记录每次要回复的人,每次使用的时候调用一下`global userId` 来取到它,这么设计肯定会有Bug但是我还没遇到,求大神改成闭包或异步...

```
# 搜索群聊
itchat.search_chatrooms(userName=fromUserName)
# 搜索好友
itchat.search_friends(userName=fromUserName)
# 搜索公众号
itchat.search_mps(name='小冰')[0]
```

剩下的去看文档吧,写的挺详细的
http://itchat.readthedocs.io/zh/latest/
![](https://dn-mhke0kuv.qbox.me/5b75c8436c9bdc24205e)
玩的开心😁
