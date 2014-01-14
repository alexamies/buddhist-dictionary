<?php
/**
 * Unit test for ChineseText class.
 */
require_once dirname(__FILE__) . '/../../web/inc/chinesetext.php';

class ChineseTextTest extends PHPUnit_Framework_TestCase {

    public function testTextElements1() {
        $text = '觀自在菩薩';
        $chineseText = new ChineseText($text);
        $elements = $chineseText->getTextElements();
        $this->assertEquals(1, count($elements));
        $word1 = $elements[0]->getWord();
        $this->assertEquals($text, $word1->getTraditional());
    }

    public function testGetTextElements2() {
        $text = '觀自在菩薩行深';
        $chineseText = new ChineseText($text);
        $elements = $chineseText->getTextElements();
        $this->assertEquals(3, count($elements));
        $word1 = $elements[0]->getWord();
        $this->assertEquals('觀自在菩薩', $word1->getTraditional());
        $word2 = $elements[1]->getWord();
        $this->assertEquals('行', $word2->getSimplified());
    }

    public function testGetTextElements3() {
        $text = '度一切苦厄。';
        $chineseText = new ChineseText($text);
        $elements = $chineseText->getTextElements();
        $this->assertEquals(4, count($elements));
    }

    public function testGetTextElements4() {
        $text = '推进农业';
        $chineseText = new ChineseText($text, $langType='modern');
        $elements = $chineseText->getTextElements();
        $this->assertEquals(2, count($elements));
        $word1 = $elements[0]->getWord();
        $this->assertEquals('推进', $word1->getSimplified());
        $word2 = $elements[1]->getWord();
        $this->assertEquals('农业', $word2->getSimplified());
    }

    public function testGetTextElements5() {
        $text = '哆他';
        $chineseText = new ChineseText($text, $langType='literary');
        $elements = $chineseText->getTextElements();
        $this->assertEquals(2, count($elements));
        $word1 = $elements[0]->getWord();
        $this->assertEquals('哆', $word1->getSimplified());
        $word2 = $elements[1]->getWord();
        $this->assertEquals('他', $word2->getSimplified());
        $this->assertEquals(33559, $word2->getId());
    }
}
