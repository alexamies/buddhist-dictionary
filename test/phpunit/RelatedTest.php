<?php
/**
 * Unit test for Related and RelatedDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/related_dao.php';

class RelatedTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
        $simplified1 = '买';
        $simplified2 = '买到';
        $note = 'Verb-complement phrase';
        $link = 'grammar_sentence_elements.php#complements';
        $related = new Related($simplified1, $simplified2, $note, $link);
        $this->assertEquals($simplified1, $related->getSimplified1());
        $this->assertEquals($simplified2, $related->getSimplified2());
        $this->assertEquals($note, $related->getNote());
        $this->assertEquals($link, $related->getLink());
    }

    public function testGetRelated() {
        $simplified1 = '买';
        $dao = new RelatedDAO($simplified1, $simplified2);
        $words = $dao->getRelated($simplified1);
        $this->assertTrue(count($words) > 0);
    }
}
