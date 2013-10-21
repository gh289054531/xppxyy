#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons import app_globals as g
from pylons.controllers.util import abort, redirect

from mhtrade.lib.base import BaseController, render

import MySQLdb
import base64

log = logging.getLogger(__name__)

class IndexController(BaseController):

	def index(self):
		# Return a rendered template
		#return render('/index.mako')
		# or, return a string
		return render('/index.mako')

	def choosebigserver(self):
		bigservername=request.params["bigservername"]
		con=None
		try:
			con=MySQLdb.connect(host=g.dbhost,user=g.dbuser,passwd=g.dbpasswd,db=g.dbdb,port=g.dbport,charset="utf8")
			cur=con.cursor();
			cur.execute("select server_name from servers where big_server_name=%s",(bigservername))
			con.commit()
			rows=cur.fetchall()
			c.servernames=[]
			for row in rows:
				c.servernames.append(row[0])
		except MySQLdb.Error,e:
			print "Mysql error %d:%s"%(e.args[0],e.args[1])
			c.errorMsg="数据库读区信息出错"
		finally:
			if con!=None:
				con.close()
		return render("index.mako")

	def chooseserver(self):
		servername=request.params.get("servername","NULL")
		if servername=="NULL":
			return render("index.mako")
		username=session.get("username","NULL")
		session['server']=servername
		c.servername=servername
		session.save()
		if username!="NULL":
			c.username=username
			return render("usersell.mako")
		return render("userlogin.mako")

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
		if session.get("level", "NULL") == 'admin':
			return render("adminoperate.mako")
		else:
			return "权限不足"

	def adminlogout(self):
		session.delete()
		return render("adminlogin.mako")

	def userlogin(self):
		servername=session.get('server',"NULL")
		print servername
		if servername == "NULL":
			return render("index.mako")
		c.servername=servername
		
		username=session.get('username',"NULL")
		print username
		if username!= "NULL":
			c.username=username
			return render("usersell.mako")
		
		username = request.params.get("username", "NULL")
		password = request.params.get("password", "NULL")
		encrypassword=base64.encodestring(password)
		try:
			con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
			cur = con.cursor()
			cur.execute("select password from users where username = %s", username)
			con.commit()
			row = cur.fetchone()
			try_password=str(row[0])
		except MySQLdb.Error as e:
			print "mysql error %d: %s" %(e.args[0], e.args[1])
			c.errorMsg = "登录校验密码错误"
		finally:
			if con != None:
				con.close()
		if encrypassword == try_password:
			session['username'] = username
			session['level'] = 'user'
			session.save()
			return render("usersell.mako")
		else:
			c.errorMsg = "密码错误"
		return render("userlogin.mako")

	def userlogout(self):
		session.delete()
		return render("index.mako")
