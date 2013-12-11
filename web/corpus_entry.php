<?php
  // A page to display a corpus entry based in mark down or plain text.
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
      <a href="index.html">Corpus</a> &gt; 
      Corpus Entry
    </div>
    <div class="content">
<?php

if (isset($_REQUEST['text'])) {
    $text = $_REQUEST['text'];
    print($text);
} else {
    print();
}
?>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013, <a href="http://www.nantien.edu.au/">www.nantien.edu.au</a>.
      </p>
    </div>
  </body>
</html>
