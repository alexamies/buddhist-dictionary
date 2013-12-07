<?php
  // A stand-alone version of the Sanskrit search.  
  require_once 'inc/sanskrit_dao.php' ;
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <title>NTI Chinese-Sanskrit-English Buddhist Dictionary</title>
    <link rel="shortcut icon" href="http://nantien.edu.au/sites/default/files/Nan%20Tien%20Institute%20Logo.jpg" 
          type="image/jpeg" />
    <link rel="stylesheet" type="text/css" href="styles.css"/>
  </head>
  <body>
    <h1>NTI Chinese-Sanskrit-English Buddhist Dictionary</h1>
    <p class="menu">
      <a class="menu" href="index.html">Home</a> | 
      <a class="menu" href="tools.html">Tools</a> | 
      <a class="menu" href="corpus.html">Corpus</a> | 
      <a class="menu" href="dict_resources.html">Resources</a> | 
      <a class="menu" href="about.html">About</a>
    </p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; 
      Sanksrit Search
    </div>
<?php
    $searchTerm = "";
    if (isset($_REQUEST['word'])) {
        $searchTerm = $_REQUEST['word'];
    }
?>
    <div class="content">
      <div class='search'>
        <form action='sanskrit_query.php' method='post' id='searchForm'>
          <fieldset>
            <input type='text' name='word' id='searchWord' size='50'
                   value='<?php echo htmlspecialchars($searchTerm, ENT_QUOTES) ?>'/>
            <input id='searchButton' type='submit' value='Search' title='Search'/>
          </fieldset>
        </form>
      </div>
<?php

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
			            print(
			                "<a href='?word=" . $alternate . "'>" .
			                $alternate . "</a> (" .
			                $suggestions[$i]->getReason() . ") "
			            );
			        }
			        print("</p>\n");
			    }
		    } else {
			    print(
					"<table id='wordTable'>\n" .
					"<tbody id='wordTabBody'>\n" .
					"<tr>" . 
					"<th class='portlet'>IAST</th>" .
					"<th class='portlet'>Devanagari</th>" .
					"<th class='portlet'>Pali</th>" .
					"<th class='portlet'>Chinese</th>" .
					"<th class='portlet'>English</th>" . 
					"<th class='portlet'>Grammar</th>" .
					"<th class='portlet'>Notes</th>" .
					"</tr>\n"
					);
			    for ($i=0; $i<$len; $i++) {
				    print(
						"<tr>\n" .
						"<td>" . $words[$i]->getIast() . "</td>" .
						"<td>" . $words[$i]->getDevan() . "</td>" .
						"<td>" . $words[$i]->getPali() . "</td>" .
						"<td>" . $words[$i]->getTraditional() . "</td>" .
						"<td>" . $words[$i]->getEnglish() . "</td>" .
						"<td>" . $words[$i]->getGrammar() . "</td>" .
						"<td>" . $words[$i]->getNotes() . "</td>" .
						"</tr>\n"
						);
			    }
			    print(
					"</tbody>\n" .
					"</table>\n"
					);
		    }
		}
	}
?>
      <p>
        Enter IAST, plain Latin, Devanagari, Traditional Chinese, or English and click Search.
        Examples: tathāgata, Tathagata, तथागत, 如來, or Buddha. See 
        <a href="/sanskrit_in_buddhism.html">Understanding Buddhist Sanskrit Terms</a> for 
        and introduction to Sanskrit Buddhist terms and use electronic documents.
      </p>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013, <a href="http://www.nantien.edu.au/">www.nantien.edu.au</a>.
      </p>
    </div>
  </body>
</html>
