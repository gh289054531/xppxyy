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
<br/>
<p>卖家请输入登录信息:</p>
<form action="/index/userlogin" method="post">
	用户名：<input type="text" name="username"/>
	密码：<input type="password" name="password"/>
	<input type="submit" value="登录服务器" />
</form>
</body>
</html>
	
