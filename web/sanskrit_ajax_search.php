<?php
  // An AJAX endpoing for Sanskrit search.  
  require_once 'inc/sanskrit_dao.php' ;
  $words = array();
  if (isset($_REQUEST['word'])) {
    $word = $_REQUEST['word'];
    $matchtype = $_REQUEST['matchtype'];
    $sanskritDAO = new SanskritDAO();
    $words = $sanskritDAO->getSanskrit($word, $matchtype);

    // Print list of words
    if (isset($words)) {
      $len = count($words);
      if ($len == 0) {
        $suggestions = $sanskritDAO->suggest($word);
        print('{"error":"No matches found."}');
        //$len = count($suggestions);
        if ($len == 0) {
          //print('{"error":"No suggestions found."}');
        } else {
          $suggestionsJSON = '[';
          for ($i=0; $i<$len; $i++) {
            $alternate = $suggestions[$i]->getAlternate();
            $reason = $suggestions[$i]->getReason();
            $suggestionsJSON .= '{"word":"' . $alternate . '","reason":"' . $reason . '"}';
            if ($i < $len -1) {
              print(',');
            }
          }
          $suggestionsJSON .= ']';
        }
      } else {
        $wordsJSON = '[';
        for ($i=0; $i<$len; $i++) {
          $wordsJSON .= '{' .
              '"iast":"' . $words[$i]->getIast() . '",' .
              '"devanagari":"' . $words[$i]->getDevan() . '",' .
              '"pali":"' . $words[$i]->getPali() . '",' .
              '"traditional":"' . $words[$i]->getTraditional() . '",' .
              '"english":"' . $words[$i]->getEnglish() . '",' .
              '"grammar":"' . $words[$i]->getGrammar() . '",' .
              '"root":"' . $words[$i]->getRoot() . '",' .
              '"notes":"' . $words[$i]->getNotes() . '"' .
              '}';
          if ($i < $len -1) {
            $wordsJSON .= ',';
          }
        }
        $wordsJSON .= ']';
      }
    }
    if (isset($wordsJSON)) {
      print('{"words":' . $wordsJSON . "}");
    }
  } else {
    print('{"error":"Please supply a query."}');
  }
?>
