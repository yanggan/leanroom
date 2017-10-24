# coding:utf-8
from model import *



def init_course():

    print Course.add_course([
        {
            'id':10000,
            'name':u'HTML/CSS课程',
            'description':u'WEB最基础的内容学习',
            'img_url':"/static/img/course/html.jpg",
            'category_id':1000
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
            'category_id':1002
        },
        {
            'id':None,
            'name':u'Mysql课程',
            'description':u'',
            'img_url':"/static/img/course/mysql.jpg",
            'category_id':1002
        },
        {
            'id':None,
            'name':u'Oracle课程',
            'description':u'',
            'img_url':"/static/img/course/oracle.jpg",
            'category_id':1002
        },
        {
            'id':None,
            'name':u'SQLServer课程',
            'description':u'',
            'img_url':"/static/img/course/sqlserver.jpg",
            'category_id':1002
        },        
        {
            'id':None,
            'name':u'MongoDB课程',
            'description':u'',
            'img_url':"/static/img/course/mongodb.jpg",
            'category_id':1002
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

    return Category.init_category()


if __name__ == "__main__":

    print init_category()
    print init_course()
    print init_resouce()
    print add_resouce()
    
    pass