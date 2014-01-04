<?php
// Script to look up all words in a block of Chinese text
require_once 'inc/phrase.php' ;
mb_internal_encoding('UTF-8');
header('Content-Type: text/json;charset=utf-8');
$text = $_POST['text'];
error_log("Length of text: " . strlen($text));
if (strlen($text) > 100) {
    print('{"error":"Too long. Text cannot exceed 100 characters."}' .
          '{"words":"[]"}');
} else {
    $phrase = new Phrase($text, 'traditional');
    $phraseElements = $phrase->getPhraseElements();
    $words = "[";
    foreach ($phraseElements as $phraseElement) {
        $elemText = $phraseElement->getText();
        $elemType = $phraseElement->getType();
        $wordSenses = array();
        $english = "";
        $notes = "";
        $id = "";
        if (($elemType == 1) || ($elemType == 2)) {
            $wordSenses = $phraseElement->getWords();
            $english = $wordSenses[0]->getEnglish();
            $notes = $wordSenses[0]->getNotes();
            $id = $wordSenses[0]->getId();
        }
        $count = count($wordSenses);
        $words .= '{"text":"' . $elemText . '",' .
                   '"english":"' . $english . '",' .
                   '"notes":"' . $notes . '",' .
                   '"id":"' . $id . '",' .
                   '"count":"' . $count . '"' .
                  '},';
    }
    $words = rtrim($words, ",") . "]";
    error_log("words: $words \n");
    print('{"words":' . $words . "}");
}
?>
