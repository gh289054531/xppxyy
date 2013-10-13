# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381676490.479855
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
        c = context.get('c', UNDEFINED)
        session = context.get('session', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>Insert title here</title>\n</head>\n<body>\n\u7ba1\u7406\u5458\u767b\u5f55\u6210\u529f!')
        # SOURCE LINE 8
        __M_writer(escape(session['username']))
        __M_writer(u'\n<br>\n<a href="/index/adminlogout">[\u9000\u51fa]</a>\n<br>\n<div>\n\t<form action="/adminop/addserver" method="post">\n\t\t\u5927\u533a\u540d\uff1a<input type="text" name="bigservername" />\n\t\t\u533a\u540d\uff1a<input type="text" name="servername" />\n\t\t<input type="submit" value="\u6dfb\u52a0\u533a\u4fe1\u606f" />\n\t</form>\n')
        # SOURCE LINE 18
        if hasattr(c,"errorMsg"):
            # SOURCE LINE 19
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 21
        __M_writer(u'</div>\n\n<a>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


