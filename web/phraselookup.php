<?php
// Script to look up a phrase entry
require_once 'inc/phrase_dao.php' ;
mb_internal_encoding('UTF-8');
header('Content-Type: text/json;charset=utf-8');
$id = $_GET['id'];
error_log("Phrase id: $id");
$dao = new PhraseDAO();
$phrase = $dao->getPhrase($id);
$json = "[";
if ($phrase != null) {
    $chinese_phrase = $phrase->getChinesePhrase();
    $pos_tagged = $phrase->getPosTagged();
    $sanskrit = $phrase->getSanskrit();
    $source_no = $phrase->getSourceNo();
    $source_name = $phrase->getSourceName();
    $json .= "{\"id\":\"$id\",".
              "\"chinese_phrase\":\"$chinese_phrase\",".
              "\"pos_tagged\":\"$pos_tagged\",".
              "\"sanskrit\":\"$sanskrit\",".
              "\"source_no\":\"$source_no\",".
              "\"source_name\":\"$source_name\"".
              "}";
}
$json .= "]";
error_log("json: $json \n");
print($json);
?>
