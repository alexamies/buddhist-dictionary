<?php
/**
 * Unit test for ChineseText class.
 */
require_once dirname(__FILE__) . '/../../web/inc/chinesetext.php';

class ChineseTextTest extends PHPUnit_Framework_TestCase {

    public function testGetPhraseElements1() {
        $text = '觀自在菩薩';
        $chineseText = new ChineseText($text);
        $elements = $chineseText->getTextElements();
        $this->assertEquals(1, count($elements));
    }

    public function testGetPhraseElements2() {
        $text = '觀自在菩薩行深';
        $chineseText = new ChineseText($text);
        $elements = $chineseText->getTextElements();
        $this->assertEquals(3, count($elements));
    }

    public function testGetPhraseElements3() {
        $text = '度一切苦厄。';
        $chineseText = new ChineseText($text);
        $elements = $chineseText->getTextElements();
        $this->assertEquals(4, count($elements));
    }
}
