# coding:utf-8
from application import app
from flask import Flask,request,render_template,flash,redirect,url_for,session,make_response
from flask_restful import Resource, Api, abort, reqparse


from model import *


# 避免中文传给jinja2时候报错
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



# 这个部分先写方法 
class Course_Man(object):
    """
    1、获取所有课程分类，和分类地下课程
    2、获取单门课程的的信息，包含资源
    3、获取单门课程的


    """
    def __init__(self):
        pass
        
class Act_Man(object):
    """
    1、生成兑换码
    2、查询、修改兑换码
    3、使用兑换码，验证兑换码是否有效

    """
    def __init__(self):
        pass

    def 
    




# 首页
@app.route('/')
@app.route('/index')
@app.route('/course')
@app.route('/course/')
def index():

    return render_template("course.html",course=fake_category)





# 课程详情页
@app.route('/course/<int:course_id>',methods=['POST','GET'])
def course_detail(course_id):

    if request.method == "GET":

        # 2种情况，1、第一次访问，2、输入兑换码后，重定向访问，这时候需要返回带密码页面
        # 1、读取用户的cookies和session，把兑换码拿出来，匹配是否是这门课程的对缓慢
        # 2、如果是这门课程的兑换码，则返回带提取密码数据的页面
        # 3、如果不是，则返回普通的页面
        print request.cookies

        user_cookies = request.cookies


        if session.get('key','nokey') != 'nokey':
            # 用户已经输入了正确的兑换码,判断条件是拿到cookies or session
            pass
            resp = make_response(render_template("course_detail.html",course_data=fake_course_date,passwd_dict=fake_passwd_data))
            # 设置cookies
            # resp.set_cookie('username','the username')
            return resp
        else:
            # 第一次访问
            return render_template("course_detail.html",course_data=fake_course_date,passwd_dict=None)
    elif request.method == "POST":
        # 这是个用户输入兑换码后提交到后台来的数据
        # 1、获取兑换码，判断是否有效，是对应课程的兑换码
        # 2、如果有效，则保持兑换码到用户的cookies
        # 3、把兑换码放到session中
        # 4、返回重定向，让浏览器get访问本链接

        x = request.form.get('key', '')
        session['key'] = x
        print x
        flash(x)

        # 返回时候直接设置cookies
        redirect_to_course = redirect(url_for('course_detail',course_id=course_id))
        resp = make_response(redirect_to_course)
        resp.set_cookie('course_112','code')
        return resp

# 通过激活码激活课程
@app.route("/act")
def course_activete():
    # pass
    return render_template('act.html')


@app.route('/test')
def test():
    return render_template('test.html')