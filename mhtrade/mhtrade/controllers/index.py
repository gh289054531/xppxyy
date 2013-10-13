#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons import app_globals as g
from pylons.controllers.util import abort, redirect

from mhtrade.lib.base import BaseController, render

import MySQLdb

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def index1(self):
        # Return a rendered template
        #return render('/index.mako')
        # or, return a string
        return render('/index.mako')
    def ChooseBigServer(self):
        bigservername=request.params["bigservername"]
        #request.POST["AA"]
       # request.GET["BB"]
        return 
    
    #管理员登录时输入url：/index/indexadmin
    def indexadmin(self):
        return render("adminlogin.mako")
    
    #处理管理员登录的逻辑代码
    def adminlogin(self):
        username=session.get("username","NULL")
        if username=="NULL":
            adminid=request.params.get("adminid","NULL")
            adminpw=request.params.get("adminpw","NULL")
            #如果有恶意用户。他们不通过表达访问这个函数而是直接输入url访问。则跳转到登录页。
            if adminid=="NULL" or adminpw=="NULL":
                c.errorMsg="heike"
                return render("adminlogin.mako")
            #如果用户名密码不对，则提示错误，返回登录页面
            if adminid!="xpplovexyy" or adminpw!="xpplovexyy":
                c.errorMsg="error"
                return render("adminlogin.mako")
            #用户名密码都正确，往session里面写入用户名和用户等级
            else :
                 session['username']=adminid
                 session['level']='admin'
                 session.save()
        return render("adminoperate.mako")
    
    def adminlogout(self):
        session.delete()
        return render("adminlogin.mako")
	
