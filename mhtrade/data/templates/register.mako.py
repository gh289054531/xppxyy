# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382628324.131783
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/register.mako'
_template_uri='register.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u7528\u6237\u6ce8\u518c</title>\n<script src="../base64.js"></script>\n<script type="text/javascript">\nfunction encrypw(){\n\tvar pw=document.getElementById("pw");\n\tvar pwtext=pw.value;\n\tpw.value=base64encode(pwtext);\n\tconsole.log(pw.value)\n\tvar repw=document.getElementById("repw");\n\tvar pwtext=repw.value;\n\trepw.value=base64encode(pwtext);\n\tconsole.log(repw.value)\n\treturn true;\n}\n</script>\n</head>\n<body>\n')
        # SOURCE LINE 22
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\t\n\t<table style="width: 600px; margin: 0 auto; text-align: center;">\n\t\t<form action="/userRegister/doregister" method="post">\n\t\t\t<tr>\n\t\t\t\t<td>\u7528\u6237\u540d\uff1a</td>\n\t\t\t\t<td><input type="text" name="username"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u5bc6\u7801\uff1a</td>\n\t\t\t\t<td><input id="pw" type="password" name="password"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u5bc6\u7801\u786e\u8ba4\uff1a</td>\n\t\t\t\t<td><input id="repw" type="password" name="repassword"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>QQ\uff1a</td>\n\t\t\t\t<td><input type="text" name="qq"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u90ae\u7bb1\uff1a</td>\n\t\t\t\t<td><input type="text" name="email"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\u4e2a\u6027\u7b7e\u540d\uff1a</td>\n\t\t\t\t<td><input type="text" name="selfIntroduction"></input></td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td><input type="submit" value="\u6ce8\u518c" onclick="return encrypw()"></input></td>\n\t\t\t</tr>\n\t\t</form>\n\t</table>\n\t<p>\n')
        # SOURCE LINE 55
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 56
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 58
        __M_writer(u'</p>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


