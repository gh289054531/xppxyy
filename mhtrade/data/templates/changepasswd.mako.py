# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382460606.03233
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/changepasswd.mako'
_template_uri='changepasswd.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u767b\u5f55\u6210\u529f</title>\n</head>\n<body>\n\n<br/>\n')
        # SOURCE LINE 10
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n\n<table style="width:600px;margin:0 auto;text-align:center;">\n<form action="/userRegister/haschanged" method="post">\n\t<tr>\n\t<td>\u8f93 \u5165 \u65e7 \u5bc6 \u7801: </td>\n\t<td><input type="password" name="oldpasswd"/></td>\n\t</tr>\n\t<tr>\n\t<td>\u8f93 \u5165 \u65b0 \u5bc6 \u7801: </td>\n\t<td><input type="password" name="newpasswd"/></td>\n\t</tr>\n\t<tr>\n\t<td>\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801\uff1a</td>\n\t<td><input type="password" name="newpasswdrepeat"/></td>\n\t</tr>\n\t<tr>\n\t<td><input type="submit" value="\u786e\u5b9a"></td>\n\t</tr>\n</from>\n</table>\n<p>\n')
        # SOURCE LINE 32
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 33
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'</p>\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


