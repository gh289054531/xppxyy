<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>管理员登录</title>
<script src="../base64.js"></script>
<script type="text/javascript">
function encrypw(){
	var pw=document.getElementById("pw");
	var pwtext=pw.value;
	console.log(pwtext);
	pw.value=base64encode(pwtext);
	console.log(pw.value);
	return true;
}
</script>
</head>
<body>
<%include file="headbar.mako"/>
	<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
	</p>
<form action="/index/adminlogin" method="post">
	管理员帐号：<input type="text" name="adminid" />
	密码：<input id="pw" type="password" name="adminpw" />
	<input type="submit" value="登录" onclick="return encrypw()" />
</form>
</body>
</html>