# coding:utf-8
from application import app
from flask import Flask,request,render_template,flash,redirect,url_for,session
from flask_restful import Resource, Api, abort, reqparse



# 避免中文传给jinja2时候报错
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 路由管理

from model import *


# 首页
@app.route('/')
@app.route('/index')
@app.route('/course')
@app.route('/course/')
def index():

    return render_template("course.html",course=fake_category)

# @app.route('/course')
# def course():
#     return render_template("course.html")


# 课程详情页
@app.route('/course/<int:course_id>',methods=['POST','GET'])
def course_detail(course_id):

    if request.method == "GET":
        # 2种情况，1、第一次访问，2、输入兑换码后，重定向访问，这时候需要返回带密码页面
        # 判断是有对应cookies和session，然后才返回带密码的数据
        if session.get('key','nokey') != 'nokey':
            pass
            return render_template("course_detail.html",course_data=fake_course_date,passwd_dict=fake_passwd_data)
        else:
            # 第一次访问
            return render_template("course_detail.html",course_data=fake_course_date,passwd_dict=None)
    elif request.method == "POST":
        # 这是个用户输入兑换码后提交到后台来的数据
        # 获取
        x = request.form.get('key', '')
        session['key'] = x
        print x
        flash(x)

        # 返回给
        return redirect(url_for('course_detail',course_id=course_id))

# 通过激活码激活课程
@app.route("/act")
def course_activete():
    # pass
    return render_template('act.html')


@app.route('/test')
def test():
    return render_template('test.html')