<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>找回密码</title>
</head>
<body>

<br/>
<%include file="headbar.mako"/>

<form action="/userRegister/findpasswd_sendmail" method="post">
	输入用户名: <input type="text" name="username"/>
	<input type="submit" value="找回密码">
</from>

<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>

</form>
</body>
</html>
