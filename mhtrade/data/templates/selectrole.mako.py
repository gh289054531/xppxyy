# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382459845.475991
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/selectrole.mako'
_template_uri='selectrole.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u8bf7\u9009\u62e9\u4e00\u4e2a\u8eab\u4efd\u767b\u5f55</title>\n</head>\n<body>\n')
        # SOURCE LINE 8
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n<p>\n')
        # SOURCE LINE 10
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 11
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 13
        __M_writer(u'</p>\n\u8fd9\u4e2a\u662f\u9009\u62e9\u89d2\u8272\u7684\u9875\u9762\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


