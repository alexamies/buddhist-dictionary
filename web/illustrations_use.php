<?php
  	require_once 'inc/illustration_model.php' ;
	require_once 'inc/illustration_dao.php' ;

	header('Content-Type: text/html;charset=utf-8');
	session_start();
	$conceptTitle = $_SESSION['conceptTitle'];
	$conceptURL = $_SESSION['conceptURL'];

	// Retrieve image information from database
	$mediumResolution = $_REQUEST['mediumResolution'];
	$illustrationDAO = new IllustrationDAO();
	$illustration = $illustrationDAO->getAllIllustrationByMedRes($mediumResolution);
	if ($illustration) {
		$titleZhCn = $illustration->getTitleZhCn();
		$titleEn = $illustration->getTitleEn();
		$author = $illustration->getAuthor();
		$authorURL = $illustration->getAuthorURL();
		$license = $illustration->getLicense();
		$licenseUrl = $illustration->getLicenseUrl();
		$licenseFullName = $illustration->getLicenseFullName();
		if (!$licenseFullName) {
			$licenseFullName = $license;
		}
		$highResolution = $illustration->getHighResolution();
	}
	
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
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>
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
      <h2>Image Use</h2>
<?php
	print("<div class='breadcrumbs'>");
  	print("<a href='index.html'>Chinese Notes 中文笔记</a> &gt; ");
  	print("<a href='" . $conceptURL . "'>" . $conceptTitle . "</a> &gt; ");
  	print("图片用法 Image Use");

	if ($illustration) {
		print("<h1>$titleZhCn $titleEn</h1>");
		if ($highResolution) {
			print("<div class='titlePicture'><img src='images/$highResolution'/></div>");
		} else {
			print("<div class='titlePicture'><img src='images/$mediumResolution'/></div>");
		}

		if ($authorURL) {
			print("<p>创始人 Created by: <a href='$authorURL'>$author</a></p>");
		} else if ($author) {
			print("<p>创始人 Created by: $author</p>");
		}

		print("<h3 class='article'>图片用法 Image Use</h3>");
		if ($licenseUrl) {
			print("<p>用法协议 Useage agreement: <a href='$licenseUrl'>$licenseFullName</a></p>");
		} else {
			print("<p>用法协议 Useage agreement: $licenseFullName</p>");
		}
	
	} else {
		print("图片 $mediumResolution 没有找到。");
		print("The image $mediumResolution was not found.");
	}
?>
      <p>
        Copyright Nan Tien Institute 2013 - 2014, 
        <a href="http://www.nantien.edu.au/" title="Nan Tien Institute">www.nantien.edu.au</a>.
      </p>
    </div>
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
  </body>
</html>
