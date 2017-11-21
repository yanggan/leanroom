# coding:utf-8
from model import *
from dev_tools import *

import re

class Data_Processor(object):
    """
    docstring for Data_Processor
    1、数据流: model(db) -> Processor -> view -> templates -> browser
    2、业务流：
        - 获取分类数据
        - 分类数据加工
        - 获取课程详细数据
        - 验证兑换码

    """
    def __init__(self):
        pass

    @staticmethod
    def get_category():
        # 获取分类
        pass
        return Category.get_category()

    @staticmethod
    def get_category_has_status(cookies=None):
        #  前台显示已经兑换课程的功能,加工分类，返回带兑换状态的分类数据
        new_category_data = []
        active_courses_list = []
        
        print "进入get_category_has_status功能"

        # 把keys拿出来,判断哪些课程已经兑换过
        cookies_keys_list = cookies.keys()
        # for出来cookies里面保存的已经兑换的课程id
        cookies_str = ''.join(cookies_keys_list)
        # print "test",long_str
        active_courses_list = re.findall(r'course_(\d+)',cookies_str)
        has_active_course = False
        if active_courses_list != []:
            has_active_course = True
            active_courses_list = [ int(x) for x in active_courses_list ]        
            print active_courses_list,type(active_courses_list[0]) # 如 ['10000']
            new_data = Category.get_category(is_active_id=active_courses_list)
            return {'category_data':new_data,'has_active_course':has_active_course } 
        else:
            return {'category_data':Category.get_category(),'has_active_course':has_active_course }  
        

    @staticmethod
    def verify_actcode(course_id,user_input_key):
        #  验证兑换码
        pass
        return Actcode.verify_actcode(course_id,user_input_key)

    @staticmethod
    def get_course_data(course_id):
        # 获取课程数据
        pass
        return Course.get_one_course(course_id)

    @staticmethod
    def get_devtools_data():
        # 获取课程数据
        # 开启或者关闭调试信息功能
        # show_git_data()
        if config["default"].GIT_VERSION_DISPLAY:
            
            git_data = show_git_data()
            dev_data = {
                'flag':config["default"].GIT_VERSION_DISPLAY,
                'git': git_data
            }
        else:

            dev_data = {
                'flag':config["default"].GIT_VERSION_DISPLAY,
            }

        return dev_data
    
    @staticmethod
    def get_passwd_data(course_data):
        # 获取课程id+密码的dict
        pass
        return course_data.get('passwd_dict')
    @staticmethod
    def get_course_free_status(course_data):

        pass
        return course_data.get('course_is_free')

    @staticmethod
    def act_verify(user_input_act=None):
        # 给验证码，验证对应课程
        # 返回flash
        
        if user_input_act == None:
            print "没有表单数据"
            return {'flag':False,'status':'no act code','flash':'未输入兑换码'}
        user_input_act = re.search(r'\d{4}',user_input_act).group() 
        print "用户输入数据：",user_input_act
        result = Actcode.verify_only_actcode(user_input_act)
        print result

        return result
    @staticmethod
    def get_category_has_bookdata():
        # 查询分类
        x =  Category.get_bookslist_category()
        print x
        return x