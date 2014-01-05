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
            <li class="active"><a href="corpus.html">Texts</a></li>
            <li><a href="tools.html">Tools</a></li>
            <li><a href="dict_resources.html">Resources</a></li>
            <li><a href="about.html">About</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">
      <h2>Phrase Detail</h2>
    <p>
      [UNDER DEVELOPMENT] Phrase detail for phrase with id
<?php
    echo $_REQUEST['id']
?>
    </p>
    <div>
      <span id="toolTip"><span id="pinyinSpan">Pinyin</span> <span id="englishSpan">English</span></span>
    </div>
      <hr/>
    <p>
      Copyright Nan Tien Institute 2013 - 2014, 
      <a href="http://www.nantien.edu.au/" title="Nan Tien Institute">www.nantien.edu.au</a>.
    </p>
  </body>
</html>
