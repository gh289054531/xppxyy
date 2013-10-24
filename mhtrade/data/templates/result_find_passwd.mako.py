# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382629567.377358
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/result_find_passwd.mako'
_template_uri='result_find_passwd.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u91cd\u8bbe\u5bc6\u7801</title>\n<script src="../base64.js"></script>\n<script type="text/javascript">\nfunction encrypw(){\n\tvar pw=document.getElementById("pw");\n\tvar pwtext=pw.value;\n\tpw.value=base64encode(pwtext);\n\tconsole.log(pw.value)\n\tvar repw=document.getElementById("repw");\n\tvar pwtext=repw.value;\n\trepw.value=base64encode(pwtext);\n\tconsole.log(repw.value)\n\treturn true;\n}\n</script>\n</head>\n<body>\n')
        # SOURCE LINE 22
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n\n<form action="/userRegister/if_findpasswd" method="post">\n\t\u8f93 \u5165 \u65b0 \u5bc6 \u7801: <input id="pw" type="password" name="newpasswd"/>\n\t\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801\uff1a<input id="repw" type="password" name="newpasswdrepeat"/>\n\t<input type="hidden" name="username" value=')
        # SOURCE LINE 27
        __M_writer(escape(c.username))
        __M_writer(u' />\n\t<input type="submit" value="\u786e\u5b9a" onclick="return encrypw()">\n</from>\n\n<p>\n')
        # SOURCE LINE 32
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 33
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'</p>\n\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


