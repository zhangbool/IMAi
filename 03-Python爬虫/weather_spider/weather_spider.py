import requests

#content = requests.get("https://m.zq12369.com/cityselect.php").content.decode("utf8")
content = requests.get("http://pm25.in/shanghai").content.decode("utf8")

print(content)

#https://api.map.baidu.com/?qt=s&c=1&wd=北京
