# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382451770.481152
_template_filename=u'/home/pstar/xppxyy/mhtrade/mhtrade/templates/headbar.html'
_template_uri=u'/headbar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        username = context.get('username', UNDEFINED)
        c = context.get('c', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<table>\n\t<tr>\n\t\t<td>\n')
        # SOURCE LINE 4
        if hasattr(c,username): 
            # SOURCE LINE 5
            __M_writer(u'\t\t\t\t<a href="/index/userlogin">[\u767b\u5f55]</a>\n')
            # SOURCE LINE 6
        else: 
            # SOURCE LINE 7
            __M_writer(u'\t\t\t\t<a href="/index/userlogout">[\u9000\u51fa]</a> \n')
            pass
        # SOURCE LINE 9
        __M_writer(u'\t\t</td>\n')
        # SOURCE LINE 10
        if hasattr(c,username):
            # SOURCE LINE 11
            __M_writer(u'\t\t\t\t<td><a href="/userRegister/changepasswd">[\u4fee\u6539\u5bc6\u7801]</a></td>\n')
            pass
        # SOURCE LINE 13
        __M_writer(u'\t\t<td><a href="/userRegister/register" target="_blank">[\u6ce8\u518c]</a></td>\n\t\t<td><a href="">[\u627e\u56de\u5bc6\u7801]</a></td>\n\t\t<td><a href="/index/index">[\u9009\u62e9\u670d\u52a1\u5668]</a></td>\n\t\t<td><a href="">[\u4ea4\u6613\u754c\u9762]</a></td>\n\t</tr>\n\n</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


