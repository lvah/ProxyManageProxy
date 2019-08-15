import requests

url = 'http://172.25.254.197:7777/get_proxy/'
proxy = requests.get(url).text
print(proxy)


