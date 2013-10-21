#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mhtrade.lib.base import BaseController, render
import formencode
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import sys
import MySQLdb
from pylons import app_globals as g

reload(sys)
sys.setdefaultencoding('utf-8')
log = logging.getLogger(__name__)

class UserregisterController(BaseController):
    
    class RegisterForm(formencode.Schema):
        allow_extra_fields=True
        filter_extra_fields=True
        username=formencode.validators.String(not_empty=True,min=6,max=30,messages={'tooShort':"用户名长度在6-30之间",'tooLong':"用户名长度在6-30之间",'empty':'请输入用户名'})
        password=formencode.validators.String(not_empty=True,min=6,max=30,messages={'tooShort':"密码长度在6-30之间",'tooLong':"密码长度在6-30之间",'empty':'请输入密码'})
        repassword=formencode.validators.String(not_empty=True,min=6,max=30,messages={'tooShort':"密码长度在6-30之间",'tooLong':"密码长度在6-30之间",'empty':'请输入密码'})
        chained_validators=[formencode.validators.FieldsMatch('password','repassword',messages={'invalidNoMatch':"密码输入不一致"})]
        qq=formencode.validators.Regex(r'^[0-9]{4,15}$',messages={'invalid':"QQ输入不合法"})
        email=formencode.validators.Email(min=0,max=50,messages={'badDomian':"格式错误",'noAt':"格式错误",'badType':"格式错误",'badUsername':"格式错误",'domainDoesNotExist':"格式错误"})
        selfIntroduction=formencode.validators.String(min=0,max=100,messages={'tooShort':"用户名长度在6-30之间",'tooLong':"用户名长度在6-30之间"})


    def register(self):
        print 1;
        return render("register.html")
    
    @restrict('POST')
    @validate(schema=RegisterForm(),form='register')
    def doregister(self):
        username=request.params.get('username')
        password=request.params.get("password")
        qq=request.params.get("qq")
        email=request.params.get("email")
        selfIntroduction=request.params.get("selfIntroduction")
        print username,password,selfIntroduction
        return 
    
    def changepasswd(self):
        username = session['username']
        c.username = username
        return render("changepasswd.mako")
	
    def haschanged(self):
        username = session['username']
        c.username = username
        newpasswd=request.params.get('newpasswd')
        newpasswdrepeat=request.params.get('newpasswdrepeat')
        print newpasswd
        if newpasswd != newpasswdrepeat:
            c.errorMsg = "there is difference between this two new password, repeat again"
            return render("changepasswd.mako")
        try:        
            con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
            cur = con.cursor()
            cur.execute("update users set password=%s where username =%s", (newpasswd,username))
            con.commit()
        except MySQLdb.Error as e:
            print "mysql error %d: %s" %(e.args[0], e.args[1])
            c.errorMsg = "an error accour"
        finally:
			if con != None:
				con.close()
        return render("usersell.mako")
    
