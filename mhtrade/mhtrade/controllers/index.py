#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
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
        bigservername=request.POST["bigservername"]
        return 
    
    def indexadmin(self):
        return render("adminlogin.mako")
        
    def adminlogin(self):
        username=session.get("username","NULL")
        if username=="NULL":
            adminid=request.params.get("adminid","NULL")
            adminpw=request.params.get("adminpw","NULL")
            if adminid=="NULL" or adminpw=="NULL":
                return render("adminlogin.mako")
            if adminid!="xpplovexyy" or adminpw!="xpplovexyy":
                c.errorMsg="error"
                return render("adminlogin.mako")
            else :
                 session['username']=adminid
                 session['level']='admin'
                 session.save()
        return render("adminoperate.mako")
    
    def adminlogout(self):
        session.delete()
        return render("adminlogin.mako")
	
