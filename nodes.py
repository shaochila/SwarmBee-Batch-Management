# -*- coding: utf-8 -*
import os
import json

with open('nodes.json') as file:
    nodes_json = file.read()

nodes = json.loads(nodes_json)

def peer():
    for node in nodes:
        ipport = node['ip']+':'+node['port']
        #sh = './peer.sh'+ ' '+ ipport
        sh = "curl -s http://"+ ipport + "/peers  | jq '.peers | length'"
        print ipport
        os.system(sh)

def cashout_all():
    for node in nodes:
        ipport = node['ip']+':'+node['port']
        sh = './cashout.sh'+' ' + 'cashout-all' + ' '+ ipport
        log = 'echo'+' '+'`date +"%Y-%m-%d %H:%M:%S"`' + ' '+'cashout-all'+' 2021 GET RICH  '+ ipport + '>>' + ' ' + 'cashout.log'
        os.system(log)
        print sh
        os.system(sh)

def chequebook():
    print 'goerli以太坊浏览器：https://goerli.etherscan.io/address/'
    for node in nodes:
        ipport = node['ip']+':'+node['port']
        sh = "curl -s "+ipport+ "/chequebook/address | jq '. | .chequebookaddress'"
        print ipport
        os.system(sh)

def balance():
    for node in nodes:
        ipport = node['ip']+':'+node['port']
        print ipport
        sh = "curl -s"  +"  "+ipport +"/chequebook/balance | jq '. | .totalBalance*0.0000000000000001'"
        os.system(sh)
    
print '把所有ip和端口填入nodes.json文件中'
print '1：所有的peer数'
print '2：cashout-all全部'
print '3：输出所有chequebookaddress'
print '4: 输出所有gbzz余额'
innn = input('选择功能\n')

if innn == 1:
    peer()
elif innn == 2:
    cashout_all()
elif innn == 3:
    chequebook()
elif innn == 4:
    balance()
else:
    print '错了'
