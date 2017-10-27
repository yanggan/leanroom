# coding:utf-8
from model import *



def init_course():

    print Course.add_course([
        {
            'id':10000,
            'name':u'HTML/CSS课程',
            'description':u'WEB最基础的内容学习',
            'img_url':"/static/img/course/html.jpg",
            'category_id':1000,
            'is_free':True
        },
        {
            'id':None,
            'name':u'Bootstrap框架课程',
            'description':u'高效简单的必学框架',
            'img_url':"/static/img/course/bootstrap.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'Javascript课程',
            'description':u'前端开发的必学语言',
            'img_url':"/static/img/course/js.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'jQuery库课程',
            'description':u'一个JavaScript库,极大简化了JavaScript编程',
            'img_url':"/static/img/course/jq.jpg",
            'category_id':1000
        },        
        {
            'id':None,
            'name':u'Vue.js前端框架课程',
            'description':u'轻量级的前端JS框架',
            'img_url':"/static/img/course/vue.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'React前端框架课程',
            'description':u'来自Facebook的JS框架',
            'img_url':"/static/img/course/react.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'AngularJS前端框架课程',
            'description':u'来自Google开发的前端JS框架',
            'img_url':"/static/img/course/angular.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'Node.Js课程',
            'description':u'前端必学的Javascript运行环境',
            'img_url':"/static/img/course/nodejs.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'前端Photoshop课程',
            'description':u'前端切图必学必会',
            'img_url':"/static/img/course/ps.jpg",
            'category_id':1000
        },
        {
            'id':None,
            'name':u'Sqlite课程',
            'description':u'',
            'img_url':"/static/img/course/sqlite.jpg",
            'category_id':1006
        },
        {
            'id':None,
            'name':u'Mysql课程',
            'description':u'',
            'img_url':"/static/img/course/mysql.jpg",
            'category_id':1006
        },
        {
            'id':None,
            'name':u'Oracle课程',
            'description':u'',
            'img_url':"/static/img/course/oracle.jpg",
            'category_id':1006
        },
        {
            'id':None,
            'name':u'SQLServer课程',
            'description':u'',
            'img_url':"/static/img/course/sqlserver.jpg",
            'category_id':1006
        },        
        {
            'id':None,
            'name':u'MongoDB课程',
            'description':u'',
            'img_url':"/static/img/course/mongodb.jpg",
            'category_id':1006
        }

    ])
    return "init course OK"

def init_resouce():
    print Resource.add_resource([

            {
                'id':600000,
                'name':u'Html入门到精通视频合集',
                'url':"http://pan.baidu.com/s/1c1OgW3A",
                'passwd':'yhaa',
                'size':'3.2',
                'course_id':10000

            }

    ])
    return "init resource ok"

def add_resouce():
    print Resource.add_resource([

            {
                'id':None,
                'name':u'Bootstrap入门到精通视频合集',
                'url':"http://pan.baidu.com/s/1c1OgW3A",
                'size':'3.2',
                'passwd':'dead',
                'course_id':10001

            },
            {
                'id':None,
                'name':u'Bootstrap入门到精通视频合集',
                'url':"http://pan.baidu.com/s/1c1OgW3A",
                'size':'3.2',
                'passwd':'dead',
                'course_id':10001

            },
            {
                'id':None,
                'name':u'Bootstrap入门到精通视频合集',
                'url':"http://pan.baidu.com/s/1c1OgW3A",
                'size':'3.2',
                'passwd':'dead',
                'course_id':10001

            },            
            {
                'id':None,
                'name':u'Bootstrap入门到精通视频合集',
                'url':"http://pan.baidu.com/s/1c1OgW3A",
                'size':'3.2',
                'passwd':'dead',
                'course_id':10001

            }

    ])
    return "add resource ok"


def init_category():

    x = [
        u'Web前端',
        u'Java开发',
        u"PHP开发",
        u'Python开发',
        u'移动端开发',
        u"运维开发",
        u'数据库',
        u'数据分析',
        u'其他'
        ] 

    return Category.init_category(x)

# # 这个部分先写方法 
# class Course_Man(object):
#     """
#     1、获取所有课程分类，和分类地下课程
#     2、获取单门课程的的信息，包含资源
#     3、获取单门课程的


#     """
#     def __init__(self):
#         pass
        
# class Act_Man(object):
#     """
#     1、生成兑换码
#     2、查询、修改兑换码
#     3、使用兑换码，验证兑换码是否有效

#     """
#     def __init__(self):
#         pass

#     def creat_act(self):
#         pass

#     def verify_act(self,course_id,act_code):
        
#         print("接受到的课程ID和兑换码")
#         print(course_id,act_code)
#         x = {'flag':False,'status':"兑换码不正确，请联系客服"}
#         y = {'flag':True,'status':"兑换成功"}

#         return y

# act = Act_Man()

# 初始化兑换码
def init_actcode():
    #初始化兑换码
    return Actcode.init_unique_actcode()

def renew_course_size():
    # 更新课程文件大小
    return Course.count_course_size()

if __name__ == "__main__":

    print init_category()
    print init_course()
    print init_resouce()
    print add_resouce()
    print init_actcode()
    print renew_course_size()
    pass