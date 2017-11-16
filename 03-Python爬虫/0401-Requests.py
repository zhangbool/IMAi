
import requests

#request的基本使用
# print(dir(requests))
# url = "http://www.baidu.com"
# result = requests.get(url)
# print(result)
# print(result.status_code)
# print(str(result.content, "utf-8"))


#传递参数
# params = {"k1":"v1", "k2":"v2"}
# result01 = requests.get("http://httpbin.org/get", params)
# print(result01.url)


#二进制文件处理，这里用图片进行测试
# from PIL import Image
# from io import BytesIO
# result02 = requests.get("http://f.hiphotos.baidu.com/image/pic/item/91ef76c6a7efce1b101f0bd9a551f3deb48f65e9.jpg")
# image = Image.open(BytesIO(result02.content))
# image.save("C:\\Users\ivanl001\Pictures\zhang.jpg")

#json数据的处理
# result03 = requests.get("https://github.com/timeline.json")
# print(type(result03.json()))
# print(result03.json())


#原始数据处理，这里仍然以图片为例
# result04 = requests.get("http://f.hiphotos.baidu.com/image/pic/item/91ef76c6a7efce1b101f0bd9a551f3deb48f65e9.jpg")
# with open("C:\\Users\ivanl001\Pictures\zhang02.jpg", "wb+") as f:
#     for chunk in result04.iter_content(1024):
#         f.write(chunk)

#表单提交，这里的post地址貌似不行了，所以这里不纠结
# form = {"name":"ivanl001", "password":"ivan is the king of world!"}
# result05 = requests.post("http://httpbin.org/post", data=form)
# print(result05.content)

#cookie

# url = "http://www.baidu.com"
# result06 = requests.get(url)
# cookies = result06.cookies
# for key, value in cookies.get_dict().items():
#     print(key, value)

# cookies = {"c1":"v1", "c2":"v2"}
# result07 = requests.get("http://httpbin.org/cookies", cookies=cookies)
# print(result07.text)

#重定向
# result08  =requests.get("http://github.com", allow_redirects = True)
# print(result08.url)
# print(result08.status_code)
# print(result08.history)

#代理
# proxies =