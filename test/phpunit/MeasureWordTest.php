<?php
/**
 * Unit test for MeasureWord and MeasureWordDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/measure_word_dao.php';

class MeasureWordTest extends PHPUnit_Framework_TestCase {

    public function testTopicGetters() {
        $mwId = 1531;
        $mwSimplified = '把';
        $mwTraditional = NULL;
        $mwPinyin = 'bǎ';
        $mwEnglish = 'Measure word for chairs, bunches of things, etc';
        $mw = new MeasureWord($mwId, $mwSimplified, $mwTraditional, $mwPinyin, 
                              $mwEnglish);
        $this->assertEquals($mwId, $mw->getMwId());
        $this->assertEquals($mwSimplified, $mw->getMwSimplified());
        $this->assertEquals($mwTraditional, $mw->getMwTraditional());
        $this->assertEquals($mwPinyin, $mw->getMwPinyin());
        $this->assertEquals($mwEnglish, $mw->getMwEnglish());
    }

    public function testGetAllMeasureWords() {
        $dao = new MeasureWordDAO();
        $mws = $dao->getAllMeasureWords();
        $this->assertTrue(count($mws) > 1);
    }

    public function testGetMeasureWordsForNoun() {
        $dao = new MeasureWordDAO();
        $mws = $dao->getMeasureWordsForNoun('刀子');
        $this->assertTrue(count($mws) > 0);
    }

    public function testGetNounsForMeasureWord() {
        $dao = new MeasureWordDAO();
        $entries = $dao->getNounsForMeasureWord('把');
        $this->assertTrue(count($entries) > 0);
    }
}
