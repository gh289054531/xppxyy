<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>用户登录</title>
<script src="../base64.js"></script>
<script type="text/javascript">
function encrypw(){
	var pw=document.getElementById("pw");
	var pwtext=pw.value;
	pw.value=base64encode(pwtext);
	return true;
}
</script>
</head>
<body>
<%include file="headbar.mako"/>
<p>如果您是买家，请直接进入商品界面无需登录;如果您是卖家，需要登录后才能出售物品。</p>
<a href="">买家请点击</a>
<br/>
<hr/>
<br/>
<p>卖家请输入登录信息:</p>
<p>如果您没有帐号，请点击<a href="/userRegister/register">[注册]</a></p>
<p><a href="/userRegister/findpasswd">[忘记密码]</a></p>
<form action="/index/userlogin" method="post">
	用户名：<input type="text" name="username"/>
	密码：<input id="pw" type="password" name="password"/>
	<input type="submit" value="登录服务器" onclick="return encrypw()" />
</form>
<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>
</body>
</html>
