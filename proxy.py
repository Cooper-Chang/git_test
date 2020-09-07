# coding=utf-8
import requests


def get_proxy():
    while True:
        try:
            response = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=98a20a42362ab1cd15d722240c9d5613&ttl&random=true')
            ip_proxy = response.content.split(",")[0]

            return ip_proxy
        except Exception, e:
            print(u"获取代理出错")


