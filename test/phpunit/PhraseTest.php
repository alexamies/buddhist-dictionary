<?php
/**
 * Unit test for Phrase classe.
 */
require_once dirname(__FILE__) . '/../../web/inc/phrase.php';

class PhraseTest extends PHPUnit_Framework_TestCase {

    public function testGetChunks() {
        $text = '人类学';
        $outputType = 'traditional';
        $phrase = new Phrase($text, $outputType);
        $chunks = $phrase->getChunks();
        $this->assertEquals(1, count($chunks));
        $this->assertEquals($text, $chunks[0]->getText());
        $this->assertEquals(1, $chunks[0]->getType());
    }

    public function testGetPhraseElements1() {
        $text = '人类学';
        $outputType = 'traditional';
        $phrase = new Phrase($text, $outputType);
        $elements = $phrase->getPhraseElements();
        $this->assertEquals(1, count($elements));
        $this->assertEquals($text, $elements[0]->getText());
        $words = $elements[0]->getWords();
        $this->assertEquals(1, count($words));
        $this->assertEquals($text, $words[0]->getSimplified());
    }

    public function testGetPhraseElements2() {
        $text = '人类 学';
        $outputType = 'traditional';
        $phrase = new Phrase($text, $outputType);
        $elements = $phrase->getPhraseElements();
        $this->assertEquals(3, count($elements));
        $words1 = $elements[0]->getWords();
        $this->assertEquals('人类', $words1[0]->getSimplified());
        $this->assertEquals(0, $elements[1]->getType());
        $words3 = $elements[2]->getWords();
        $this->assertEquals('学', $words3[0]->getSimplified());
    }

    public function testGetPhraseElements3() {
        $text = '佛光山南天大學';
        $outputType = 'traditional';
        $phrase = new Phrase($text, $outputType);
        $elements = $phrase->getPhraseElements();
        $this->assertEquals(2, count($elements));
        $words1 = $elements[0]->getWords();
        $this->assertEquals('佛光山', $words1[0]->getSimplified());
        $words2 = $elements[1]->getWords();
        $this->assertEquals('南天大學', $words2[0]->getTraditional());
    }
}
