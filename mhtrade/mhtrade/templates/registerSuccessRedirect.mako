<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>请确认邮件</title>
</script>

</head>
<body>
<%include file="headbar.mako"/>
%if hasattr(c,"errorMsg"):
	${c.errorMsg} 
%else:
	<p>系统已经向您的邮箱发送一份邮件，请验证邮件中的链接信息即可完成注册。</p>
%endif
</body>