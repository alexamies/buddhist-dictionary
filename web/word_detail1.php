<?php
// An embedded version of the word detail content.  This HTML content is fetched
// using AJAX and embedded in the search page.

require_once 'inc/word_detail_top.php' ;
?>
<?php
// Print the details of the word
if (isset($words) && count($words) <> 1) {
    $len = count($words);
    if ($len == 0) {
        print("<p>No matches found.  Try phrase mode or look at the <a href='help.html'>Help</a>.</p>\n");
    } else {
        print("<p>$len matches found</p>\n" .
              "<table id='wordTable'>\n" .
              "<tbody id='wordTabBody'>\n" .
              "<tr>" . 
              "<th class='portlet'>Simplified</th>" .
              "<th class='portlet'>Traditional</th>" .
              "<th class='portlet'>Pinyin</th>" .
              "<th class='portlet'>English</th>" .
              "<th class='portlet'>Grammar</th>" . 
              "<th class='portlet'>Notes</th>" .
              "</tr>\n");
        for ($i=0; $i<$len; $i++) {
            $grammarEn = $words[$i]->getGrammar();
            $grammarCn = $grammarCnLookup[$grammarEn];
            $id = $words[$i]->getId();
            print("<tr>\n" .
                  "<td><a href='word_detail.php?id=$id'>" . $words[$i]->getSimplified() . "</a></td>\n" .
                  "<td>" . $words[$i]->getTraditional() . "</td>\n" .
                  "<td>" . $words[$i]->getPinyin() . "</td>\n" .
                  "<td>\n" . $words[$i]->getEnglish() . "</td>\n" .
                  "<td>$grammarCn</td>\n" .
                  "<td>\n" . $words[$i]->getNotes() . "</td>\n" .
                  "</tr>\n");
        }
        print("</tbody>\n" .
              "</table>\n");
    }
} else {
    // We have an illustration for this word
    if ($word->getImage()) {
        $mediumResolution = $word->getImage();
        print("<div id='wordImage'>" .
              "<a href='illustrations_use.php?mediumResolution=$mediumResolution'>" .
              "<img class='use' src='images/$mediumResolution" . 
              "' alt='" . $word->getEnglish() . 
              "' title='" . $word->getEnglish() . 
              "'/>" .
              "</a>" .
              "</div>\n");
    }
    // Basic text
    $simplified = $word->getSimplified();
    print("<p class='wordDetail'>" .
          "<span id='simplifiedDetail'>" . $simplified . "</span>" .
          "&nbsp;&nbsp;&nbsp;<span>" . $word->getPinyin() . "</span>" .
          "&nbsp;&nbsp;&nbsp;<span>" . $word->getEnglish() . "</span>" .
          "</p>\n");
    print("<div>" . 
          "Traditional: " . $word->getTraditional() . "</div>\n");
    if ($word->getMp3()) {
        print("<div>听 listen: <a href='mp3/" . $word->getMp3() . "' target='audio'>" .
              "<img src='images/audio.gif' alt='Play audio' border='0'/>" . 
              "</a>" .
              "</div>\n");
    }
    $grammarEn = $word->getGrammar();
    $grammarCn = $grammarCnLookup[$grammarEn];
    print("<div>Grammar: " . $grammarCn . "</div>\n");
    if ($word->getNotes()) {
        print("<div>Notes: " . $word->getNotes() . "</div>\n");
    }
		
    // Synonyms
    // $synonymDAO = new SynonymDAO();
    // $synonyms = $synonymDAO->getSynonyms($simplified);
    if (isset($synonyms) && count($synonyms) > 0) {
        print("<div>Synonyms: ");
        foreach ($synonyms as  $synonym) {
            print("<a href='word_detail.php?word=" .  $synonym . "'>" .  $synonym . "</a> ");
        }
        print("</div>\n");
    }
		
    // Related terms
    // print(getRelatedText($simplified));

    // Description of concept
    if ($word->getConceptCn()) {
        print("<div>Concept: " . $word->getConceptCn() . " " . $word->getConceptEn() . "</div>\n");
    }

    // Link to parent concept
    if ($word->getParentEn()) {
        print("<div>Parent concept: " . 
              "<a href='word_detail.php?english=" . 
              $word->getParentEn() . "'>" . $word->getParentCn() . 
              "</a> (" . 
              $word->getParentEn() . 
              ")</div>\n");
    }

    // Topic
    if ($word->getTopicCn()) {
        print("<div>Topic: " . 
              "<a href='word_detail.php?english=" . $word->getTopicEn() . "'>" . 
              $word->getTopicCn() . "</a> (" . $word->getTopicEn() . 
              ")</div>\n");
    }
		
    // Get nominal measure words
    if ($grammarEn == 'noun') {
        $measureWordDAO = new MeasureWordDAO();
        $mws = $measureWordDAO->getMeasureWordsForNoun($word->getSimplified());
        if (isset($mws) && count($mws) > 0) {
            print("<p>Measure words: ");
            foreach ($mws as  $mw) {
                print("<a href=\"word_detail.php?id=" . $mw->getId() . "\">" .
                      $mw->getSimplified() .
                      "</a> ");
            }
            print("</p>\n");
        }
			
    // get nouns matching measure words
    } else if ($grammarEn == 'measure word') {
        $measureWordDAO = new MeasureWordDAO();
        $nouns = $measureWordDAO->getNounsForMeasureWord($word->getSimplified());
        if (isset($nouns) && count($nouns) > 0) {
            print("<p>Matching nouns: ");
            foreach ($nouns as  $noun) {
                print("<a href=\"word_detail.php?id=" . $noun->getId() . "\">" .
                      $noun->getSimplified() .
                      "</a> ");
            }
            print("</p>\n");
        }
    }

    // Examples
    // $exampleDAO = new ExampleDAO();
    // $examples = $exampleDAO->getExamplesForWord($word->getId());
    if (isset($examples) && count($examples) > 0) {
        print("<p>Examples:</p>" .
        "<ol>");
        foreach ($examples as  $example) {
            print("<li>" .
                  "<div>" . 
                  $example->getSimplified() . 
                  '</div><div>' . $example->getPinyin(). 
                  '</div><div>' . $example->getEnglish() . 
                  "</div>\n");
            if ($example->getAudioFile()) {
                print("<div>听 (listen): <a href='mp3/" . $example->getAudioFile() . "' target='audio'>" .
                      "<img src='images/audio.gif' alt='Play audio' border='0'/>" . 
                      "</a>" .
                      "</div>\n");
            }
            if ($example->getSourceLink()) {
                print("<div>Source: <a href='" . $example->getSourceLink() . 
                      "'>" . $example->getSource() . "</a></div>\n");
            } elseif ($example->getSource()) {
                print("<div>Source: " . $example->getSource() . "</div>\n");
            }
            print("</li>\n");
        }
        print("</ol>\n");
    }

    // Annotation markup
    $server = "";
    //$server = "http://chinesenotes.com";
    print("<h2 class='wordDetail'>HTML</h2>\n" .
          "<div class='code'>\n" .
          "<br/>\n" . 
          " &lt;a href='$server$script?id=" . $word->getId() . "'&gt;" . $word->getSimplified() . "&lt;/a&gt;" . 
          "<br/>\n" . 
          "<br/>\n" . 
          "</div>\n");
}
?>  
<p>
  <a href='help.html'>Help</a>
</p>
