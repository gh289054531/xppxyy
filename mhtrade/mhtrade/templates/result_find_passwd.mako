<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title></title>
</head>
<body>
<%include file="headbar.mako"/>

<form action="/userRegister/if_findpasswd" method="post">
	输 入 新 密 码: <input type="password" name="newpasswd"/>
	再次输入新密码：<input type="password" name="newpasswdrepeat"/>
	<input type="hidden" name="username" value=${c.username} />
	<input type="submit" value="确定">
</from>

<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>

</form>
</body>
</html>
