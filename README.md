# CmdHttpTool
Windows 命令行 GET/POST 请求工具，支持本地网址

## Prerequisite
```
# Python 3

pip install requests

# Cmder(建议)
```

## Quick Start
```
python api.py get "http://www.test.com/json" a=1&b=2
python api.py post http://www.test.com/json" "a=1&b=2"               # 支持url参数
python api.py post http://www.test.com/json" {"a":1, "b":2}        # 支持json格式

# 返回值

<Response [200]>

{
    "code":200,
    "data": [
         "hello":"world"
    ]
}
```

## Usage
```
python api.py [get/post] "[url]" "[json/url parameters]"             # URL与URL参数需使用双引号
```

## website
https://blog.csdn.net/panguangyuu/article/details/105518924
