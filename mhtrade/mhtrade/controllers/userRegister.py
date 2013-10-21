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
reload(sys)
sys.setdefaultencoding('utf-8')
log = logging.getLogger(__name__)

class UserregisterController(BaseController):
    
    class RegisterForm(formencode.Schema):
        allow_extra_fields = True
        filter_extra_fields = True
        username = formencode.validators.String(not_empty=True, min=6, max=30, messages={'tooShort':"用户名长度在6-30之间", 'tooLong':"用户名长度在6-30之间", 'empty':'请输入用户名'})
        password = formencode.validators.String(not_empty=True, min=6, max=30, messages={'tooShort':"密码长度在6-30之间", 'tooLong':"密码长度在6-30之间", 'empty':'请输入密码'})
        repassword = formencode.validators.String(not_empty=True, min=6, max=30, messages={'tooShort':"密码长度在6-30之间", 'tooLong':"密码长度在6-30之间", 'empty':'请输入密码'})
        chained_validators = [formencode.validators.FieldsMatch('password', 'repassword', messages={'invalidNoMatch':"密码输入不一致"})]
        qq = formencode.validators.Regex(r'^[0-9]{4,15}$', messages={'invalid':"QQ输入不合法"})
        email = formencode.validators.Email(not_empty=True, min=0, max=50, messages={ 'empty':'请输入密码', 'badDomian':"格式错误", 'noAt':"格式错误", 'badType':"格式错误", 'badUsername':"格式错误", 'domainDoesNotExist':"格式错误"})
        selfIntroduction = formencode.validators.String(min=0, max=100, messages={'tooShort':"用户名长度在6-30之间", 'tooLong':"用户名长度在6-30之间"})


    def register(self):
        print 1;
        return render("register.html")
    
    @restrict('POST')
    @validate(schema=RegisterForm(), form='register')
    def doregister(self):
        username = request.params.get('username')
        password = request.params.get("password")
        password = base64.encodestring(password)
        qq = request.params.get("qq")
        email = request.params.get("email")
        selfIntroduction = request.params.get("selfIntroduction")
        print username, password, selfIntroduction
        code = random.randint(100, 1000000)
        encrycode = base64.encodestring(str(code))
        url = 'http://localhost:5000/userRegister/registerComfirmEmail?' + urllib.urlencode({'username':username, 'code':encrycode})
        sendmail({'name':"smtp.qq.com", 'user':'289054531', 'passwd':'pstar910131'}, '289054531@qq.com', [email], '梦幻交易系统用户注册验证', '请点击链接完成注册: ' + url)
        con = None
        try:
            con = MySQLdb.connect(host=g.dbhost, user=g.dbuser, passwd=g.dbpasswd, db=g.dbdb, port=g.dbport, charset="utf8")
            cur = con.cursor();
            cur.execute("insert into users(username,password,QQ,self_introduction,email,level,code) values (%s,%s,%s,%s,%s,%s,%s)", (username, password, qq, selfIntroduction, email, 'user', code))
            con.commit()
        except MySQLdb.Error, e:
            print "Mysql error %d:%s" % (e.args[0], e.args[1])
            c.errorMsg = "数据库写入信息出错"
        finally:
            if con != None:
                con.close()
        return
    
    def registerComfirmEmail(self):
        username = request.params.get('username')
        code = base64.decodestring(request.params.get('code'))
        print code
        print type(code)
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
        return
    
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

    
