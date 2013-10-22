# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382462469.810826
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/hassendemail.mako'
_template_uri='hassendemail.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title></title>\n</head>\n<body>\n\n<br/>\n\n')
        # SOURCE LINE 11
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n<p>\u90ae\u4ef6\u5df2\u53d1\u9001\u81f3\u60a8\u6ce8\u518c\u7684\u90ae\u7bb1\uff0c\u8bf7\u70b9\u51fb\u90ae\u4ef6\u4e2d\u7684\u94fe\u63a5\u5b8c\u6210\u627e\u56de\u5bc6\u7801</p>\n\n<p>\n')
        # SOURCE LINE 15
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 16
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 18
        __M_writer(u'</p>\n\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


