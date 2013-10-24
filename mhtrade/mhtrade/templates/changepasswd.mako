<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>登录成功</title>
<script src="../base64.js"></script>
<script type="text/javascript">
function encrypw(){
	var oldpasswd=document.getElementById("oldpasswd");
	var text=oldpasswd.value;
	oldpasswd.value=base64encode(text);
	
	var newpasswd=document.getElementById("newpasswd");
	var text=newpasswd.value;
	newpasswd.value=base64encode(text);
	
	var newpasswdrepeat=document.getElementById("newpasswdrepeat");
	var text=newpasswdrepeat.value;
	newpasswdrepeat.value=base64encode(text);
	
	return true;
}
</script>
</head>
<body>

<br/>
<%include file="headbar.mako"/>

<table style="width:600px;margin:0 auto;text-align:center;">
<form action="/userRegister/haschanged" method="post">
	<tr>
	<td>输 入 旧 密 码: </td>
	<td><input id="oldpasswd" type="password" name="oldpasswd"/></td>
	</tr>
	<tr>
	<td>输 入 新 密 码: </td>
	<td><input id="newpasswd" type="password" name="newpasswd"/></td>
	</tr>
	<tr>
	<td>再次输入新密码：</td>
	<td><input id="newpasswdrepeat" type="password" name="newpasswdrepeat"/></td>
	</tr>
	<tr>
	<td><input type="submit" value="确定" onclick="return encrypw()"></td>
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
