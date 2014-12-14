<html xmlns="http://www.w3.org/1999/xhtml" ng-app="phraseApp">
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
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
      ga('create', 'UA-57634593-1', 'auto');
      ga('send', 'pageview');
    </script>
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
            <li class="active"><a href="corpus.html">Texts</a></li>
            <li><a href="tools.html">Tools</a></li>
            <li><a href="dict_resources.html">Resources</a></li>
            <li><a href="about.html">About</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container" ng-controller="phraseCtrl">
      <script>
        id = "<?= $_REQUEST['id'] ?>";
      </script>
      <h2>Phrase Detail</h2>
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>Chinese Text</th>
            <th><a href="annotation.html" title="More information on the phrase detail format">Phrase Detail</a></th>
          </tr>
        </thead>
        <tbody>
          <tr ng-repeat="phrase in results">
            <td>{{phrase.chinese_phrase}}</td>
            <td>
              {{phrase.pos_tagged}}
              <div ng-if="phrase.sanskrit">
                Sanskrit: {{phrase.sanskrit}}
              </div>
              <div>
                Source: {{phrase.source_name}}
              </div>
            </td>
          <tr>
        </tbody>
      </table>
      <p>
        See the <a href="pos_tags.html">Part-of-Speech Tag Definitions</a> for a list of the tags used.
      </p>
      <div>
        <span id="toolTip"><span id="pinyinSpan">Pinyin</span> <span id="englishSpan">English</span></span>
      </div>
      <hr/>
      <p>
        Copyright Nan Tien Institute 2013 - 2014, 
        <a href="http://www.nantien.edu.au/" title="Nan Tien Institute">www.nantien.edu.au</a>.
      </p>
      <p>This page was last updated on December 13, 2014.</p>
    <div>
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <script src="script/angular.min.js"></script>
    <script src="script/phrase.js"></script>
  </body>
</html>
