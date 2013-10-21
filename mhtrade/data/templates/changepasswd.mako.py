# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382370162.515801
_template_filename='/home/choice/xppxyy/mhtrade/mhtrade/templates/changepasswd.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u767b\u5f55\u6210\u529f</title>\n</head>\n<body>\n\n<br/>\n<p>')
        # SOURCE LINE 10
        __M_writer(escape(c.username))
        __M_writer(u' \u4f60\u597d</p>\n\n<form action="/userRegister/haschanged" method="post">\n\t\u8f93 \u5165 \u65b0 \u5bc6 \u7801: <input type="password" name="newpasswd"/>\n\t\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801\uff1a<input type="password" name="newpasswdrepeat"/>\n\t<input type="submit" value="\u786e\u5b9a">\n</from>\n\n<p>\n')
        # SOURCE LINE 19
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 20
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'</p>\n\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


