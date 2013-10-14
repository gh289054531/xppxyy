function ChooseBigServer(td){
	var bigserver=td.innerHTML;
	console.log(bigserver);
	var form1=document.getElementById("form1");
	var input=document.getElementById("bigservername");
	input.value=bigserver;
	form1.submit();
}

function ChooseServer(td){
	var server=td.innerHTML;
	console.log(server);
	var form2=document.getElementById("form2");
	var input=document.getElementById("servername");
	input.value=server;
	form2.submit();
}