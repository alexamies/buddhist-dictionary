<?php
  // Searches for an individual character
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NTI Buddhist Text Reader">
    <title>NTI Buddhist Text Reader</title>
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
    <script type='text/javascript' src='script/chinesenotes.js'></script>
    <script type="text/javascript" src="script/prototype.js"></script>
    <script type="text/javascript" src="script/character_search.js"></script>
  </head>
  <body>
    <div class="starter-template">
      <div class="row">
        <div class="span2"><img id="logo" src="images/yan.png" alt="Logo" class="pull-left"/></div>
        <div class="span7"><h1>NTI Buddhist Text Reader</h1></div>
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
      <h2>Character Search</h2>
      <div class='search'>
        <form action='character_detail_frag.php' method='post' id='searchForm'>
          <fieldset>
            <p>
              <input type='text' name='character' id='character' size='5'/>
              <input id='searchButton' type='submit' value='Search' title='Search'/>
            </p>
            <p>
              <input type='radio' name='inputType' id='singleRadio' value='single' 
                     checked='checked'/>
              <label for="singleRadio">Single character</label>
              <input type='radio' name='inputType' id='multipleRadio' value='multiple'/>
              <label for="multipleRadio">Multiple characters</label><br/>
          </p>
        </fieldset>
      </form>
      <div id='results'>
        <p>
          To search for a single character enter the character or Unicode (e.g. 卜, 21340, 
          or 535c) into the text field. To search for multiple characters check the 
          multiple character checkbox and enter the characters into the text field.
          You can also search on Sanskrit (e.g. Devanagari: पण्डित; IAST: paṇḍita) 
          and International Phonetic Alphabet (e.g. ɔ̃) character strings
	</p>
      </div>
    </div>
    <div id='searching' style='display:none;'>Searching ...</div>
<?php
  // Print the details of the character
  require_once 'character_detail_frag.php' ;
?>
      <div>
        <span id="toolTip" style='display:none;'><span id="pinyinSpan">Pinyin</span> 
        <span id="englishSpan">English</span></span>
      </div>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013 - 2014, 
        <a href="http://www.nantien.edu.au/" title="Nan Tien Institute">www.nantien.edu.au</a>.
      </p>
    </div>
  </body>
</html>
