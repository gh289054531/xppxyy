<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>用户注册</title>
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
	<table style="width: 600px; margin: 0 auto; text-align: center;">
		<form action="/userRegister/doregister" method="post">
			<tr>
				<td>用户名：</td>
				<td><input type="text" name="username"></input></td>
			</tr>
			<tr>
				<td>密码：</td>
				<td><input id="pw" type="password" name="password"></input></td>
			</tr>
			<tr>
				<td>密码确认：</td>
				<td><input id="repw" type="password" name="repassword"></input></td>
			</tr>
			<tr>
				<td>QQ：</td>
				<td><input type="text" name="qq"></input></td>
			</tr>
			<tr>
				<td>邮箱：</td>
				<td><input type="text" name="email"></input></td>
			</tr>
			<tr>
				<td>个性签名：</td>
				<td><input type="text" name="selfIntroduction"></input></td>
			</tr>
			<tr>
				<td><input type="submit" value="注册" onclick="return encrypw()"></input></td>
			</tr>
		</form>
	</table>
	<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>
</body>
</html>