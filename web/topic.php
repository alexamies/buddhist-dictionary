<?php
  	require_once 'inc/words_dao.php' ;
  	require_once 'inc/topic_dao.php' ;

	header('Content-Type: text/html;charset=utf-8');
	session_start();
	$conceptTitle = $_SESSION['conceptTitle'];
	$conceptURL = $_SESSION['conceptURL'];
	if (isset($_REQUEST['english'])) {
		$topicEnglish = $_REQUEST['english'];
		$_SESSION['topicEnglish'] = $topicEnglish;
	} else {
		$topicEnglish = $_SESSION['topicEnglish'];
	}
	$topicDAO = new TopicDAO();
	$topic = $topicDAO->getTopicForEnglish($topicEnglish);
	$title = $topic->getSimplified() . ' ' . $topic->getEnglish();
	$longtitle = '词汇目录：' . $topic->getSimplified() . ' Vocabulary List: ' . $topic->getEnglish();
	$longtitleBr = '词汇目录：' . $topic->getSimplified() . '<br/> Vocabulary List: ' . $topic->getEnglish();
	$_SESSION['conceptTitle'] = $title;
	$_SESSION['conceptURL'] = $_SERVER['SCRIPT_NAME'];
  	require_once 'inc/words_dao.php' ;

	$wordsDAO = new WordsDAO();
	$words = $wordsDAO->getWordsForTopicEn($topic->getEnglish());

	// Grammar lookup
	$grammarCnLookup = array(
			'noun'  => 'Noun 名词', 
			'adjective' => 'Adjective 形容词',
			'proper noun' => 'Proper noun 专名',
			'verb' => 'Verb 动词',
			'adverb' => 'Adverb 副词',
			'particle' => 'Particle 助词',
			'pronoun' => 'Pronoun 代词',
			'numeral' => 'Numeral 数词',
			'ordinal' => 'Ordinal 序数',
			'preposition' => 'Preposition 介词',
			'measure word' => 'Measure word 量词',
			'conjunction' => 'Conjunction 连词',
			'interrogative pronoun' => 'Interrogative pronoun 疑问代词',
			'auxiliary verb' => 'Auxiliary verb 助动词',
			'idiom' =>	'Idiom 成语',
			'phrase' => 'Phrase 词组',
			'quantity' => 'Quantity 数量'
			);

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
    <link rel="shortcut icon" href="/favicon.ico"/>
    <link rel="stylesheet" type="text/css" href="styles.css"/>
    <script type="text/javascript" src="script/chinesenotes.js"></script>
<?php
    print("<title>$longtitle</title>");
    print("<meta name='keywords' content='中文词汇, $title'>");
    print("<meta name='description' content='$longtitle'>");
?>
  </head>
  <body>
<div class="breadcrumbs">
  <a href="index.html">Chinese Notes 中文笔记</a> &gt; 
  <a href="topics_explorer.php">Word Explorer 探险单词</a> &gt; 
<?php
	print($title);
?>
</div>      
<?php
	print("<h1>$longtitleBr</h1>");
?>
<p class='source'>
  <a href="javascript:openVocab('/word_detail.php?id=2055');">点击</a><a href="javascript:openVocab('/word_detail.php?id=2056');">任何</a><a 
  href="javascript:openVocab('/word_detail.php?id=2057');">单词</a><a href="javascript:openVocab('/word_detail.php?id=604');">可以</a><a 
  href="javascript:openVocab('/word_detail.php?id=537');">看</a><a href="javascript:openVocab('/word_detail.php?id=2765');">例子</a>，<a 
  href="javascript:openVocab('/word_detail.php?id=2766');">笔记</a>，<a href="javascript:openVocab('/word_detail.php?id=2027');">或</a><a 
  href="javascript:openVocab('/word_detail.php?id=280');">听</a><a href="javascript:openVocab('/word_detail.php?id=2767');">录音</a>。<br/>
  Click on any word to see an example, notes, or listen to an MP3.<br/>
</p>
<table id='currencyTable'>
  <tbody id='currencyTabBody'>
    <tr>
      <th class="portlet">Simplified 简体</th>
      <th class="portlet">Traditional 繁体</th>
      <th class="portlet">Pinyin 拼音</th>
      <th class="portlet">English 英文</th>
      <th class="portlet">Grammar 语法</th>
      <th class="portlet">Notes 注释</th>
    </tr>
<?php
	foreach ($words as  $word) {
		$grammarEn = $word->getGrammar();
		$grammarCn = $grammarCnLookup[$grammarEn];
		print(
				'<tr>' . 
				"<td width='15%'>" . 
					"<a href='/word_detail.php?id=" . $word->getId() . "'>" .
					$word->getSimplified() . 
					'</a>' . 
				'</td>' . 
				"<td width='15%'>" . 
					"<a href='/word_detail.php?id=" . $word->getId() . "'>" .
					$word->getTraditional() . 
					'</a>' . 
				'</td>' . 
 				'<td>' . 
					$word->getPinyin() . 
				'</td>' . 
				'<td>' . 
					$word->getEnglish() . 
				'</td>' . 
				'<td>' . 
					$grammarCn . 
				'</td>' . 
				'<td>' . 
					$word->getNotes() . 
				'</td>' . 
				'</tr>' . 
				"\n");
	}
	
?>
  </tbody>
</table>
<br/>
<?php
  include "footer.txt";
?>
  </body>
</html>
