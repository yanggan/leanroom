# coding:utf-8
from model import *
from dev_tools import *

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
    def category_add_status(old_category_data=None,cookies=None):
        #  前台显示已经兑换课程的功能,加工分类，返回带兑换状态的分类数据
        pass
        # # 前台显示已经兑换课程的功能
        # active_courses_list = []
        # if request.method == "GET":
        #     # 把keys拿出来,判断哪些课程已经兑换过
        #     cookies_keys_list = request.cookies.keys()
        #     # for出来cookies里面保存的已经兑换的课程id
        #     long_str = ''.join(cookies_keys_list)
        #     print "test",long_str
        #     active_courses_list = re.findall(r'course_(\d+)',long_str)
        #     print active_courses_list
        #     # 处理新的cate_data
        #     new_cate_data = []
        #     for cate in  cate_real_data:
        #         for active_id in active_courses_list:
        #             print cate.id,type(cate.id)
        new_category_data = []
        return old_category_data

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