<?php
/**
 * Unit test for Word and WordDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/word_dao.php';

class WordTest extends PHPUnit_Framework_TestCase {

    public function testWordGetters() {
        $word_id = 1444;
        $simplified = '民族';
        $traditional = '\\N';
        $pinyin = 'mínzú';
        $english = 'nationality / ethnic group';
        $grammar = 'noun';
        $concept_cn = '\\N';
        $concept_en = '\\N';
        $topic_cn = '人类学';
        $topic_en = 'Anthropology';
        $parent_cn = '\\N';
        $parent_en = '\\N';
        $image = 'ewenke400.jpg';
        $mp3 = 'min2zu2.mp3';
        $notes = '\\N';
        $topic = new Word($simplified, $english, $url, $title);
        $this->assertEquals($simplified, $topic->getSimplified());
        $this->assertEquals($english, $topic->getEnglish());
        $this->assertEquals($url, $topic->getUrl());
        $this->assertEquals($title, $topic->getTitle());
    }

    public function testGetAllTopics() {
        $topicDAO = new TopicDAO();
        $topics = $topicDAO->getAllTopics();
        $this->assertTrue(count($topics) > 1);
    }

    public function testGetTopicForEnglish() {
        $simplified = '人类学';
        $english = 'Anthropology';
        $url = 'http://chinesenotes.com/ethnic_groups.php';
        $title = 'Chinese Ethnic Groups';
        $topicDAO = new TopicDAO();
        $topic = $topicDAO->getTopicForEnglish($english);
        $this->assertTrue($topic != NULL);
        $this->assertEquals($simplified, $topic->getSimplified());
        $this->assertEquals($english, $topic->getEnglish());
        $this->assertEquals($url, $topic->getUrl());
        $this->assertEquals($title, $topic->getTitle());
    }
}
