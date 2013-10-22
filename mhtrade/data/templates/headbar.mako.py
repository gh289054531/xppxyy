# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382459638.08903
_template_filename=u'/home/pstar/xppxyy/mhtrade/mhtrade/templates/headbar.mako'
_template_uri=u'headbar.mako'
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
        __M_writer(u'\n<table style="height:50px;width:100%;text-align:center;">\n\t<tr>\n\t\t<td>\n')
        # SOURCE LINE 5
        if hasattr(c,"username"): 
            # SOURCE LINE 6
            __M_writer(u'\t\t\t\t\u60a8\u597d\uff1a')
            __M_writer(escape(c.username))
            __M_writer(u'!&nbsp;&nbsp;<a href="/index/userlogout">[\u9000\u51fa]</a> \n')
            # SOURCE LINE 7
        else: 
            # SOURCE LINE 8
            __M_writer(u'\t\t\t\t<a href="/index/userloginpage">[\u767b\u5f55]</a>\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'\t\t</td>\n')
        # SOURCE LINE 11
        if hasattr(c,"username"):
            # SOURCE LINE 12
            __M_writer(u'\t\t\t\t<td><a href="/userRegister/changepasswd">[\u4fee\u6539\u5bc6\u7801]</a></td>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\t\t<td><a href="/userRegister/register" target="_blank">[\u6ce8\u518c]</a></td>\n\t\t<td><a href="">[\u627e\u56de\u5bc6\u7801]</a></td>\n\t\t<td><a href="/index/index">[\u9009\u62e9\u670d\u52a1\u5668]</a>\n')
        # SOURCE LINE 17
        if hasattr(c,"servername"):
            # SOURCE LINE 18
            __M_writer(u'\t\t\t\u5f53\u524d\u670d\u52a1\u5668\uff1a')
            __M_writer(escape(c.servername))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 20
        __M_writer(u'\t\t</td>\n\t\t<td><a href="/index/chooserole">[\u9009\u62e9\u89d2\u8272]</a>\n')
        # SOURCE LINE 22
        if hasattr(c,"rolename"):
            # SOURCE LINE 23
            __M_writer(u'\t\t\t\u5f53\u524d\u8eab\u4efd\uff1a')
            __M_writer(escape(c.rolename))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 25
        __M_writer(u'\t\t</td>\n\t\t<td><a href="">[\u4ea4\u6613\u754c\u9762]</a></td>\n\t</tr>\n\n</table>\n<hr />')
        return ''
    finally:
        context.caller_stack._pop_frame()


