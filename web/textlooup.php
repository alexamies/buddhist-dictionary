<?php
require_once 'inc/phrase.php' ;
mb_internal_encoding('UTF-8');
header('Content-Type: text/html;charset=utf-8');
error_log("Got a post request\n");
$phrase = new Phrase($_POST['text'], 'traditional');
$phraseElements = $phrase->getPhraseElements();
$words = "[";
foreach ($phraseElements as $phraseElement) {
    $elemText = $phraseElement->getText();
    $words .= '"' . $elemText . "\",";
}
$words = rtrim($words, ",") . "]";
print($words);
?>
