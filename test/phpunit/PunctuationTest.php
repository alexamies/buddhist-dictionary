<?php
/**
 * Unit test for Punctuation class.
 */
require_once dirname(__FILE__) . '/../../web/inc/punctuation.php';

class PunctuationTest extends PHPUnit_Framework_TestCase {

    public function testAllMethods1() {
        $c = '人';
        $punctuation = new Punctuation($c);
        $this->assertEquals(FALSE, $punctuation->isPunctuation());
    }

    public function testAllMethods2() {
        $c = '。';
        $punctuation = new Punctuation($c);
        $this->assertEquals('.', $punctuation->getASCIIReplacement());
        $this->assertEquals(TRUE, $punctuation->isPunctuation());
    }

}
