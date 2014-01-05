<?php
// A stand-alone version of the word detail content.  
require_once 'inc/word_detail_top.php' ;
?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NTI Chinese-English Dictionary and Buddhist Text Project">
    <title>NTI Chinese-English Dictionary and Buddhist Text Project</title>
    <link rel="shortcut icon" href="images/yan.png" type="image/jpeg" />
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
    <!-- Custom styles for this template -->
    <link rel="stylesheet" href="buddhistdict.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script type="text/javascript" src="script/prototype.js"></script>
    <script type="text/javascript" src="script/search.js"></script>
    <script type="text/javascript" src="script/chinesenotes.js"></script>
  </head>
  <body>
    <div class="starter-template">
      <div class="row">
        <div class="span2"><img id="logo" src="images/yan.png" alt="Logo" class="pull-left"/></div>
        <div class="span7"><h1>NTI Chinese-English Dictionary and Buddhist Text Project</h1></div>
      </div>
    </div>
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="index.html">Home</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="corpus.html">Texts</a></li>
            <li class="active"><a href="tools.html">Tools</a></li>
            <li><a href="dict_resources.html">Resources</a></li>
            <li><a href="about.html">About</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">
      <h2>Chinese Word Detail</h2>
<?php
    // Print a list of words
    if (isset($words) && count($words) <> 1) {
      $len = count($words);
      if ($len == 0) {
        print("<p>No matches found</p>\n");
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
                "<td><a href='$script?id=$id'>" . $words[$i]->getSimplified() . "</a></td>\n" .
                "<td>" . $words[$i]->getTraditional() . "</td>\n" .
                "<td>" . $words[$i]->getPinyin() . "</td>\n" .
                "<td>\n" . $words[$i]->getEnglish() . "</td>\n" .
                "<td>$grammarCn ($grammarEn)</td>\n" .
                "<td>\n" . $words[$i]->getNotes() . "</td>\n" .
                "</tr>\n");
        }
        print("</tbody>\n" .
              "</table>\n");
      }
    // Print the details of an individual word
    } else {

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
            "\t&nbsp;&nbsp;&nbsp;\t<span>" . $word->getPinyin() . "</span>" .
            "<span>\t&nbsp;&nbsp;&nbsp;\t" . $word->getEnglish() . "</span>" .
            "</p>\n");
      print("<div>" . 
            "Traditional: " . $word->getTraditional() . "</div>\n");
      if ($word->getMp3()) {
        print("<div>Listen: <a href='mp3/" . $word->getMp3() . "'>" .
              "<img src='images/audio.gif' alt='Play audio'/>" . 
              "</a>" .
              "</div>\n");
      }

      // Grammar
      $grammarEn = $word->getGrammar();
      $grammarText = $grammarCnLookup[$grammarEn];
      print("<div>Grammar: " . $grammarText . "</div>\n");
		
      // Detailed notes
      if ($word->getNotes()) {
        print("<div>Notes: " . $word->getNotes() . "</div>\n");
      }
		
      // Synonyms
      $synonymDAO = new SynonymDAO();
      $synonyms = $synonymDAO->getSynonyms($simplified);
      if (isset($synonyms) && count($synonyms) > 0) {
        print("<div>Synonyms: ");
        foreach ($synonyms as  $synonym) {
          print("<a href='" . $_SERVER['SCRIPT_NAME'] . "?word=" .  $synonym . "'>" .  $synonym . "</a> ");
        }
        print("</div>\n");
      }
		
      // Related terms
      print(getRelatedText($simplified));

      // Description of concept
      if ($word->getConceptCn()) {
        print("<div>Concept: " . $word->getConceptCn() . " " . $word->getConceptEn() . "</div>\n");
      }

      // Link to parent concept
      if ($word->getParentEn()) {
        print("<div>Parent concept: " . 
        "<a href='" . $_SERVER['SCRIPT_NAME'] . "?english=" . 
        $word->getParentEn() . "'>" . $word->getParentCn() . 
        "</a> (" . 
        $word->getParentEn() . 
        ")</div>\n");
      }

      // Topic
      if ($word->getTopicCn()) {
        print("<div>Topic: " . 
              "<a href='/topic.php?english=" . 
              urlencode($word->getTopicEn()) . "'>" . 
              $word->getTopicEn() . "</a></div>\n");
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
            print("<div>Listen: <a href='mp3/" . $example->getAudioFile() . 
                  "' target='audio'>" .
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
    }

    print("</div><p/><p/>");
?>
    <div>
      <span id="toolTip"><span id="pinyinSpan">Pinyin</span> <span id="englishSpan">English</span></span>
    </div>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013-2014, 
        <a href="http://www.nantien.edu.au/" title="Fo Guang Shan Nan Tien Institute">www.nantien.edu.au</a>.
      </p>
    </div>
  </body>
</html>
