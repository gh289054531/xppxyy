#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals as g

from mhtrade.lib.base import BaseController, render
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

log = logging.getLogger(__name__)

class AdminopController(BaseController):

    def addserver(self):
        level=session.get("level","NULL")
        if level=="NULL" :
            c.errorMsg="未登录"
            return render("adminlogin.mako")
        if level=="common":
            c.errorMsg="权限不足"
            return render("adminlogin.mako")#待修改
        if level=="admin":
            bigservername=request.params.get("bigservername","NULL")
            servername=request.params.get("servername","NULL")
            if bigservername=="NULL" or servername=="NULL" or bigservername=="" or servername=="":
                c.errorMsg="输入的区信息错误"
                return render("adminoperate.mako")
            con=None
            try:
                con=MySQLdb.connect(host=g.dbhost,user=g.dbuser,passwd=g.dbpasswd,db=g.dbdb,port=g.dbport,charset="utf8")
                cur=con.cursor();
                cur.execute("insert into servers(big_server_name,server_name) values(%s,%s)",(bigservername,servername))
                con.commit()
            except MySQLdb.Error,e:
                print "Mysql error %d:%s"%(e.args[0],e.args[1])
                c.errorMsg="数据库插入区信息出错"
            finally:
                if con!=None:
                    con.close()
                
        return render("adminoperate.mako")
