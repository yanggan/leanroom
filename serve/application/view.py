# coding:utf-8
from application import app
from flask import Flask,request,render_template
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
def index():

    return render_template("course.html",course=fake_category)

# @app.route('/course')
# def course():
#     return render_template("course.html")


# 课程详情页
@app.route('/course/<int:course_id>')
def course_detail(course_id):
    # 生成数据

    # 返回给
    return render_template("course_detail.html",course_data=fake_course_date)

# 通过激活码激活课程
@app.route("/act")
def course_activete():
    # pass
    return render_template('act.html')


@app.route('/test')
def test():
    return render_template('test.html')