import hashlib
import FEAccount
import pandas
import requests
import random
import time
global listn
listn = []
cyname = []
jieshi = []
#<<Nezha>> & <<JiangZiya>>,The Power of Chinese Animated film.
#For memory of <<Nezha>> with Nezha and AoBing , <<JiangZiya>> with JiangZiya,ShenGongbao,XiaoJiu and SiBuxiang
#Designed By Wenjiachen, Github@Wenjia03
key = '847255f34a0a4914bd887b488e6ad1b5'
def waitwrite():
    listlen = len(listn)
    j = 0
    while j < listlen :
        now = listn[j]
        cyname.append(now[0])
        print('预读取' + cyname[j] + '成功')
        j = j + 1


print('Designed By WenjiaChen in LenShuijiang No.6 High School')
i = 0
df = pandas.read_csv('cyjs.csv',encoding ='gbk')
listn = df.values.tolist()
listlen = len(listn)
print('ok')
waitwrite()
while i < listlen :
    jup = False
    print('正在进行第' + str(i + 1) + '项，共计' +str(listlen)+'项')
    nowlist = listn[i]
    postmes = {'key' : key,'keyword':nowlist[0]}
    rre = requests.post('http://api.avatardata.cn/ChengYu/Search',params = postmes)
    rep = rre.json()
    #print(rep)
    try:
        resultbase = rep['result'][0]
    except:
        print('未找到该成语')
        jieshi.append('None')
        jup = True
    if jup == False:
        if len(resultbase['id']) != 0:
            id = resultbase['id']
            print('已找到成语ID，ID:' + id)
            postmes = {'key' : key,'id':id}
            rree = requests.post('http://api.avatardata.cn/ChengYu/LookUp',params = postmes)
            repe = rree.json()
            repebase = repe['result']
            if len(repebase['content']) !=0:
                content = repebase['content']
                print(nowlist[0]+'解释为：'+content+'，已经保存至系统')
                jieshi.append(content)
            else:
                print('该成语查找释义失败')
                jieshi.append('None')
        else:
            print('无该成语结果')
            jieshi.append('None')
    
    i = i + 1

print('开始写入文件……')
print(str(len(cyname))+','+str(len(jieshi)))
dataframe = pandas.DataFrame({'成语':cyname,'释义':jieshi})

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("result.csv",index=False,sep=',',encoding ='gbk')
