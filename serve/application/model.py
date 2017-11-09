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
from sqlalchemy import Column,Integer, String,Float,Boolean,create_engine,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 基类：
Base = declarative_base()

# 解决sqlalchemy插入中文提示错误的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import os
import datetime

import random,string,uuid

# 定义数据库和表
class Course(Base):

    # 课程表
    __tablename__ = "Course"

    # 表字段
    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String(40))
    description = Column('description',String)
    img_url = Column('img_url',String(100))
    # category_id = Column('category_id')
    taobao_id = Column('taobao_id',Integer)
    taobao_price = Column('taobao_price',Float)
    is_free = Column('is_free',Boolean,default=False)
    read_count = Column('read_count',Integer,default=0)

    # 课程的打包资源url链接
    course_url = Column('course_url',String)
    course_passwd = Column('course_passwd',String)

    # 和兑换码的关系,1个课程对应n个兑换码
    course_actcode = relationship("Actcode")
    # 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

    course_resouce = relationship("Resource")
    course_size = Column('couse_size',Float,default=0)


    # 和分类的关系，1个课程对应多个分类，定义外键
    category_id = Column(Integer, ForeignKey('Category.id'))
    # 在子表类中通过 foreign key (外键)引用父表的参考字段

    # 增删改查使用静态方法
    @staticmethod
    def get_session(engine):
        # 获取session对象
        DBSession = sessionmaker(bind=engine)
        sess = DBSession()
        print "OK"
        return sess

    @staticmethod
    def add_course(add_list=[]):
        # 传入参数：[{'id':1000,'name':'xxx','descripiton':'xxx','img_url':'','category_id':id},{}]
        if add_list == []:
            return "No Course add data"

        # 获取sess/插入
        sess = Course.get_session(engine)

        add_cate_list = []
        # 插入
        for cate in add_list:
            new_cate = Course( 
                id = cate.get('id'),
                name = cate.get('name'),
                description = cate.get('description'),
                img_url = cate.get('img_url'),
                category_id = cate.get('category_id'),
                is_free=cate.get('is_free'),
                read_count = cate.get('read_count')
                )
            add_cate_list.append(new_cate)

        sess.add_all(add_cate_list)
        sess.commit()
        sess.close()

        
        return "Course add OK"

    @staticmethod
    def count_course_size(course_id=0):
        # 统计课程资源的总大小,如果不传特定id进来，更新所有课程大小
        sess = Course.get_session(engine)
        size = 0
        if course_id == 0:
            # 更新所有课程的课程大小
            all_course_list = sess.query(Course).all()
            for course in all_course_list:
                # 每个课程的大小，for资源大小相加
                for resource in course.course_resouce:
                    size = size + resource.size

                # 更新课程size
                course.course_size = size
                size = 0 
            sess.commit()
            sess.close()
            return 'update all course resource size succeed'

        course_case = sess.query(Course).filter_by(id=course_id).one()
        print course_case
        for resource in course_case.course_resouce:
            size = size + resource.size
        print size
        return size

    @staticmethod
    def get_one_course(course_id=None):
        # 如果为空，则不处理,例如couse_id = 10000
        if course_id == None:
            return 'no have course_id'
        
        sess = Course.get_session(engine)
        # 先更新所有的课程的resource_size字段
    
        try:
            course_case = (sess.query(Course).filter_by(id=course_id).one())
        except Exception as e:
            sess.commit()
            sess.close()
            return {'flag':False,'status':'This course is not found','course_data':None}

        
        print '分类ID',course_case.category_id
        # 包含的资源和密码字典



        course_data = []
        passwd_dict = {}
        for x in course_case.course_resouce:
            course_data.append({
                'resource_id':x.id,
                'resource_name':x.name,
                'resource_description':x.description,
                'content_type':x.content_type,
                "update_time":x.update_time,
                'resource_addr':x.url,
                'resource_size':x.size,
                'resource_passwd':x.passwd
                })
            passwd_dict[x.id] = x.passwd 
        # 给模板的字典结构
        return_data = {
            "course_category":sess.query(Category).filter_by(id=course_case.category_id).one().name,
            'course_id':course_case.id,
            'course_name':course_case.name,
            'course_count':len(course_case.course_resouce),
            'course_img':course_case.img_url,
            'course_data':course_data,
            'course_size':course_case.course_size,
            'passwd_dict':passwd_dict,
            'course_is_free':course_case.is_free,
            'course_share_url':course_case.course_url,
            'course_share_passwd':course_case.course_passwd,
            'course_read_count':round(float(course_case.read_count)/1000,2)

        }
        # 增加阅读量
        if course_case.read_count == None or course_case.read_count == 0 :
            course_case.read_count = 1
        else:
            course_case.read_count = course_case.read_count + 1
        
        sess.commit()
        sess.close()
        return {'flag':True,'status':'find the course succeed','course_data':return_data}

    @staticmethod
    def get_all_course():
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
        print "Get sesssion OK"
        return sess

    @staticmethod
    def init_category(cate_list=[]):
        #初始化分类  
        # 初始分类：
        if cate_list == []:
            cate_list = [u'前端开发',u'后端开发',u"数据库",u'IOS开发',u'Android开发',u"运维开发",u'编程语言',u'数据结构和算法',u'网络安全',u'数据分析'] 
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
    def get_category(where='',is_active_id=[]):
        # 直接全部
        sess = Category.get_session(engine)
        real_data = []

        # 统计课程大小
        Course.count_course_size()

        # 查询分类 
        for instance in sess.query(Category).order_by(Category.id):
            # print(instance.id, instance.name,instance.category_course)
            # instance.category_course 是cate对应的课程list
            cate_course = []
            is_active_flag = 0
            is_active_course_data = []
            cate_has_active_course = None
            for course_data in instance.category_course:
               
                if is_active_id !=[]:

                    # 判断激活id = 课程id
                    is_active_flag = [1 if i==course_data.id else 0 for i in is_active_id]
                    is_active_flag = 1 if 1 in is_active_flag  else 0
                    
                    x = {
                        'course_id':course_data.id,
                        'course_name':course_data.name,
                        'course_img':course_data.img_url,
                        'course_size':course_data.course_size,
                        'category_id':course_data.category_id,
                        'is_active':is_active_flag,
                        'course_is_free':course_data.is_free,
                        'course_count':len(course_data.course_resouce),
                        'course_read_count':round(float(course_data.read_count)/1000,2)
                    }
                    is_active_course_data.append(x) if is_active_flag == 1 else None
                    is_active_flag = 0
                    
  
                    
                else:
                    x = {
                        'course_id':course_data.id,
                        'course_name':course_data.name,
                        'course_img':course_data.img_url,
                        'course_size':course_data.course_size,
                        'category_id':course_data.category_id,
                        'course_is_free':course_data.is_free,
                        'is_active':0,
                        'course_count':len(course_data.course_resouce),
                        'course_read_count':round(float(course_data.read_count)/1000,2)
                    }
                
                cate_course.append(x)
                # 增加阅读量
                if course_data.read_count == None:
                    course_data.read_count = 1
                else:
                    course_data.read_count = course_data.read_count + 1
                sess.commit()

            # 给模板的数据结构
            data = {
                'category_id':instance.id,
                'category_name':instance.name,
                'category_count':len(instance.category_course),
                'category_course':cate_course,
                'category_active_course': is_active_course_data if is_active_course_data != [] else None
            
            }
            real_data.append(data)
        # print(real_data)
        sess.close()
        return real_data

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
    description = Column('description',String)
    url = Column('url',String(100))
    passwd = Column('passwd',String(100))
    size = Column('size',Float)
    update_time = Column('update_time',String)

    # 1：视频，2：视频+源码 3：视频+项目实战 4：书籍
    content_type = Column('content_type',Integer,default=False)

    # 外键，一个课程对应多个资源
    course_id = Column(Integer, ForeignKey('Course.id'))

    # 增删改查使用静态方法      
    @staticmethod
    def get_session(engine):
        # 获取session对象
        DBSession = sessionmaker(bind=engine)
        sess = DBSession()
        print "Get sesssion OK"
        return sess

    @staticmethod
    def add_resource(add_list):
        # 传入参数：[{'id':1000,'name':'xxx','descripiton':'xxx','img_url':'','category_id':id},{}]
        if add_list == []:
            return "No Course add data"

        # 获取sess/插入
        sess = Resource.get_session(engine)

        add_res_list = []
        # 插入
        for res in add_list:
            new_res = Resource( 
                id = res.get('id'),
                name = res.get('name'),
                description = res.get('description'),
                url = res.get('url'),
                passwd = res.get('passwd'),
                size = res.get('size'),  
                update_time = datetime.datetime.now().strftime('%Y-%m-%d'),
                content_type = res.get('content_type'),
                course_id = res.get('course_id')
                )
            add_res_list.append(new_res)
        sess.add_all(add_res_list)
        sess.commit()
        sess.close()
        
        return "Resource add OK"        



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
    code = Column('code',String)
    use_count = Column('use_count',Integer,default=0)
    is_use =  Column('is_use',Boolean,default=False)
    is_invalid = Column('is_use',Boolean,default=False) # 为ture则兑换码不可用
    # 和course的关系
    course_id = Column(Integer, ForeignKey('Course.id'))
    # 在子表类中通过 foreign key (外键)引用父表的参考字段



    # 增删改查使用静态方法
    @staticmethod
    def get_session(engine):
        # 获取session对象
        DBSession = sessionmaker(bind=engine)
        sess = DBSession()
        print "Get sesssion OK"
        return sess

    @staticmethod
    def init_actcode(course_number=50):
        # course_number为每个课程初始化多少个兑换码
        sess = Actcode.get_session(engine)
        all_course_list = sess.query(Course).all()
        print'所有课程',all_course_list,len(all_course_list)

        new_code_list = []
        chars = string.digits
        for course in all_course_list:
            # 每个课程遍历生成
            print '课程 %s 正在生成 %s 个兑换码...' % (course.name,str(course_number))
            # 12cd12
  
            # 每个课程生成100兑换码
            for i in range(course_number):

                code = "".join(random.choice(chars) for i in range(4)) #兑换码
                print code
                # 
                new_code = Actcode(
                    # id = 100,
                    code = code,
                    course_id = course.id
                    )

                new_code_list.append(new_code)
        
        # 1、生成一定数量的 2、查重，避免重复，然后再插入数据


        sess.add_all(new_code_list)
        sess.commit()
        sess.close()
        return "init actcode succeed"

    @staticmethod
    def init_unique_actcode(course_number=30):
        # 1、生成一定数量的 2、查重，避免重复，然后再插入数据
        sess = Actcode.get_session(engine)
        all_course_list = sess.query(Course).all()

        print len(all_course_list)
        for_times = course_number *  len(all_course_list)
        chars = string.digits
        code_list = []
        act_code_obj_list = []
        # 用来判断不重复的函数
        def check_code(code,code_list):
            if code in code_list:
                new_code = "".join(random.choice(chars) for i in range(4)) #兑换码   
                new_code = check_code(new_code,code_list)
                return new_code
            else:
                return code

        for index in range(for_times):
            code = "".join(random.choice(chars) for i in range(4)) #兑换码   
            code = check_code(code,code_list)
            code_list.append(code)
        
        # 插入数据,把code_list改为生成器,用code_gen.next()取值
        code_gen = (code for code in code_list)
        
        for course in all_course_list:
            for i in range(course_number):
                # print (course.id,code_gen.next()) # 如(10013, '8386')
                new_code = Actcode(
                    # id = 100,
                    code = code_gen.next(),
                    course_id = course.id
                    )
                act_code_obj_list.append(new_code)

        sess.add_all(act_code_obj_list)
        sess.commit()
        sess.close()
        return "init actcode succeed"

    @staticmethod
    def add_actcode(course_id,course_add_number=50):
        # 1、取出所有码 2、生成新的码，确保唯一性 3、写入新的码
        sess = Actcode.get_session(engine)
        course_case = sess.query(Course).filter_by(id=course_id).one()
        all_actcode_obj_list = sess.query(Actcode).all()
        chars = string.digits
        # print course_case.id
        # print len(all_actcode_obj_list)
        # 现有的兑换码列表
        db_actcode_list = [actcode.code for actcode in all_actcode_obj_list ]
        new_actcode_list = []
        new_actcode_obj_list = []
        # 检察唯一性
        def check_code(code,code_list):
            if code in code_list:
                new_code = "".join(random.choice(chars) for i in range(4)) #兑换码   
                new_code = check_code(new_code,code_list)
                return new_code
            else:# 不重复，返回原来的code
                return code
        # 生成新的码，保证new_actcode_list是唯一的
        for index in range(course_add_number):
            code = "".join(random.choice(chars) for i in range(4)) #兑换码   
            code = check_code(code,new_actcode_list)
            new_actcode_list.append(code)
        print new_actcode_list
        # 对比db的码，有重复就重新生成,没重复就写入数据库
        for code in new_actcode_list:
            # 判断唯一
            code = check_code(code,db_actcode_list)
            # 写入数据
            new_code = Actcode(
                    # id = 100,
                    code = code,
                    course_id = course_case.id
                    )
            new_actcode_obj_list.append(new_code)
        
        sess.add_all(new_actcode_obj_list)
        sess.commit()
        sess.close()
        return "add actcode succeed"

    @staticmethod
    def get_actcode():
        pass

    @staticmethod
    def update_actcode():
        pass

    @staticmethod
    def del_actcode():
        pass

    @staticmethod
    def verify_actcode(course_id=None,act_code=None):
        # 验证是否有效
        # x = {'flag':False,'status':"兑换码不正确，请联系客服"}
        # y = {'flag':True,'status':"兑换成功"}
        if course_id ==None or act_code == None:
            return "no course or code pass in"

        sess = Actcode.get_session(engine)
        # 查询
        try:
            result = sess.query(Actcode).filter_by(code=act_code,course_id=course_id).one()
        except Exception as e:
            x = '兑换码错误，请联系客服'
            print x
            sess.close()
            return  {'flag':False,'status':x}
        else:
            # 兑换码正确,统计次数
            print result
            print result.id,result.code,result.course_id,result.use_count
            # 设置失效的兑换码也不可用
            if result.is_invalid == True:
                sess.commit()
                sess.close()
                return  {'flag':False,'status':'兑换码已失效'}
            result.is_use= True
            result.use_count = result.use_count + 1
            sess.commit()
            sess.close()
            return {'flag':True,'status':"兑换成功"}

    @staticmethod
    def verify_only_actcode(act_code=None):
        # 通过验证码直接查询课程
        # {'flag':True,'status':"find actcode and course succeed",'course_data':course_data}
        if act_code == None:
            return "no code pass in"
        sess = Actcode.get_session(engine)
        

        try:
            # 没有找到返回none,多余一个则异常
            result_actcode = sess.query(Actcode).filter_by(code=str(act_code)).one_or_none()
        except Exception as e: #大于1个报错
            # x = 'this act code  more than one course'
            # print x
            sess.close()
            return  {'flag':False,'error_code':600,'status':'this act code  more than one course','course_data':None}
        else:
            if result_actcode == None: # 找不到
                sess.close()
                return  {'flag':False,'error_code':700,'status':"no this actcode",'course_data':None}
            else:
                # 兑换码正确,统计次数
                # print result_actcode
                # print result_actcode.id,result_actcode.code,result_actcode.course_id,result_actcode.use_count
                # 设置失效的兑换码也不可用
                if result_actcode.is_invalid == True:
                    sess.close()
                    return  {'flag':False,'status':'act code invalid','error_code':800,'course_data':None}
                # 验证码有效，查找到，添加统计


                # 附带课程数据
                course_data = sess.query(Course).filter_by(id=result_actcode.course_id).first()

                # 给课程添加访问量
                # 增加阅读量
                if course_data.read_count == None or course_data.read_count == 0 :
                    course_data.read_count = 1
                else:
                    course_data.read_count = course_data.read_count + 1

                if course_data == None:
                    sess.close()
                    return  {'flag':False,'status':'act code cannot find course ','error_code':1000,'course_data':None}
                #  把对象转为dict
                course_data = {
                    'course_id':course_data.id,
                    'course_name':course_data.name,
                    'course_img':course_data.img_url,
                    'course_size':course_data.course_size,
                    'category_id':course_data.category_id,
                    'course_is_free':course_data.is_free
                }
                # 统计code的使用
                result_actcode.is_use=True
                result_actcode.use_count = result_actcode.use_count + 1

                sess.commit()
                sess.close()
                return  {'flag':True,'error_code':200,'status':"find actcode and course succeed",'course_data':course_data}
        

    @staticmethod
    def check_actcode_unique():
        # 查重
        pass


