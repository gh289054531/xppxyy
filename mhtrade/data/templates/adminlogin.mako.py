# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381756434.108345
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/adminlogin.mako'
_template_uri='adminlogin.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>Insert title here</title>\n</head>\n<body>\n\t<p>\n')
        # SOURCE LINE 9
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 10
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 12
        __M_writer(u'\t</p>\n<form action="/index/adminlogin" method="post">\n\t\u7ba1\u7406\u5458\u5e10\u53f7\uff1a<input type="text" name="adminid" />\n\t\u5bc6\u7801\uff1a<input type="password" name="adminpw" />\n\t<input type="submit" value="\u767b\u5f55" />\n</form>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


