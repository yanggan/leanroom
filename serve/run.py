# !/usr/bin/python
# coding:utf-8
from flask import Flask,request,render_template
from flask_restful import Resource, Api, abort, reqparse




app = Flask(__name__)

# # 路由管理
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")



if __name__=='__main__':
    app.run(debug=True)

