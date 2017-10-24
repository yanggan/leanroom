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
from sqlalchemy import Column,Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 基类：
Base = declarative_base()

# 解决sqlalchemy插入中文提示错误的问题
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


# 定义数据库和表
class Course(Base):

    # 课程表
    __tablename__ = "Course"

    # 表字段
    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String(40))
    description = Column('description',String(100))
    img_url = Column('img_url',String(100))
    # category_id = Column('category_id')


    # 和兑换码的关系,1个课程对应n个兑换码
    course_actcode = relationship("Actcode")
    # 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

    # 和分类的关系，1个课程对应多个分类，定义外键
    category_id = Column(Integer, ForeignKey('Category.id'))
    # 在子表类中通过 foreign key (外键)引用父表的参考字段

    # 增删改查使用静态方法
    @staticmethod
    def add_course():
        pass

    @staticmethod
    def get_course():
        pass

    @staticmethod
    def update_course():
        pass

    @staticmethod
    def del_course():
        pass



class Category(Base):

    __tablename__ = 'Category'

    # 分类表

    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String)
    description = Column('description',String)

    # 和课程的关系
    # 和分类的关系,1个课程对应多个分类，定义关系属性
    category_course = relationship("Course")



    # 增删改查使用静态方法      
    @staticmethod
    def get_session(engine):
        # 获取session对象
        DBSession = sessionmaker(bind=engine)
        sess = DBSession()
        print "OK"
        return sess

    @staticmethod
    def init_category():
        #初始化分类  
        # 初始分类：
        cate_list = [u'前端开发',u'后端开发',u"数据库",u'IOS开发',u'Android开发',u"运维开发",u'编程语言',u'数据结构和算法',u'数据分析'] 
        id_start_numbers = 1000

        # 创建session对象:
        sess = Category.get_session(engine)
        # 循环插入
        add_cate_list = []

        # 查询是是否已经有了对象,有就不插入
        count = sess.query(Category).filter(Category.id).count()
        if count != 0:
            return 'Existing data'

        for index,cate in enumerate(cate_list):
            # 第一次就规定ID
            if index == 0:

                print "第一次",index,cate
                new_cate = Category(id=id_start_numbers,name=cate)
                add_cate_list.append(new_cate)

            else:
                print index,cate
                new_cate = Category(name=cate)
                add_cate_list.append(new_cate)


        print add_cate_list,len(add_cate_list)

        # 一次性添加
        sess.add_all(add_cate_list)
        # 提交 
        sess.commit()

        # 关闭session:
        sess.close()
        
        return "OK"
        

    @staticmethod
    def add_category(add_list=[]):
        # 传入参数：[{'id':1000,'name':'xxx','descripiton':'xxx'},{},{}]
        if add_list == []:
            return "No add data"

        # 获取sess/插入
        sess = Category.get_session(engine)

        add_cate_list = []
        # 插入
        for cate in add_list:
            new_cate = Category( 
                id=cate.get('id'),
                name=cate.get('name'),
                description=cate.get('description')
                )
            add_cate_list.append(new_cate)
        sess.add_all(add_cate_list)
        sess.commit()
        sess.close()
        
        return "OK"

    @staticmethod
    def get_category(where=''):
        # 直接全部
        sess = Category.get_session(engine)
        for instance in sess.query(Category).order_by(Category.id):
            print(instance.id, instance.name)
        
        return [{},{},{}]

    @staticmethod
    def update_category():
        pass

    @staticmethod
    def del_category():
        pass



class Resource(Base):

    # 百度云链接资源表
    __tablename__ = "Resource"

    # 表

    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String(100))
    url = Column('url',String(100))
    passwd = Column('passwd',String(100))
    update_time = Column('update_time',String(100))

    # 增删改查使用静态方法
    @staticmethod
    def add_resource():
        pass

    @staticmethod
    def get_resource():
        pass

    @staticmethod
    def update_resource():
        pass

    @staticmethod
    def del_resource():
        pass



class Actcode(Base):

    # 资源表
    __tablename__ = 'Actcode'

    # 表

    id = Column('id',Integer, primary_key=True,autoincrement=True)
    code = Column('code',String(100))

    # 和course的关系
    course_id = Column(Integer, ForeignKey('Course.id'))
    # 在子表类中通过 foreign key (外键)引用父表的参考字段

    # 增删改查使用静态方法
    @staticmethod
    def add_actcode():
        pass

    @staticmethod
    def get_actcode():
        pass

    @staticmethod
    def update_actcode():
        pass

    @staticmethod
    def del_actcode():
        pass





# 初始化数据库连接:sqlite:///./application/db/learoom.db
engine = create_engine(config["default"].SQLALCHEMY_DATABASE_URI,echo=True)

# 直接 python model.py 开启这个路径
# engine = create_engine('sqlite:///./db/learoom.db',echo=True)

engine.raw_connection().connection.text_factory = str  # 解决中文插入乱码问题



# 创建数据库和表结构（目前不支持自动更新表结构，智能删库重新）
Base.metadata.create_all(bind=engine)



# 初始化category表
print Category.init_category()
# print Category.add_category([{'id':None,'name':u'科学计算','descripiton':'xxx'}])
print Category.get_category()






















# 分类模拟
fake_category = [
{
    'category_id':3213,
    'category_name':"所有课程",
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