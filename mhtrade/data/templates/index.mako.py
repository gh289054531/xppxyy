# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381420131.450291
_template_filename='/home/pstar/xppxyy/mhtrade/mhtrade/templates/index.mako'
_template_uri='/index.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u68a6\u5e7b\u4ea4\u6613\u7cfb\u7edf</title>\n<script src="../index.js">\n</script>\n\n</head>\n<body>\n\n<div style="width:600px; margin:0 auto">\n\n\t<table style="width:600px; text-align:center" border="1">\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td >\u5e7f\u4e1c1\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td>\u5e7f\u4e1c2\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td onclick="ChooseBigServer(this)">\u5e7f\u4e1c3\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td>\u5e7f\u4e1c4\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\n\t</table>\n\t<br/>\n\n\t<table  style="width:600px; text-align:center" border="1">\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t</table>\n\t\n\t<form action="/index/choosebigserver" method="post" id="form1">\n\t\t<input id="bigservername" type="hidden" name="bigservername" />\n\t</form>\n</div>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


