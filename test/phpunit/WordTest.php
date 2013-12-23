<?php
/**
 * Unit test for Word and WordDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/words_dao.php';

class WordTest extends PHPUnit_Framework_TestCase {

    public function testWordGetters() {
        $word_id = 1444;
        $simplified = '民族';
        $traditional = NULL;
        $pinyin = 'mínzú';
        $english = 'nationality / ethnic group';
        $grammar = 'noun';
        $concept_cn = NULL;
        $concept_en = NULL;
        $topic_cn = '人类学';
        $topic_en = 'Anthropology';
        $parent_cn = NULL;
        $parent_en = NULL;
        $image = 'ewenke400.jpg';
        $mp3 = 'min2zu2.mp3';
        $notes = NULL;
        $word = new Word($word_id, $simplified, $traditional, $pinyin, $english, 
                         $grammar, $concept_cn, $concept_en, $topic_cn,
                         $topic_en, $parent_cn, $parent_en, $image, $mp3, $notes);
        $this->assertEquals($word_id, $word->getId());
        $this->assertEquals($simplified, $word->getSimplified());
        $this->assertEquals($traditional, $word->getTraditional());
        $this->assertEquals($english, $word->getEnglish());
        $this->assertEquals($grammar, $word->getGrammar());
        $this->assertEquals($concept_cn, $word->getConceptCn());
        $this->assertEquals($concept_en, $word->getConceptEn());
        $this->assertEquals($topic_cn, $word->getTopicCn());
        $this->assertEquals($topic_en, $word->getTopicEn());
        $this->assertEquals($parent_cn, $word->getParentCn());
        $this->assertEquals($parent_en, $word->getParentEn());
        $this->assertEquals($image, $word->getImage());
        $this->assertEquals($mp3, $word->getMp3());
        $this->assertEquals($notes, $word->getNotes());
    }

    public function testGetCountForTopic11() {
        $topic_en = 'Anthropology';
        $wordsDAO = new WordsDAO();
        $num = $wordsDAO->getCountForTopic($topic_en);
        $this->assertTrue($num > 0);
    }

    public function testGetCountForTopic2() {
        $topic_en = 'History';
        $wordsDAO = new WordsDAO();
        $num = $wordsDAO->getCountForTopic($topic_en);
        $this->assertTrue($num > 0);
    }

    public function testGetWords1() {
        $term = 'Anthropology';
        $matchType = 'exact';
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWords($term, $matchType);
        $this->assertTrue(count($words) > 0);
        $english = $words[0]->getEnglish();
        $this->assertTrue(stripos($english, $term) > -1);
    }

    public function testGetWords2() {
        $term = 'Anthropology';
        $matchType = 'not exact';
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWords($term, $matchType);
        $this->assertTrue(count($words) > 0);
        $english = $words[0]->getEnglish();
        $this->assertTrue(stripos($english, $term) > -1);
    }

    public function testGetWords3() {
        $term = '南朝梁';
        $matchType = 'exact';
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWords($term, $matchType);
        $this->assertTrue(count($words) > 0);
        $this->assertEquals($term, $words[0]->getSimplified());
    }

    public function testGetWordsByGrammar() {
        $grammar = 'noun';
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWordsByGrammar($grammar);
        $this->assertTrue(count($words) > 0);
        $this->assertEquals($grammar, $words[0]->getGrammar());
    }

    public function testGetWordsForConceptEn() {
        $conceptEn = 'Dynasty';
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWordsForConceptEn($conceptEn);
        $this->assertTrue(count($words) > 0);
        $this->assertEquals($conceptEn, $words[0]->getConceptEn());
    }

    public function testGetWordsForTopicEn() {
        $topicEn = 'History';
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWordsForTopicEn($topicEn);
        $this->assertTrue(count($words) > 0);
        $this->assertEquals($topicEn, $words[0]->getTopicEn());
    }

    public function testGetWordForId() {
        $word_id = 1444;
        $simplified = '民族';
        $traditional = NULL;
        $pinyin = 'mínzú';
        $english = 'nationality / ethnic group';
        $grammar = 'noun';
        $concept_cn = NULL;
        $concept_en = NULL;
        $topic_cn = '人类学';
        $topic_en = 'Anthropology';
        $parent_cn = NULL;
        $parent_en = NULL;
        $image = 'ewenke400.jpg';
        $mp3 = 'min2zu2.mp3';
        $notes = NULL;
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWordForId($word_id);
        $this->assertEquals(1, count($words));
        $word = $words[0];
        $this->assertEquals($word_id, $word->getId());
        $this->assertEquals($simplified, $word->getSimplified());
        $this->assertEquals($traditional, $word->getTraditional());
        $this->assertEquals($english, $word->getEnglish());
        $this->assertEquals($grammar, $word->getGrammar());
        $this->assertEquals($concept_cn, $word->getConceptCn());
        $this->assertEquals($concept_en, $word->getConceptEn());
        $this->assertEquals($topic_cn, $word->getTopicCn());
        $this->assertEquals($topic_en, $word->getTopicEn());
        $this->assertEquals($parent_cn, $word->getParentCn());
        $this->assertEquals($parent_en, $word->getParentEn());
        $this->assertEquals($image, $word->getImage());
        $this->assertEquals($mp3, $word->getMp3());
        $this->assertEquals($notes, $word->getNotes());
    }

    public function testGetWordForEnglish() {
        $word_id = 1444;
        $simplified = '民族';
        $traditional = NULL;
        $pinyin = 'mínzú';
        $english = 'nationality / ethnic group';
        $grammar = 'noun';
        $concept_cn = NULL;
        $concept_en = NULL;
        $topic_cn = '人类学';
        $topic_en = 'Anthropology';
        $parent_cn = NULL;
        $parent_en = NULL;
        $image = 'ewenke400.jpg';
        $mp3 = 'min2zu2.mp3';
        $notes = NULL;
        $wordsDAO = new WordsDAO();
        $words = $wordsDAO->getWordForEnglish($english);
        $this->assertEquals(1, count($words));
        $word = $words[0];
        $this->assertEquals($word_id, $word->getId());
        $this->assertEquals($simplified, $word->getSimplified());
        $this->assertEquals($traditional, $word->getTraditional());
        $this->assertEquals($english, $word->getEnglish());
        $this->assertEquals($grammar, $word->getGrammar());
        $this->assertEquals($concept_cn, $word->getConceptCn());
        $this->assertEquals($concept_en, $word->getConceptEn());
        $this->assertEquals($topic_cn, $word->getTopicCn());
        $this->assertEquals($topic_en, $word->getTopicEn());
        $this->assertEquals($parent_cn, $word->getParentCn());
        $this->assertEquals($parent_en, $word->getParentEn());
        $this->assertEquals($image, $word->getImage());
        $this->assertEquals($mp3, $word->getMp3());
        $this->assertEquals($notes, $word->getNotes());
    }

}
