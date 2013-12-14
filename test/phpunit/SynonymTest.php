<?php
/**
 * Unit test for Synonym and SynonymDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/synonym_dao.php';

class SynonymTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
        $simplified1 = '佛塔';
        $simplified2 = '塔';
        $synonym = new Synonym($simplified1, $simplified2);
        $this->assertEquals($simplified1, $synonym->getSimplified1());
        $this->assertEquals($simplified2, $synonym->getSimplified2());
    }

    public function testGetSynonyms() {
        $simplified1 = '佛塔';
        $dao = new SynonymDAO($simplified1, $simplified2);
        $words = $dao->getSynonyms($simplified1);
        $this->assertTrue(count($words) > 0);
    }
}
