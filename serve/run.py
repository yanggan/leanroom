# !/usr/bin/python
# coding:utf-8
from flask import Flask,request,render_template
from flask_restful import Resource, Api, abort, reqparse
from config.config import config # 引入字典


def create_app():  
    app=Flask(__name__)  
    app.config.from_object(config["default"])  

    return app  


app = create_app()


# 路由管理
# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("course.html")

@app.route('/course')
def course():
    return render_template("course.html")


# 课程详情页
@app.route('/course/<int:course_id>')
def course_detail(course_id):
    # 生成数据

    # 返回给
    return render_template("course_detail.html",course_id=course_id)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__=='__main__':
    app.run(debug=app.config['DEBUG'])

