import json
import time
import random
from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get("https://piaofang.maoyan.com/dashboard")
time.sleep(2)
texts = chrome.find_elements_by_xpath("//div[@class='cal-box']/span")

now = time.strftime("%H:%M:%S",time.localtime())
num = texts[1].text
result = {"now":now,"num":num}
json_result = json.dumps(result)#将字典转换为json
#loads将json转换为字典
time.sleep(2)
print("content-type:application/json")#返回
print('\n')
print(json_result)


# import json
# import time
# import random
#
# now = time.strftime("%H:%M:%S",time.localtime())
# num = random.randint(1,11)
# result = {"now":now,"num":num}
#
# json_result = json.dumps(result)#将字典转换为json
# #loads将json转换为字典
#
# print("content-type:application/json")#返回
# print('\n')
# print(json_result)