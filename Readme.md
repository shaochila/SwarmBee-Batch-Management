# Swarm bee 节点批量管理

## <font color=#FF0000>被管理的节点机器需要打开debugapi端口（默认是1635） </font>

## 功能：

* 批量查看peer数
* 批量cashout-all
* 批量查看支票地址chequebook
* 批量查询所有余额

## 使用方法

使用python2运行nodes.py，按照提示输入

```python2
chmod +x nodes.py
python nodes.py
```

nodes.json文件中按照顺序依次填写IP端口

```json
[
    {
        "ip":"这里填ip","port":"这里填端口"
    },
    {
        "ip":"ip","port":"port"
    }
    
]
```

