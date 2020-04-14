# -*- coding:utf-8 -*-

import requests
import sys
import json

def sendRequest(method: str, url: str, paramters: dict):
	try:
		if method.lower() == 'post':
			content = requests.post(url, data=paramters)
		else:
			content = requests.get(url, params=paramters)


		print(content)
		print("\n")
		
		try:
			json_data = json.loads(str(content.text))
			print(json.dumps(json_data, indent=4, separators=(',', ': '), ensure_ascii=False))
		except:
			print(str(content.text))

	except Exception as e:
		print(e.args)	


def parseParamters(p: str) -> dict:
	pdict = dict()
	try:
		p = str(p)
		p = p[1:-1]                     # 截取json的两个括号
		plist = p.split(",")
		
		for i in plist:
			k, v = str(i).split(":")
			pdict[k] = v
	except:
		plist = p.split("&")

		for i in plist:
			k, v = str(i).split("=")
			pdict[k] = v
			
	return pdict


if __name__ == '__main__':
	print("----------------------------------------------------------------------")

	if len(sys.argv) >= 3:
		method = sys.argv[1]
		url = sys.argv[2]

		if len(sys.argv) == 4 and sys.argv[3].strip():
			paramters = sys.argv[3]
			paramters = parseParamters(paramters)
		else:
			paramters = dict()

		sendRequest(method, url, paramters)
	else:
		sys.exit()
