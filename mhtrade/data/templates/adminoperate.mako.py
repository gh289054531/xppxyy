# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381506553.828216
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/adminoperate.mako'
_template_uri='adminoperate.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>Insert title here</title>\n</head>\n<body>\n\u7ba1\u7406\u5458\u767b\u5f55\u6210\u529f!\n<br>\n<a href="/index/adminlogout">[\u9000\u51fa]</a>\n<br>\n')
        # SOURCE LINE 12
        __M_writer(escape(session['username']))
        __M_writer(u'\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


