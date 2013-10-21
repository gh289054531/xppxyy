# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382374794.000756
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/usersell.mako'
_template_uri='usersell.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u767b\u5f55\u6210\u529f</title>\n</head>\n<body>\n\n<br/>\n<p>\n')
        # SOURCE LINE 11
        if hasattr(c,"username"):
            # SOURCE LINE 12
            __M_writer(u'\t')
            __M_writer(escape(c.username))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\u4f60\u597d!\n </p>\n<p>\u767b\u5f55\u6210\u529f\u670d\u52a1\u5668:\n')
        # SOURCE LINE 17
        if hasattr(c,"servername"):
            # SOURCE LINE 18
            __M_writer(u'\t')
            __M_writer(escape(c.servername))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 20
        __M_writer(u'</p>\n\n<p><a href="/userRegister/changepasswd">[\u4fee\u6539\u5bc6\u7801]</a></p>\n\n<p><a href="/index/userlogout">[\u9000\u51fa]</a></p>\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


