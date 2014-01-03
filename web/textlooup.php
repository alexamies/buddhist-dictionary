<?php
// Script to look up all words in a block of Chinese text
require_once 'inc/phrase.php' ;
mb_internal_encoding('UTF-8');
header('Content-Type: text/html;charset=utf-8');
$text = $_POST['text'];
error_log("Length of text: " . strlen($text));
if (strlen($text) > 100) {
    print('{"error":"Too long. Text cannot exceed 100 characters."}' .
          '{"words":""}');
} else {
    error_log("Returning results.\n");
    $phrase = new Phrase($text, 'traditional');
    $phraseElements = $phrase->getPhraseElements();
    $words = "[";
    foreach ($phraseElements as $phraseElement) {
        $elemText = $phraseElement->getText();
        $words .= '"' . $elemText . "\",";
    }
    $words = rtrim($words, ",") . "]";
    print('{"words":' . $words . "}");
}
?>
