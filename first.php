<html> 
<head> 
<meta http-equiv="Content-Type" content="text/html;" />
<meta charset=utf-8 /> 
<title>XSSԭ������</title> 
</head> 
<body> 
<form action="" method="get"> 
<input type="text" name="xss_input"> 
<input type="submit"> 
</form> 
<hr> 
<?php 
$xss = $_GET['xss_input'];  
echo "�������Ϊ".$xss;  
?> 
</body> 
</html> 