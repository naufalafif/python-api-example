<?php

/*
ini adalah halaman untuk membaca hasil dari api python,
dengan cata membaca source code & melakukan parsing terhadap respon tersebut

*/


$page = file_get_contents('http://localhost:5000/hitung-pangkat');
$hasil_json  = json_decode($page);

echo "HASIL PANGKAT = ".$hasil_json->hasil_pangkat;
?>
<hr>

<?php

echo "ini adalah var dump ";
echo var_dump($hasil_json);

?>