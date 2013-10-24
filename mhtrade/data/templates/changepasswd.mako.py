# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382626469.089615
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/changepasswd.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u767b\u5f55\u6210\u529f</title>\n<script src="../base64.js"></script>\n<script type="text/javascript">\nfunction encrypw(){\n\tvar oldpasswd=document.getElementById("oldpasswd");\n\tvar text=oldpasswd.value;\n\toldpasswd.value=base64encode(text);\n\t\n\tvar newpasswd=document.getElementById("newpasswd");\n\tvar text=newpasswd.value;\n\tnewpasswd.value=base64encode(text);\n\t\n\tvar newpasswdrepeat=document.getElementById("newpasswdrepeat");\n\tvar text=newpasswdrepeat.value;\n\tnewpasswdrepeat.value=base64encode(text);\n\t\n\treturn true;\n}\n</script>\n</head>\n<body>\n\n<br/>\n')
        # SOURCE LINE 28
        runtime._include_file(context, u'headbar.mako', _template_uri)
        __M_writer(u'\n\n<table style="width:600px;margin:0 auto;text-align:center;">\n<form action="/userRegister/haschanged" method="post">\n\t<tr>\n\t<td>\u8f93 \u5165 \u65e7 \u5bc6 \u7801: </td>\n\t<td><input id="oldpasswd" type="password" name="oldpasswd"/></td>\n\t</tr>\n\t<tr>\n\t<td>\u8f93 \u5165 \u65b0 \u5bc6 \u7801: </td>\n\t<td><input id="newpasswd" type="password" name="newpasswd"/></td>\n\t</tr>\n\t<tr>\n\t<td>\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801\uff1a</td>\n\t<td><input id="newpasswdrepeat" type="password" name="newpasswdrepeat"/></td>\n\t</tr>\n\t<tr>\n\t<td><input type="submit" value="\u786e\u5b9a" onclick="return encrypw()"></td>\n\t</tr>\n</from>\n</table>\n<p>\n')
        # SOURCE LINE 50
        if hasattr(c,"errorMsg") :
            # SOURCE LINE 51
            __M_writer(u'\t\t')
            __M_writer(escape(c.errorMsg))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 53
        __M_writer(u'</p>\n</form>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


