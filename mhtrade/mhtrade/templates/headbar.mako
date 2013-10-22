
<table style="height:50px;width:100%;text-align:center;">
	<tr>
		<td>
			% if hasattr(c,"username"): 
				您好：${c.username}!&nbsp;&nbsp;<a href="/index/userlogout">[退出]</a> 
			% else: 
				<a href="/index/userloginpage">[登录]</a>
			% endif
		</td>
			%if hasattr(c,"username"):
				<td><a href="/userRegister/changepasswd">[修改密码]</a></td>
			%endif
		<td><a href="/userRegister/register" target="_blank">[注册]</a></td>
		<td><a href="/userRegister/findpasswd">[找回密码]</a></td>
		<td><a href="/index/index">[选择服务器]</a>
		%if hasattr(c,"servername"):
			当前服务器：${c.servername}
		%endif 
		</td>
		<td><a href="/index/chooserole">[选择角色]</a>
		%if hasattr(c,"rolename"):
			当前身份：${c.rolename}
		%endif 
		</td>
		<td><a href="">[交易界面]</a></td>
	</tr>

</table>
<hr />