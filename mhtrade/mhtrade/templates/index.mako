<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>梦幻交易系统</title>
<script src="../index.js">
<link href="../index.css" rel="stylesheet" type="text/css" />
</script>

</head>
<body>

<div style="width:600px; margin:0 auto;text-align:center">

	<table style="width:600px; text-align:center" border="1">
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td >广东1区</td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td>广东2区</td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td onclick="ChooseBigServer(this)">广东3区</td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td>广东4区</td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>
		<tr style="height:50px">
			<td></td>
			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
 			<td></td>
		</tr>

	</table>
	<br/>

	<table  style="width:560px; text-align:center" border="1">
		<%
			count=0
		%>
		%if hasattr(c,'servernames'):
			%for servername in c.servernames:
				%if count==0:
					<tr style="height:50px;">
				%endif
				<td onclick="ChooseServer(this)">${servername}</td>
				%if count==6 or count==len(c.servernames)-1:
					</tr>
				%endif
				%if count==6:
					<%
						count=0
					%>
				%else:
					<%
						count=count+1;
					%>
				%endif
			%endfor
		%endif
	</table>
	
	<form action="/index/choosebigserver" method="post" id="form1">
		<input id="bigservername" type="hidden" name="bigservername" />
	</form>
	
	<form action="/index/chooseserver" method="post" id="form2">
		<input id="servername" type="hidden" name="servername" />
	</form>
</div>


</body>
</html>