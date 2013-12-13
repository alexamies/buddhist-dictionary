<?php
  // Searches for an individual character
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <title>NTI Chinese-Sanskrit-English Buddhist Dictionary</title>
    <link rel="stylesheet" type="text/css" href="styles.css"/>
    <script type='text/javascript' src='script/chinesenotes.js'></script>
    <script type="text/javascript" src="script/prototype.js"></script>
    <script type="text/javascript" src="script/character_search.js"></script>
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
    <div class="content">
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
        Copyright Nan Tien Institute 2013, <a href="http://www.nantien.edu.au/">www.nantien.edu.au</a>.
      </p>
    </div>
  </body>
</html>
