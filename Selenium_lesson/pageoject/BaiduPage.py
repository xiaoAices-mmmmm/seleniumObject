from Selenium_lesson.framework.base_page import BasePage
class baidu(BasePage):
    kw=['id','kw']#定位搜索输入框
    su=['id','su']#定位搜索按钮
    def kw_send(self,value):#搜索框输入内容
        self.send(self.kw,value)
    def kw_click(self):
        self.click(self.su)
class Qemil(BasePage):#QQ邮箱方法
    uname = ('id', "u")
    pwd = ('id', "p")
    submit = ('id', "login_button")
    def u_uname(self,value):
        self.send(self.uname,value)
    def p_pwd(self,value):
        self.send(self.pwd,value)
    def L_submit(self):
        self.click(self.submit)
