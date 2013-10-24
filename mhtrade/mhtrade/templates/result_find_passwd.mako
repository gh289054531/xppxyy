<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>重设密码</title>
<script src="../base64.js"></script>
<script type="text/javascript">
function encrypw(){
	var pw=document.getElementById("pw");
	var pwtext=pw.value;
	pw.value=base64encode(pwtext);
	console.log(pw.value)
	var repw=document.getElementById("repw");
	var pwtext=repw.value;
	repw.value=base64encode(pwtext);
	console.log(repw.value)
	return true;
}
</script>
</head>
<body>
<%include file="headbar.mako"/>

<form action="/userRegister/if_findpasswd" method="post">
	输 入 新 密 码: <input id="pw" type="password" name="newpasswd"/>
	再次输入新密码：<input id="repw" type="password" name="newpasswdrepeat"/>
	<input type="hidden" name="username" value=${c.username} />
	<input type="submit" value="确定" onclick="return encrypw()">
</from>

<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>

</form>
</body>
</html>
