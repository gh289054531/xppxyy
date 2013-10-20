# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382269425.036645
_template_filename='/home/choice/xppxyy/mhtrade/mhtrade/templates/index.mako'
_template_uri='index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>\u68a6\u5e7b\u4ea4\u6613\u7cfb\u7edf</title>\n<script src="../index.js">\n<link href="../index.css" rel="stylesheet" type="text/css" />\n</script>\n\n</head>\n<body>\n\n<div style="width:600px; margin:0 auto;text-align:center">\n\n\t<table style="width:600px; text-align:center" border="1">\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td onclick="ChooseBigServer(this)">\u5e7f\u4e1c1\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td>\u5e7f\u4e1c2\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td onclick="ChooseBigServer(this)">\u5e7f\u4e1c3\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td>\u5e7f\u4e1c4\u533a</td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\t\t<tr style="height:50px">\n\t\t\t<td></td>\n\t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n \t\t\t<td></td>\n\t\t</tr>\n\n\t</table>\n\t<br/>\n\n\t<table  style="width:560px; text-align:center" border="1">\n\t\t')
        # SOURCE LINE 111

        count=0
                        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 113
        __M_writer(u'\n')
        # SOURCE LINE 114
        if hasattr(c,'servernames'):
            # SOURCE LINE 115
            for servername in c.servernames:
                # SOURCE LINE 116
                if count==0:
                    # SOURCE LINE 117
                    __M_writer(u'\t\t\t\t\t<tr style="height:50px;">\n')
                    pass
                # SOURCE LINE 119
                __M_writer(u'\t\t\t\t<td onclick="ChooseServer(this)">')
                __M_writer(escape(servername))
                __M_writer(u'</td>\n')
                # SOURCE LINE 120
                if count==6 or count==len(c.servernames)-1:
                    # SOURCE LINE 121
                    __M_writer(u'\t\t\t\t\t</tr>\n')
                    pass
                # SOURCE LINE 123
                if count==6:
                    # SOURCE LINE 124
                    __M_writer(u'\t\t\t\t\t')

                    count=0
                                                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 126
                    __M_writer(u'\n')
                    # SOURCE LINE 127
                else:
                    # SOURCE LINE 128
                    __M_writer(u'\t\t\t\t\t')

                    count=count+1;
                                                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 130
                    __M_writer(u'\n')
                    pass
                pass
            pass
        # SOURCE LINE 134
        __M_writer(u'\t</table>\n\t\n\t<form action="/index/choosebigserver" method="post" id="form1">\n\t\t<input id="bigservername" type="hidden" name="bigservername" />\n\t</form>\n\t\n\t<form action="/index/chooseserver" method="post" id="form2">\n\t\t<input id="servername" type="hidden" name="servername" />\n\t</form>\n</div>\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