# 初始化数据库连接:sqlite:///./application/db/learoom.db
engine = create_engine(config["default"].SQLALCHEMY_DATABASE_URI,echo=True)

# 直接 python model.py 开启这个路径
# engine = create_engine('sqlite:///./db/learoom.db',echo=True)

engine.raw_connection().connection.text_factory = str  # 解决中文插入乱码问题



# 创建数据库和表结构（目前不支持自动更新表结构，智能删库重新）
Base.metadata.create_all(bind=engine)



# 初始化category表
# print Category.init_category()
# print Category.add_category([{'id':None,'name':u'科学计算','descripiton':'xxx'}])






if __name__ == "__main__":

    # 修改工作路径，方便直接python model
    print "当前工作目录为"
    print(os.getcwd()) # 打印当前工作目录
    os.chdir('../') # 将当前工作目录改变为`/Users/<username>/Desktop/`
    print "当前工作目录为"
    print(os.getcwd()) # 打印当前工作目录

    # x = Course.get_one_course(10000)
    # print x

    # x = Course.count_course_size()
    # print x
    # x = Actcode.init_actcode()
    # print x

    # x = Actcode.verify_actcode(course_id=10000,act_code=2873)
    # print x

    # x = Actcode.verify_only_actcode(act_code=5128)
    # print x

    # x = Actcode.init_unique_actcode()
    # print x

    x = Actcode.add_actcode(10000,20)
    print x
   