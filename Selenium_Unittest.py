# import unittest
# from time import sleep
# from selenium import webdriver
#
#
# class YoujiuyeTest(unittest.TestCase):
#     def setUp(self):
#         self.chrome = webdriver.Chrome()
#         self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
#
#     def test_login_password(self):
#         username_dl = self.chrome.find_element_by_id("username_dl")
#
#         password_dl = self.chrome.find_element_by_id("password_dl")
#
#         button = self.chrome.find_element_by_class_name("loginbutton1")
#
#         username_dl.send_keys("15673474168")
#         password_dl.send_keys("123")
#         button.click()
#         text = self.chrome.find_element_by_id("J_usernameTip").text
#         self.assertEqual("密码应该为6-20位之间！",text,"密码太短提示内容有误")
#
#     def test_login_usrname(self):
#         username_dl = self.chrome.find_element_by_id("username_dl")
#
#         password_dl = self.chrome.find_element_by_id("password_dl")
#
#         button = self.chrome.find_element_by_class_name("loginbutton1")
#
#         username_dl.send_keys("13077186226")
#         password_dl.send_keys("123123546")
#         button.click()
#         sleep(2)
#         text = self.chrome.find_element_by_id("J_usernameTip").text
#         print("+++++++++++++++++++++++++++++++++++++++++++++++++")
#         print(text)
#         print("+++++++++++++++++++++++++++++++++++++++++++++++++")
#         self.assertEqual("账号不存在",text,"提示内容有误")
#
#     def tearDown(self):
#         sleep(10)
#         self.chrome.close()
#
# if __name__ == '__main__':
#     unittest.main()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class YoujiuyeTest(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")


    def login(self,username,password):
        username_dl = self.chrome.find_element_by_id("username_dl")

        password_dl = self.chrome.find_element_by_id("password_dl")

        button = self.chrome.find_element_by_class_name("loginbutton1")
        username_dl.send_keys(username)
        password_dl.send_keys(password)
        button.click()
        sleep(2)
        text = self.chrome.find_element_by_id("J_usernameTip").text
        return text

    def test_login_password(self):
        text = self.login("13054681236","123")
        self.assertEqual("密码应该为6-20位之间！",text,"密码太短提示内容有误")

    def test_login_usrname(self):
        text = self.login("13077186226","123123546")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print(text)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        self.assertEqual("账号不存在",text,"提示内容有误")

    def tearDown(self):
        sleep(10)
        self.chrome.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(YoujiuyeTest("test_login_password"))
    suite.addTest(YoujiuyeTest("test_login_usrname"))

    with open("report.html","wb") as f:
        runner = HTMLTestRunner(
            stream=f,
            title="教学测试",
            description="just a test"
        )
        runner.run(suite)