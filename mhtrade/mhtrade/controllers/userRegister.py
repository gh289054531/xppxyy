#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mhtrade.lib.base import BaseController, render
import formencode
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import sys
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
    

    