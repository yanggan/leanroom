#coding:utf-8
import json
from cprint import cprint

# 分类模拟数据
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
]


# 分类模拟数据

fake_course_date = {
    
    "course_category":'前端开发',
    'course_id':'121',
    'course_name':'Vue.js课程',
    'course_count':12,
    'course_img':r'http://vue-js.org/images/vue-js-what-is-that.jpg',
    'course_data':[

        {'resource_id':1,'resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':1,'resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':1,'resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':1,'resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
        {'resource_id':1,'resource_name':"vue.js入门套课","update_time":'2017.9.11','resource_addr':"http://pan.baidu.com/dad3e",'resource_passwd':"AED3"},
    
    ]


}

if __name__ == "__main__":

    pass