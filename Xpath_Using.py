#通过点击
#  from selenium import webdriver
# import time
# #实例化一个浏览器驱动
# def getFile():
#     chrome = webdriver.Chrome()
#     #访问页面
#     chrome.get("http://www.yznnw.com/files/article/html/10/10577/3503050.html")
#     i = 0
#     #捕获元素
#     for i in range(5):
#         texts = chrome.find_elements_by_xpath("//div[@class='contentbox']")
#         for t in texts:
#             with open("xiaoshuo.txt","a") as f:
#                 f.write(t.text)
#         time.sleep(2)
#         url = chrome.find_element_by_id('htmlxiazhang')
#         url.click()
#     chrome.close()
# getFile()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#通过网页
# from selenium import webdriver
# from time import sleep
#
# def getFile(Url):
#     chrome = webdriver.Chrome()
#     chrome.get(Url)
#     texts = chrome.find_elements_by_xpath("//div[@id='content']")
#     for t in texts:
#         with open("xiaoshuo.txt","a") as f:
#             f.write(t.text)
#     sleep(2)
#     Next_Url = chrome.find_elements_by_xpath("//div[@class='bottem2']/a")
#     if Next_Url:
#         Next_Urls = Next_Url[3].get_attribute("href")
#         chrome.close()
#         getFile(Next_Urls)
#     else:
#         chrome.close()
#
# Url = "https://www.biquga.com/14_14318/3654877.html"
# getFile(Url)


