<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
	</p>
<form action="/index/adminlogin" method="post">
	管理员帐号：<input type="text" name="adminid" />
	密码：<input type="password" name="adminpw" />
	<input type="submit" value="登录" />
</form>
</body>
</html>