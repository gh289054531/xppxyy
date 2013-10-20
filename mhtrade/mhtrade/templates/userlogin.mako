<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<p>您选择了服务器：${c.servername}</p>
<p>如果您是买家，请直接进入商品界面无需登录;如果您是卖家，需要登录后才能出售物品。</p>
<a href="">买家请点击</a>
<br>
<p>卖家请输入登录信息:</p>
<p>如果您没有帐号，请点击<a href="/userRegister/register">[注册]</a></p>
<form action="/index/userlogin" method="post">
	用户名：<input type="text" name="username"/>
	密码：<input type="password" name="password"/>
	<input type="submit" value="登录服务器" />
    <input type="hidden" value=${c.servername} name="servername"/>
</form>
	<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
	</p>
</body>
</html>
