class BasePage(object):

    def __init__(self,driver):
        #重置方法
        self.driver=driver
    def find_element(self,selector):
        by =selector[0]
        value=selector[1]
        element=None
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'css' or by == 'xpath':
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by =='tag':
                element = self.driver.find_element_by_tag_name(value)
            elif by == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif by == 'plink':
                element =self.driver.find_element_by_partial_link_text(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            else:
                print('没有找到元素')
            return element
        else:
            print('输入的元素定位方式错误')
    def send(self,selector,value):
        element=self.find_element(selector)#调用
        try:
            element.send_keys(value)
            print('输入的内容%s'%value)
        except BaseException:
            print('error')
    def click(self,selector):
        element=self.find_element(selector)
        element.click()

