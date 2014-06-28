<?php
  // A stand-alone version of the Sanskrit search.  
  require_once 'inc/sanskrit_dao.php' ;
?>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NTI Chinese-English Dictionary and Buddhist Text Project">
    <title>NTI Chinese-English Dictionary and Buddhist Text Project</title>
    <link rel="shortcut icon" href="images/yan.png" type="image/jpeg" />
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
    <!-- Custom styles for this template -->
    <link rel="stylesheet" href="buddhistdict.css" rel="stylesheet">
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
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
      <h2>Sanksrit Search</h2>
<?php
    $searchTerm = "";
    if (isset($_REQUEST['word'])) {
        $searchTerm = $_REQUEST['word'];
    }
?>
      <div class='search'>
        <form action='sanskrit_query.php' method='post' id='searchForm'>
          <input type='text' name='word' id='searchWord' size='50'
                 value='<?php echo htmlspecialchars($searchTerm, ENT_QUOTES) ?>'/>
          <input id='searchButton' type='submit' value='Search' title='Search'/>
        </form>
      </div>
<?php
$words = array();
if (isset($_REQUEST['word'])) {
  $word = $_REQUEST['word'];
  $sanskritDAO = new SanskritDAO();
  $words = $sanskritDAO->getSanskrit($word);
	
  // Print list of words
  if (isset($words)) {
    $len = count($words);
    if ($len == 0) {
      $suggestions = $sanskritDAO->suggest($word);
      print("<p>No matches found.</p>\n");
      $len = count($suggestions);
      if ($len == 0) {
        print("<p>No suggestions found.</p>\n");
      } else {
        print("<p>Suggestions:\n");
        for ($i=0; $i<$len; $i++) {
          $alternate = $suggestions[$i]->getAlternate();
          print("<a href='?word=" . $alternate . "'>" .
                $alternate . "</a> (" .
                $suggestions[$i]->getReason() . ") ");
        }
        print("</p>\n");
      }
    } else {
      print("<table id='wordTable' class='table table-bordered table-hover'>\n" .
            "<tbody id='wordTabBody'>\n" .
            "<tr>" . 
            "<th>IAST</th>" .
            "<th>Devanagari</th>" .
            "<th>Pali</th>" .
            "<th>Chinese</th>" .
            "<th>English</th>" . 
            "<th>Grammar</th>" .
            "<th>Root / Stem</th>" .
            "<th>Notes</th>" .
            "</tr>\n");
      for ($i=0; $i<$len; $i++) {
        print("<tr>\n" .
              "<td>" . $words[$i]->getIast() . "</td>" .
              "<td>" . $words[$i]->getDevan() . "</td>" .
              "<td>" . $words[$i]->getPali() . "</td>" .
              "<td>" . $words[$i]->getTraditional() . "</td>" .
              "<td>" . $words[$i]->getEnglish() . "</td>" .
              "<td>" . $words[$i]->getGrammar() . "</td>" .
              "<td>" . $words[$i]->getRoot() . "</td>" .
              "<td>" . $words[$i]->getNotes() . "</td>" .
              "</tr>\n");
      }
      print("</tbody>\n" .
            "</table>\n");
    }
  }
}
?>
      <p>
        Enter IAST, plain Latin, Devanāgarī, Traditional Chinese, or English and click Search.
        Examples: tathāgata, Tathagata, तथागत, 如來, or Buddha. See 
        <a href="/sanskrit_in_buddhism.html">Understanding Buddhist Sanskrit Terms</a> for 
        and introduction to Sanskrit Buddhist terms and use electronic documents.
      </p>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013 - 2014, <a href="http://www.nantien.edu.au/" 
        title="Nan Tien Institute">www.nantien.edu.au</a>.
      </p>
    </div>
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
  </body>
</html>
