# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382629268.990296
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/userlogin.mako'
_template_uri='userlogin.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u7528\u6237\u767b\u5f55</title>\n<script src="../base64.js"></script>\n<script type="text/javascript">\nfunction encrypw(){\n\tvar pw=document.getElementById("pw");\n\tvar pwtext=pw.value;\n\tpw.value=base64encode(pwtext);\n\treturn true;\n}\n</script>\n</head>\n<body>\n')
        # SOURCE LINE 17
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n<p>\u5982\u679c\u60a8\u662f\u4e70\u5bb6\uff0c\u8bf7\u76f4\u63a5\u8fdb\u5165\u5546\u54c1\u754c\u9762\u65e0\u9700\u767b\u5f55;\u5982\u679c\u60a8\u662f\u5356\u5bb6\uff0c\u9700\u8981\u767b\u5f55\u540e\u624d\u80fd\u51fa\u552e\u7269\u54c1\u3002</p>\n<a href="">\u4e70\u5bb6\u8bf7\u70b9\u51fb</a>\n<br/>\n<hr/>\n<br/>\n<p>\u5356\u5bb6\u8bf7\u8f93\u5165\u767b\u5f55\u4fe1\u606f:</p>\n<p>\u5982\u679c\u60a8\u6ca1\u6709\u5e10\u53f7\uff0c\u8bf7\u70b9\u51fb<a href="/userRegister/register">[\u6ce8\u518c]</a></p>\n<p><a href="/userRegister/findpasswd">[\u5fd8\u8bb0\u5bc6\u7801]</a></p>\n<form action="/index/userlogin" method="post">\n\t\u7528\u6237\u540d\uff1a<input type="text" name="username"/>\n\t\u5bc6\u7801\uff1a<input id="pw" type="password" name="password"/>\n\t<input type="submit" value="\u767b\u5f55\u670d\u52a1\u5668" onclick="return encrypw()" />\n</form>\n<p>\n')
        # SOURCE LINE 32
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 33
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'</p>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


