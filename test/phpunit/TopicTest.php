<?php
/**
 * Unit test for Topic and TopicDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/topic_dao.php';

class TopicTest extends PHPUnit_Framework_TestCase {

    public function testTopicGetters() {
        $unicode = 12008;
        $c = '⻨';
        $pinyin = 'mài';
        $radical = '⻨';
        $strokes = 7;
        $otherStrokes = 0;
        $english = 'Wheat';
        $notes = 'CJK Radical C-Simplified Wheat';
        $type = 'radical';
        $diacritic = NULL;
        $charModel = new CharacterModel($unicode, $c,  $pinyin, $radical, $strokes,
                                        $otherStrokes, $english, $notes, $type, $diacritic);
        $this->assertEquals($unicode, $charModel->getUnicode());
        $this->assertEquals($c, $charModel->getC());
        $this->assertEquals($pinyin, $charModel->getPinyin());
        $this->assertEquals($radical, $charModel->getRadical());
        $this->assertEquals($strokes, $charModel->getStrokes());
        $this->assertEquals($otherStrokes, $charModel->getOtherStrokes());
        $this->assertEquals($english, $charModel->getEnglish());
        $this->assertEquals($notes, $charModel->getNotes());
        $this->assertEquals($type, $charModel->getType());
        $this->assertEquals($diacritic, $charModel->getDiacritic());
    }
}
