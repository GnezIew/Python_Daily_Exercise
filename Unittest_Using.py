#断言 编写代码时，我们总是会做出一些假设，断言就是用于在代码中捕捉这些假设，可以将断言看作是异常处理的一种高级形式。
#assert代表断言，假设断言的条件为真，如果为假诱发AssertionError
#assert 断言的条件，错误的提升
# a = 1
# assert a,"a is false"
# print(a)

#上面的断言代码类似下面的if语句

# a = 1
# if not a :
#     raise AssertionError("a is false")
# else:
#     print("a is not false")

import unittest
#unittest的使用

class OurTest(unittest.TestCase):
    """
    编写测试的基础类
    """
    def setUp(self):
        """
        类似于类的init方法，在测试之初自动执行，通常用来做测试的准备
        """