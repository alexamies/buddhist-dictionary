<?php
require_once 'inc/phrase.php' ;
  	require_once 'inc/grammar_lookup.php';
  	
	mb_internal_encoding('UTF-8');
	setlocale(LC_ALL, 'Chinese_china', 'zh_CN');
	
	header('Content-Type: text/html;charset=utf-8');
	
	function utf8_urldecode($str) {
    	$str = preg_replace("/%u([0-9a-f]{3,4})/i","&#x\\1;",urldecode($str));
    	return html_entity_decode($str,null,'UTF-8');;
  	}

	// Session variables used for the breadcrumbs
	session_start();
	$conceptTitle = '句子查阅 sentence Lookup';
	$_SESSION['conceptTitle'] = $conceptTitle;
	$script = $_SERVER['SCRIPT_NAME'];
	$conceptURL = $script;
	$_SESSION['conceptURL'] = $conceptURL;

  	require_once 'inc/words_dao.php' ;

	if (isset($_REQUEST['sentence'])) {
		$text = utf8_urldecode($_REQUEST['sentence']);
		$_SESSION['sentence'] = $text;
	} else if (isset($_SESSION['sentence'])) {
		$text = $_SESSION['sentence'];
	} else {
		$text = '';
	}
	//error_log("sentence_lookup.php text length: " . strlen($text));
	
	// Output type
	$outputType = 'traditional';
	if (isset($_REQUEST['outputType'])) {
	    $outputType = $_REQUEST['outputType'];
	}

?>
<?php

	$phrase = new Phrase($text, $outputType);
	$phraseElements = $phrase->getPhraseElements();
	//$num = count($phraseElements);
	//print("<p>Phrase elements ($num):</p>\n");
	print("<table id='resultsTable'><tbody>\n");
	print("<tr>");
	print("  <th>Input Chinese <span class='cn'><br/>输入中文</span></th>");
	print("  <th>Simplified <span class='cn'><br/>简体</span></th>");
	print("  <th>Traditional <span class='cn'><br/>繁体</span></th>");
	print("  <th>Pinyin <span class='cn'><br/>拼音</span></th>");
	print("  <th>English <span class='cn'><br/>英文</span></th>");
	print("  <th>Grammar <span class='cn'><br/>语法</span></th>");
	print("  <th>Notes <span class='cn'><br/>注释</span></th>");
	print("</tr>\n");

	foreach ($phraseElements as $phraseElement) {
		$elemText = $phraseElement->getText();
		$type = $phraseElement->getType();
		if ($type == 0) {
			// Non CJK text (punctuation, etc) 
			print("<tr><td>$elemText</td><td colspan='4'>&nbsp;</td></tr>\n");

		} else if ($type == 1) {
			// Single matching word

			$words = $phraseElement->getWords();
			$word = $words[0];
			$id = $word->getId();
			$simplified = "<a href='/word_detail.php?id=" . $id . "'><span class='simplified'>" . 
 					$word->getSimplified() . "</span></a>";
			$traditional = "<span class='traditional'>" . $word->getTraditional() . "</span>";
			$pinyin = $word->getPinyin();
			$grammar = $word->getGrammar();
			$english = $word->getEnglish();
			//error_log("English: $english , Grammar: $grammar");
			$grammarCn = $grammarCnLookup[$grammar];
			$notes = $word->getNotes();
			print(
					"<tr>\n" .
					"  <td>$elemText</td>" .
					"  <td>$simplified</td>" .
					"  <td>$traditional</td>" .
					"  <td>$pinyin</td>" .
					"  <td>$english</td>" .
					"  <td>$grammarCn</td>" .
					"  <td>$notes</td>" .
					"</tr>\n"
					);
		} else if ($type == 2) {
			// Multiple Words

			$words = $phraseElement->getWords();
			$numWords = count($words);
			//error_log("Multiple Words ($numWords)");

			$inputText = "<td rowspan='$numWords'>$elemText</td>";
			foreach ($words as $word) {
				$id = $word->getId();
				$simplified = "<a href='/word_detail.php?id=" . $id . "'><span class='simplified'>" . 
                		$word->getSimplified() . "</span></a>";
				$traditional = "<span class='traditional'>" . $word->getTraditional() . "</span>";
				$pinyin = $word->getPinyin();
				$grammar = $word->getGrammar();
				$grammarCn = $grammarCnLookup[$grammar];
				$english = $word->getEnglish();
				$notes = $word->getNotes();
				if ($inputText != '') {
					print("<tr class='selectedRow'>");
					print($inputText);
					$inputText = '';
				} else {
					print("<tr>\n");
				}
				print("  <td>$simplified</td>");
				print("  <td>$traditional</td>");
				print("  <td>$pinyin</td>");
				print("  <td>$english</td>");
				print("  <td>$grammarCn</td>");
				print("  <td>$notes</td>");
				print("</tr>\n");
			}

			print("</tr>\n");

		} else if ($type == 3) {
			print("<tr><td>$elemText</td><td colspan='5'>Unknown character</td></tr>\n");
		}
	}
	print("</tbody></table>\n");

	// Print out pinyin for the phrase
	$pinyin = $phrase->getPinyin();
	print("<p>$pinyin</p>");

	// Print out HTML for the phrase
	$html = $phrase->getHtml();
	print(
		"<h4>HTML Links and Mouseover for Chinese Words " .
		"<a href='#' onclick=\"openVocab('/help_html.php');\">?</a></h4>" .
		"<p>$html</p>" .
		"<p><textarea cols='120' rows='3'>$html</textarea></p>" .
    	"<div>" .
      	"<span id='toolTip'><span id='pinyinSpan'>Pinyin</span> <span id='englishSpan'>English</span></span>" .
    	"</div>"
		);

	// print out chunks
	/*
	$chunks = $phrase->getChunks();
	print("<p>Chunks:</p>");
	foreach ($chunks as $chunk) {
		$chunkText = $chunk->getText();
		print("<p>$chunkText</p>");
	}
	*/

?>  
