from selenium import webdriver
from Selenium_lesson.pageoject.BaiduPage import baidu,Qemil
import unittest,time
# class Baidu(unittest.TestCase):
#     def test_baidu(self):
#         dr=webdriver.Chrome()
#         dr.get('https://www.baidu.com')
#         bai=baidu(dr)
#         bai.kw_send('aini')
#         time.sleep(2)
#         bai.click()
class QQemil(unittest.TestCase):
    def test_QQemil(self):
        driver=webdriver.Chrome()
        driver.get('https://mail.qq.com/')
        driver.switch_to.frame('login_frame')
        QQ=Qemil(driver)
        QQ.u_uname('*****')
        QQ.p_pwd('*****.')
        time.sleep(2)
        QQ.L_submit()
if __name__ == '__main__':
    unittest.main()

