<?php
/**
 * Unit test for Topic and TopicDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/topic_dao.php';

class TopicTest extends PHPUnit_Framework_TestCase {

    public function testTopicGetters() {
        $simplified = '人类学';
        $english = 'Anthropology';
        $url = 'http://chinesenotes.com/ethnic_groups.php';
        $title = 'Chinese Ethnic Groups';
        $topic = new Topic($simplified, $english, $url, $title);
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
