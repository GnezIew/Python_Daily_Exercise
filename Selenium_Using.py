from selenium import webdriver

#1.实例化一个浏览器驱动
chrome = webdriver.Chrome()
#2.访问页面
chrome.get("https://www.baidu.com/")
#3.捕获元素
inputs = chrome.find_element_by_id("kw")
#4.对元素进行操作
inputs.send_keys("李彦宏")
#
button = chrome.find_element_by_id("su")
button.click()