# coding:utf-8
from application import app
from flask import Flask,request,render_template,flash,redirect,url_for,session,make_response
from flask_restful import Resource, Api, abort, reqparse
import re

from model import *
from dev_tools import * 
from middleware import * 


# 避免中文传给jinja2时候报错
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



# 首页
@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])
@app.route('/course',methods=['GET'])
def index():

    # 获取分类和课程信息
    cate_data = Data_Processor.get_category_has_status(cookies=request.cookies)
    return render_template(
        "course.html",
        category=cate_data.get('category_data'),
        has_active_course=cate_data.get('has_active_course'),
        dev_data=dev_data
        )



# 课程详情页
@app.route('/course/<int:course_id>',methods=['POST','GET'])
def course_detail(course_id):

    # 各种数据获取
    course_data = Data_Processor.get_course_data(course_id)
    dev_data = Data_Processor.get_devtools_data()
    passwd_data = Data_Processor.get_passwd_data(course_data)
    is_free = Data_Processor.get_course_free_status(course_data)

    print "is free " , is_free 

    if request.method == "GET":

        # 3种情况，1、第一次访问，2、输入兑换码后，重定向访问，这时候需要返回带密码页面
        # 0、限免课程，直接返回数据
        # 1、读取用户的cookies和session，把兑换码拿出来，匹配是否是这门课程的对缓慢
        # 2、如果是这门课程的兑换码，则返回带提取密码数据的页面
        # 3、如果不是，则返回普通的页面
        # 判断session,如果有key,value就不用验证了
        if is_free == True:
            
            return render_template("course_detail.html",course_data=course_data,passwd_dict=passwd_data,dev_data=dev_data)
        
        elif session.get('course_'+str(course_id)) != None:

            user_input_key =  session.get('course_'+str(course_id))
            print user_input_key

            resp = make_response( \
                render_template("course_detail.html",course_data=course_data,passwd_dict=passwd_data,dev_data=dev_data)
                )
            return resp

        # 判断cookies,需要重新验证vaule验证码是否合法
        elif request.cookies.get('course_'+ str(course_id)) != None: #有这个课程的cookies
            
            cookie_course_key = request.cookies.get('course_'+ str(course_id))
            print cookie_course_key 
            verity_result_dict = act.verify_act(course_id,cookies_course_key) #判断code是否有效
            if verity_result_dict['flag'] == True:

                flash(verity_result_dict['status'])
                resp = make_response(\
                    render_template("course_detail.html",course_data=course_data,passwd_dict=course_data.get('passwd_dict'),dev_data=dev_data)
                    )
                return resp
        else:
            # 第一次访问
            return render_template("course_detail.html",course_data=course_data,passwd_dict=None,dev_data=dev_data)


    elif request.method == "POST":
        # 这是个用户输入兑换码后提交到后台来的数据
        # 1、获取兑换码，判断是否有效，是对应课程的兑换码[ 课程 + 兑换码 ]
        # 2、如果有效，则保持兑换码到用户的cookies
        # 3、把兑换码放到session中
        # 4、返回重定向，让浏览器get访问本链接

        user_input_key = request.form.get('key', '')        
        verity_result_dict = Data_Processor.verify_actcode(course_id,user_input_key) # 判断是否正确
    
        if verity_result_dict['flag'] == True: # 成功之后返回

            session['course_'+str(course_id)] = user_input_key # 设置session
            print session
            flash(verity_result_dict['status'])
            redirect_to_course = redirect(url_for('course_detail',course_id=course_id))
            resp = make_response(redirect_to_course)
            resp.set_cookie('course_'+str(course_id),user_input_key) # 设置cookies
            return resp # 返回response让浏览器重定向Get访问

        else: #验证失败

            flash(verity_result_dict['status'])
            return redirect(url_for('course_detail',course_id=course_id))



# 通过激活码激活课程
@app.route("/act",methods=['POST','GET'])
def course_activete():
    # pass
    if request.method == 'GET':
        return render_template('act.html')
    elif request.method == 'POST':
        user_input_act = request.form.get('act_code',None) 
        print user_input_act

        # 输入空的验证码
        if user_input_act == None or user_input_act == '':
            print "没有表单数据"
            flash(u'请输入4位数字兑换码', 'act_error')
            result_dict = {'flag':False,'status':"actcode is empty",'course_data':None,'error_code':900}
            return render_template("act.html",result_dict=result_dict)

        user_input_act = re.search(r'\d{4}',user_input_act).group()  
        # 返回 {'flag':True,'status':"find actcode and course succeed",'course_data':course_data,'error_code':200}
        result_dict = Data_Processor.act_verify(user_input_act)
        
        # 成功
        if result_dict.get('flag') == True: #验证成功
            course_id = str(result_dict.get('course_data').get('course_id'))
            session['course_'+ course_id ] = user_input_act # 设置session
            resp = make_response(redirect(url_for('course_detail',course_id=course_id)))
            resp.set_cookie('course_'+course_id,user_input_act) # 设置cookies
            return resp # 返回response让浏览器重定向Get访问
        # 兑换失败
        flash(u'兑换码错误,请核对后重新输入', 'act_error')
        return render_template("act.html",result_dict=result_dict)




@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# 用户下载课程和密码txt
@app.route('/get_course_txt/<int:course_id>')
def get_course_txt(course_id):
    
    content = "long text \ntest"

    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=passwd.txt"
    return response

    


