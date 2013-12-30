<?php
// A stand-alone version of the word detail content.  
require_once 'inc/word_detail_top.php' ;
?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <title>NTI Chinese-English Dictionary and Buddhist Text Project</title>
    <link rel="shortcut icon" href="images/yan.png" type="image/jpeg" />
    <link rel="stylesheet" type="text/css" href="styles.css"/>
    <script type="text/javascript" src="script/prototype.js"></script>
    <script type="text/javascript" src="script/search.js"></script>
    <script type="text/javascript" src="script/chinesenotes.js"></script>
  </head>
  <body>
    <img id="logo" src="images/yan.png" alt="Logo"/>
    <h1>NTI Chinese-English Dictionary and Buddhist Text Project</h1>
    <p class="menu">
      <a class="menu" class="menu" href="index.html">Home</a> |
      <a class="menu" href="tools.html">Tools</a> | 
      <a class="menu" href="corpus.html">Library</a> | 
      <a class="menu" href="dict_resources.html">Resources</a> | 
      <a class="menu" href="about.html">About</a>
    </p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; 
      Phrase detail
    </div>
    <p>
      Phrase detail for phrase with id
<?php
    echo $_REQUEST['id']
?>
    </p>
    <div>
      <span id="toolTip"><span id="pinyinSpan">Pinyin</span> <span id="englishSpan">English</span></span>
    </div>
      <hr/>
    <p>
      Copyright Nan Tien Institute 2013, <a href="http://www.nantien.edu.au/">www.nantien.edu.au</a>.
    </p>
  </body>
</html>
