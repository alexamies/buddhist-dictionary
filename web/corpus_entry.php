<?php
  // A page to display a corpus entry based in mark down or plain text.
require_once 'inc/markdown.php';
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <title>NTI Chinese-English Dictionary and Buddhist Text Project</title>
    <link rel="shortcut icon" href="images/yan.png" type="image/jpeg" />
    <link rel="stylesheet" type="text/css" href="styles.css"/>
  </head>
  <body>
    <img id="logo" src="images/yan.png" alt="Logo"/>
    <h1>NTI Chinese-English Dictionary and Buddhist Text Project</h1>
    <p class="menu">
      <a class="menu" href="index.html">Home</a> | 
      <a class="menu" href="tools.html">Tools</a> | 
      <a class="menu" href="corpus.html">Library</a> | 
      <a class="menu" href="dict_resources.html">Resources</a> | 
      <a class="menu" href="about.html">About</a>
    </p>
    <div class="breadcrumbs">
      <a href="corpus.html">Library</a> &gt; 
      Library Entry
    </div>
    <div class="content">
<?php
if (isset($_REQUEST['text'])) {
    $text = $_REQUEST['text'];
} elseif (isset($_REQUEST['uri'])) {
    $uri = $_REQUEST['uri'];
    $text = file_get_contents('corpus/' . $uri);
} else {
    print("<p>No text to display.</p>");
}
if (isset($text)) {
    $markdown = new Markdown($text);
    print($markdown->getHTML());
}
?>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013, <a href="http://www.nantien.edu.au/">www.nantien.edu.au</a>.
      </p>
    </div>
  </body>
</html>
