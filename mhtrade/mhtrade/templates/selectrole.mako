<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>请选择一个身份登录</title>
</head>
<body>
<%include file="headbar.mako"/>
<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>
这个是选择角色的页面
</body>
</html>