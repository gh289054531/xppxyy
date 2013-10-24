<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%include file="headbar.mako"/>
管理员登录成功!${session['username']}
<br>
<a href="/index/adminlogout">[退出]</a>
<br>
<div>
	<form action="/adminop/addserver" method="post">
		大区名：<input type="text" name="bigservername" />
		区名：<input type="text" name="servername" />
		<input type="submit" value="添加区信息" />
	</form>
	%if hasattr(c,"errorMsg"):
		${c.errorMsg}
	%endif
</div>

<a>
</body>
</html>