# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382368300.222598
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/register.html'
_template_uri='register.html'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>Insert title here</title>\n</head>\n<body>\n\t\n\t<table style="width: 600px; margin: 0 auto; text-align: center;">\n\t\t<form action="/userRegister/doregister" method="post">\n\t\t\t<tr>\n\t\t\t\t<td>\u7528\u6237\u540d\uff1a</td>\n\t\t\t\t<td><input type="text" name="username"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u5bc6\u7801\uff1a</td>\n\t\t\t\t<td><input type="password" name="password"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u5bc6\u7801\u786e\u8ba4\uff1a</td>\n\t\t\t\t<td><input type="password" name="repassword"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>QQ\uff1a</td>\n\t\t\t\t<td><input type="text" name="qq"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u90ae\u7bb1\uff1a</td>\n\t\t\t\t<td><input type="text" name="email"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u4e2a\u6027\u7b7e\u540d\uff1a</td>\n\t\t\t\t<td><input type="text" name="selfIntroduction"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td><input type="submit" value="\u6ce8\u518c"></input></td>\n\t\t\t</tr>\n\t\t</form>\n\t</table>\n\t<p>\n')
        # SOURCE LINE 41
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 42
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 44
        __M_writer(u'</p>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


