<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title></title>
</head>
<body>

<br/>


<p>邮件已发送至您注册的邮箱，请点击邮件中的链接完成找回密码</p>

<p>
	% if hasattr(c,"errorMsg") :
		${c.errorMsg}
	% endif
</p>

</form>
</body>
</html>
