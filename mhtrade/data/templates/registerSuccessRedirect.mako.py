# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382458911.370571
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/registerSuccessRedirect.mako'
_template_uri='registerSuccessRedirect.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u8bf7\u786e\u8ba4\u90ae\u4ef6</title>\n</script>\n\n</head>\n<body>\n')
        # SOURCE LINE 10
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n')
        # SOURCE LINE 11
        if hasattr(c,"errorMsg"):
            # SOURCE LINE 12
            __M_writer(u'\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u' \n')
            # SOURCE LINE 13
        else:
            # SOURCE LINE 14
            __M_writer(u'\t<p>\u7cfb\u7edf\u5df2\u7ecf\u5411\u60a8\u7684\u90ae\u7bb1\u53d1\u9001\u4e00\u4efd\u90ae\u4ef6\uff0c\u8bf7\u9a8c\u8bc1\u90ae\u4ef6\u4e2d\u7684\u94fe\u63a5\u4fe1\u606f\u5373\u53ef\u5b8c\u6210\u6ce8\u518c\u3002</p>\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


