<?php
$ch = curl_init("http://37.111.52.52:2280/radiusmanager/api/sysapi.php?apiuser=admin&apipass=Admin@9000&q=get_userdata&username=ms202308250001");

curl_setopt ($ch, CURLOPT_RETURNTRANSFER, TRUE); 
curl_setopt ($ch, CURLOPT_BINARYTRANSFER, TRUE);
$json = curl_exec($ch);
print_r($json);
$res = json_decode($json, TRUE);
print_r($res);
if ($res[0] == 0) // 0 - SUCCESS, 1 - FAILURE
{print "Success!<br›";
print $res[0];
//print $res[1ll'expiry'];
}
else
print $res[1];

?>