# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382456980.267111
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u767b\u5f55\u6210\u529f</title>\n</head>\n<body>\n')
        # SOURCE LINE 8
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n\u8fd9\u662f\u5356\u4e1c\u897f\u7684\u754c\u9762\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


