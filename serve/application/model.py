#coding:utf-8

# 1、需要定义数据库（初始化）
#     - course表 
#     - category表
#     - resouce表
#     - actcode表
# 2、需要对表增删改查
#     - course 
#     - category
#     - resource 
#     - actcode
# 


import json

# 引入配置字典
from config.config import config 

# 导入sqlalchemy的相关
from sqlalchemy import Column,Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# # 基类：
# Base = declarative_base()


# # 定义数据库和表
# class Course(Base):

#     __tablename__ = "Course"

#     # 表字段
#     id = Column('id',Integer,primary_key=True)
#     name = Column('name',String(40))
#     description = Column('name',String(100))
#     category_id = Column('name',String())






























# 分类模拟数据,测试
fake_category = [
{
    'category_id':3213,
    'category_name':"前端开发",
    'category_count':12,
    'category_course':[{
        'course_id':'121',
        'course_name':'Vue.js课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'139',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    {
        'course_id':'121',
        'course_name':'Vue.js课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'139',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    {
        'course_id':'121',
        'course_name':'Vue.js课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'139',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
        {
        'course_id':'121',
        'course_name':'Vue.js课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'139',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    ]
},
{
    'category_id':4341,
    'category_name':"后端开发",
    'category_count':12,
    'category_course':[{
        'course_id':'121',
        'course_name':'Vue.js课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'139',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    {
        'course_id':'121',
        'course_name':'python课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    ]
},

{'category_id':2131,'category_name':'后端开发'},
{'category_id':1131,'category_name':'移动开发'},
{
    'category_id':9041,
    'category_name':"大数据",
    'category_count':12,
    'category_course':[{
        'course_id':'3912',
        'course_name':'数据分析课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'3091',
        'course_name':'CentOS服务器运维',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    {
        'course_id':'0313',
        'course_name':'python课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'0932',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    {
        'course_id':'0984',
        'course_name':'python课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    },
    {
        'course_id':'9301',
        'course_name':'angular.js课程',
        'course_img':r'http://img2.imgtn.bdimg.com/it/u=359120593,1637693053&fm=27&gp=0.jpg'
    },
    {
        'course_id':'9842',
        'course_name':'python课程',
        'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg'
    }
    ]
},
]


# 课程内页模拟数据

fake_course_date = {
    
    "course_category":'前端开发',
    'course_id':'121',
    'course_name':'Vue.js课程',
    'course_count':12,
    'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg',
    'course_data':[

        {'resource_id':'043','resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':'120','resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':'110','resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':'129','resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':'090','resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
    
    ]


}

# 模拟密码数据

fake_passwd_data = {
    
    "043":"ek32",
    "120":"09dk",    
    "110":"od9d",    
    "129":"0okc",    
    "093":"crs4",
    "090":"cds0"
}

if __name__ == "__main__":

    pass