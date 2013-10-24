# coding=utf-8
import logging
import base64
import urllib
import MySQLdb
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals as g
from mhtrade.lib.base import BaseController, render
import formencode
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import random
import sys
import MySQLdb
from pylons import app_globals as g

reload(sys)
sys.setdefaultencoding('utf-8')
log = logging.getLogger(__name__)

class UserregisterController(BaseController):
    
    class RegisterForm(formencode.Schema):
        allow_extra_fields = True
        filter_extra_fields = True
        username = formencode.validators.String(not_empty=True, min=6, max=30, messages={'tooShort':"用户名长度在6-30之间", 'tooLong':"用户名长度在6-30之间", 'empty':'请输入用户名'})
        password = formencode.validators.String(not_empty=True,messages={ 'empty':'请输入密码'})
        repassword = formencode.validators.String(not_empty=True, messages={'empty':'请输入密码'})
        chained_validators = [formencode.validators.FieldsMatch('password', 'repassword', messages={'invalidNoMatch':"密码输入不一致"})]
        qq = formencode.validators.Regex(r'^[0-9]{4,15}$', messages={'invalid':"QQ输入不合法"})
        email = formencode.validators.Email(not_empty=True, min=0, max=50, messages={ 'empty':'请输入密码', 'badDomian':"格式错误", 'noAt':"格式错误", 'badType':"格式错误", 'badUsername':"格式错误", 'domainDoesNotExist':"格式错误"})
        selfIntroduction = formencode.validators.String(min=0, max=100, messages={'tooShort':"用户名长度在6-30之间", 'tooLong':"用户名长度在6-30之间"})


    def register(self):
        servername = session.get('servername', "NULL")
        username = session.get('username', "NULL")
        if servername!="NULL":
            c.servername = servername
        if username!="NULL":
            c.username=username
        return render("register.mako")
    
    @restrict('POST')
    @validate(schema=RegisterForm(), form='register')
    def doregister(self):
        con = None
        con = MySQLdb.connect(host=g.dbhost, user=g.dbuser, passwd=g.dbpasswd, db=g.dbdb, port=g.dbport, charset="utf8")
        cur = con.cursor();
        try:
            username = request.params.get('username',"NULL")
            password = request.params.get("password")
            print password
            originpassword=base64.decodestring(password)
            print originpassword    
            if len(originpassword)<6 or len(originpassword)>30:
                c.errorMsg="密码长度必须在6-30之间"
                return render("register.mako")
            qq = request.params.get("qq")
            email = request.params.get("email")
            selfIntroduction = request.params.get("selfIntroduction")
            code = random.randint(100, 1000000)
            encrycode = base64.encodestring(str(code))
            url = 'http://localhost:5000/userRegister/registerComfirmEmail?' + urllib.urlencode({'username':username, 'code':encrycode})
            sendmail({'name':"smtp.qq.com", 'user':'289054531', 'passwd':'pstar910131'}, '289054531@qq.com', [email], '梦幻交易系统用户注册验证', '请点击链接完成注册: <a href="' + url+'"></a>,如果无法点击请复制到浏览器地址栏访问即可。')
            cur.execute("insert into users(username,password,QQ,self_introduction,email,level,code) values (%s,%s,%s,%s,%s,%s,%s)", (username, password, qq, selfIntroduction, email, 'user', code))
            con.commit()
        except MySQLdb.Error, e:
            print "Mysql error %d:%s" % (e.args[0], e.args[1])
            c.errorMsg = "插入数据出错，很可能是用户名重复"
        finally:
            if con != None:
                con.close()
        return render("registerSuccessRedirect.mako")
    
    def registerComfirmEmail(self):
        username = request.params.get('username')
        code = base64.decodestring(request.params.get('code'))
        con = None
        try:
            con = MySQLdb.connect(host=g.dbhost, user=g.dbuser, passwd=g.dbpasswd, db=g.dbdb, port=g.dbport, charset="utf8")
            cur = con.cursor();
            cur.execute("select code from users where username= %s", (username))
            con.commit()
            row= cur.fetchone()
            codeInDB = str(row[0])
            print codeInDB
            print type(codeInDB)
            if codeInDB != code:
                return "激活错误"
            cur.execute("update users set code=%s where username=%s", (0, username))
            con.commit()
        except MySQLdb.Error, e:
            print "Mysql error %d:%s" % (e.args[0], e.args[1])
            c.errorMsg = "激活错误"
        finally:
            if con != None:
                con.close()
        return render("index.mako")

    def changepasswd(self):
        servername = session.get('servername', "NULL")
        username = session.get('username', "NULL")
        if servername!="NULL":
            c.servername = servername
        if username!="NULL":
            c.username=username
        if username=="NULL":
            return render("userlogin.mako")
        return render("changepasswd.mako")
	
    def haschanged(self):
        servername = session.get('servername', "NULL")
        username = session.get('username', "NULL")
        if servername!="NULL":
            c.servername = servername
        if username!="NULL":
            c.username=username
        if username=="NULL":
            return render("userlogin.mako")
        oldpasswd=request.params.get("oldpasswd")
        newpasswd=request.params.get('newpasswd')
        newpasswdrepeat=request.params.get('newpasswdrepeat')
        if len(base64.decodestring(newpasswd))<6 or len(base64.decodestring(newpasswd))>64:
            c.errorMsg="密码长度必须在6-64之间"
            return render("changepasswd.mako")
        if newpasswd != newpasswdrepeat:
            c.errorMsg = "两次输入密码不相同，请重新输入"
            return render("changepasswd.mako")
        try:        
            con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
            cur = con.cursor()
            cur.execute("select password from users where username =%s", (username))
            con.commit()
            passwordInDB=cur.fetchone()[0]
        except MySQLdb.Error as e:
            print "mysql error %d: %s" %(e.args[0], e.args[1])
            c.errorMsg = "从数据库读密码错误"
        finally:
            if con != None:
                con.close()
        if str(oldpasswd).strip()!=str(passwordInDB).strip():
            c.errorMsg="旧密码错误"
            return render("changepasswd.mako")
        try:        
            con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
            cur = con.cursor()
            cur.execute("update users set password=%s where username =%s", (newpasswd,username))
            con.commit()
        except MySQLdb.Error as e:
            print "mysql error %d: %s" %(e.args[0], e.args[1])
            c.errorMsg = "往数据库插入新密码错误"
        finally:
			if con != None:
				con.close()
        return render("index.mako")
    
    def findpasswd(self):
        servername = session.get('servername', "NULL")
        if servername != "NULL":
            c.servername = servername
        username = session.get('username', "NULL")
        if username != "NULL":
            c.username=username
        return render("findpasswd.mako")
    
    def findpasswd_sendmail(self):
        servername = session.get('servername', "NULL")
        if servername != "NULL":
            c.servername = servername
        username = session.get('username', "NULL")
        if username != "NULL":
            c.username=username
        username = request.params.get('username')
        try:        
            con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
            cur = con.cursor()
            cur.execute("select count(*) from users where username =%s", (username))
            con.commit()
            count=cur.fetchone()[0]
            if count==0:
                c.errorMsg="用户名不存在"
        except MySQLdb.Error as e:
            print "mysql error %d: %s" %(e.args[0], e.args[1])
            c.errorMsg = "从数据库读密码错误"
        finally:
            if con != None:
                con.close()
        if hasattr(c,"errorMsg"):
            return render("findpasswd.mako")
        try:
            con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
            cur = con.cursor()
            cur.execute("select email from users where username = %s", username)
            con.commit()
            row = cur.fetchone()
            email = row[0]
        except MySQLdb.Error as e:
            print "mysql error %d: %s" %(e.args[0], e.args[1])
            e.errorMsg = "查询用户对应邮箱出错"
        finally:
            if con != None:
                con.close()
        code = random.randint(100, 1000000)
        encrycode = base64.encodestring(str(code))
        url = 'http://localhost:5000/userRegister/find_change_passwd?' + urllib.urlencode({'username':username, 'code':encrycode})
        sendmail({'name':"smtp.qq.com", 'user':'289054531', 'passwd':'pstar910131'}, '289054531@qq.com', [email], '梦幻交易系统找回密码', '请点击链接重设密码: ' + url)
        return render("hassendemail.mako")
        
    def find_change_passwd(self):
        username = request.params.get('username')
        if username=="NULL":
            return "修改密码失败，请不要改动向您邮箱发送的网址。"
        c.username = username
        return render("result_find_passwd.mako")

    def if_findpasswd(self):
        servername = session.get('servername', "NULL")
        username = session.get('username', "NULL")
        if servername!="NULL":
            c.servername = servername
        if username!="NULL":
            c.username=username
        username = request.params.get('username')
        newpasswd=request.params.get('newpasswd')
        newpasswdrepeat=request.params.get('newpasswdrepeat')
        if newpasswd != newpasswdrepeat:
            c.errorMsg = "两次输入密码不相同，请重新输入"
            return render("result_find_passwd.mako")
        if len(base64.decodestring(newpasswd))<6 or len(base64.decodestring(newpasswd))>64:
            c.errorMsg="密码长度必须在6-64之间"
            return render("result_find_passwd.mako")
        try:        
            con = MySQLdb.connect(host = g.dbhost, user = g.dbuser, passwd = g.dbpasswd, db = g.dbdb, port = g.dbport, charset = "utf8")
            cur = con.cursor()
            cur.execute("update users set password=%s where username =%s", (newpasswd,username))
            con.commit()
        except MySQLdb.Error as e:
            print "mysql error %d: %s" %(e.args[0], e.args[1])
            c.errorMsg = "往数据库插入新密码错误"
        finally:
			if con != None:
				con.close()
        return render("index.mako")
       

def sendmail(server, fro, to, subject, text):
    assert type(server) == dict 
    assert type(to) == list 
    msg = MIMEMultipart() 
    msg['From'] = fro 
    msg['Subject'] = subject 
    msg['To'] = COMMASPACE.join(to)  # COMMASPACE==', ' 
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text)) 
    import smtplib 
    smtp = smtplib.SMTP(server['name']) 
    smtp.login(server['user'], server['passwd']) 
    smtp.sendmail(fro, to, msg.as_string()) 
    smtp.close()

