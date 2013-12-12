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
        $text = '[an example](http://example.com/ title="Title")';
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = '<a href="http://example.com/" title="Title">an example</a>';
        $this->assertEquals($expected, $html);
    }

    public function testLink2() {
        $text = "[an example](http://example.com/ title='Title')";
        $markdown = new Markdown($text);
        $html = $markdown->getHTML();
        $expected = '<a href="http://example.com/" title="Title">an example</a>';
        $this->assertEquals($expected, $html);
    }

}
