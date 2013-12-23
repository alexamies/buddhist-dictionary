<?php
/**
 * Unit test for Markdown class.
 */
require_once dirname(__FILE__) . '/../../web/inc/markdown.php';

class MarkdownTest extends PHPUnit_Framework_TestCase {

    public function testTrivial() {
        $text = 'Diamond Sutra Chapter 1 Sanskrit Text';
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $this->assertTrue(strlen($html) > 0);
        $this->assertTrue(strpos($html, $text) > -1);
    }

    public function testParagraphs1() {
        $text = "Hello\n\n";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $this->assertTrue(strpos($html, '<p>Hello</p>') > -1);
    }

    public function testParagraphs2() {
        $text = "Good bye\n \n";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $this->assertTrue(strpos($html, '<p>Good bye</p>') > -1);
    }

    public function testLinks1() {
        $text = '[an example](http://example.com/ "Title")';
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = '<a href="http://example.com/" title="Title">an example</a>';
        $this->assertEquals($expected, $html);
    }

    public function testLink2() {
        $text = "[an example](http://example.com/ 'Title')";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = '<a href="http://example.com/" title="Title">an example</a>';
        $this->assertEquals($expected, $html);
    }

    public function testLink3() {
        $text = '[University of the West Sanskrit Buddhist Canon](http://www.dsbcproject.org./node/6348/ "Sanskrit Buddhist Canon")';
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = '<a href="http://www.dsbcproject.org./node/6348/" title="Sanskrit Buddhist Canon">University of the West Sanskrit Buddhist Canon</a>';
        $this->assertEquals($expected, $html);
    }

    public function testLink4() {
        $text = "[an example](http://example.com/ 'Title')\n[an example 2](http://example.com/ 'Title 2')";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = "<a href=\"http://example.com/\" title=\"Title\">an example</a>\n" .
                    "<a href=\"http://example.com/\" title=\"Title 2\">an example 2</a>";
        $this->assertEquals($expected, $html);
    }

    public function testCBETA1() {
        $text = "T08n0235_p0748c15(00)║\n";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = "T08n0235_p0748c15(00)║<br/>\n";
        $this->assertEquals($expected, $html);
    }

    public function testCBETA2() {
        $text = "【經錄部類】〔般若部類〕〔般若部〕\n";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = "【經錄部類】〔般若部類〕〔般若部〕<br/>\n";
        $this->assertEquals($expected, $html);
    }

    public function testCBETA3() {
        $text = "【T08n0235_p0748c15(00)║\n" .
                "T08n0235_p0748c16(00)║　　No. 235 [Nos. 220(9), 236-239]\n";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = "【T08n0235_p0748c15(00)║<br/>\n" .
                    "T08n0235_p0748c16(00)║　　No. 235 [Nos. 220(9), 236-239]<br/>\n";
        $this->assertEquals($expected, $html);
    }

    public function testPhraseGloss() {
        $text = '當此, 當/P[at] 此/PN[this] <at that time>';
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = '當此, 當/P[at] 此/PN[this] &lt;at that time&gt;';
        $this->assertEquals($expected, $html);
    }

}
