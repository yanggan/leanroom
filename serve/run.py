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


# # 路由管理
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/print')
def test():

    print type(app.config)
    return "OK"

if __name__=='__main__':
    app.run(debug=app.config['DEBUG'])

