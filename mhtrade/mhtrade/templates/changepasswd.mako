<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>登录成功</title>
</head>
<body>

<br/>
<%include file="headbar.mako"/>

<table style="width:600px;margin:0 auto;text-align:center;">
<form action="/userRegister/haschanged" method="post">
	<tr>
	<td>输 入 旧 密 码: </td>
	<td><input type="password" name="oldpasswd"/></td>
	</tr>
	<tr>
	<td>输 入 新 密 码: </td>
	<td><input type="password" name="newpasswd"/></td>
	</tr>
	<tr>
	<td>再次输入新密码：</td>
	<td><input type="password" name="newpasswdrepeat"/></td>
	</tr>
	<tr>
	<td><input type="submit" value="确定"></td>
	</tr>
</from>
</table>
<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>
</form>
</body>
</html>
