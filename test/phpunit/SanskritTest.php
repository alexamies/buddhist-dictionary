<?php
/**
 * Unit tests for Sanskri, SanskritDAO, and Suggestion classes.
 */
//require_once dirname(__FILE__) . '/../../web/inc/sanskrit_model.php';
require_once dirname(__FILE__) . '/../../web/inc/sanskrit_dao.php';

class SanskritTest extends PHPUnit_Framework_TestCase {

    public function testSanskritGetters() {
        $id = 818;
        $word_id = 541;
        $latin = 'vadhvah';
        $iast = 'vadhvāḥ';
        $devan = 'वध्वाः';
        $pali = NULL;
        $traditional = '女人';
        $english = 'a woman';
        $notes = 'Singular genetive form';
        $grammar = 'feminine';
        $root = NULL;
        $sanskrit = new Sanskrit($id, $word_id, $latin, $iast, $devan, $pali, $traditional, 
                                 $english, $notes, $grammar, $root);
        $this->assertEquals($id, $sanskrit->getId());
        $this->assertEquals($word_id, $sanskrit->getWordId());
        $this->assertEquals($latin, $sanskrit->getLatin());
        $this->assertEquals($iast, $sanskrit->getIast());
        $this->assertEquals($devan, $sanskrit->getDevan());
        $this->assertEquals($pali, $sanskrit->getPali());
        $this->assertEquals($traditional, $sanskrit->getTraditional());
        $this->assertEquals($english, $sanskrit->getEnglish());
        $this->assertEquals($notes, $sanskrit->getNotes());
        $this->assertEquals($grammar, $sanskrit->getGrammar());
        $this->assertEquals($root, $sanskrit->getRoot());
    }

    public function testGetSanskritByID() {
        $sanskritDAO = new SanskritDAO();
	$sanskrit = $sanskritDAO->getSanskritByID(27);
        $this->assertEquals(27, $sanskrit->getId());
        $this->assertEquals(23092, $sanskrit->getWordId());
        $this->assertEquals('asoka', $sanskrit->getLatin());
        $this->assertEquals('aśoka', $sanskrit->getIast());
        $this->assertEquals(NULL, $sanskrit->getPali());
        $this->assertEquals('阿育王', $sanskrit->getTraditional());
        $this->assertEquals('Ashoka', $sanskrit->getEnglish());
        $this->assertTrue(strlen($sanskrit->getNotes()) > 0);
        $this->assertEquals('proper_noun', $sanskrit->getGrammar());
        $this->assertEquals(NULL, $sanskrit->getRoot());
    }

    public function testGetSanskrit() {
        $sanskritDAO = new SanskritDAO();
        $words = $sanskritDAO->getSanskrit('Heart Sutra');
        $this->assertEquals(1, count($words));
        $word = $words[0];
        $this->assertEquals(17, $word->getId());
        $this->assertEquals(5042, $word->getWordId());
        $this->assertEquals('prajnaparamitahrdayasutram', $word->getLatin());
        $this->assertEquals('prajñāpāramitāhṛdayasutram', $word->getIast());
        $this->assertEquals('प्रज्ञापारमिताहृदयसुत्रम्', $word->getDevan());
        $this->assertEquals(NULL, $word->getPali());
        $this->assertEquals('般若波羅蜜多心經', $word->getTraditional());
        $this->assertTrue(strlen($word->getEnglish()) > 0);
        $this->assertEquals(NULL, $word->getNotes());
        $this->assertEquals('proper_noun', $word->getGrammar());
        $this->assertEquals(NULL, $word->getRoot());
    }

    public function testSuggest() {
        $sanskritDAO = new SanskritDAO();
        $suggestions = $sanskritDAO->suggest('bhavasi');
        $this->assertEquals(1, count($suggestions));
        $suggestion = $suggestions[0];
        $this->assertEquals('bhava', $suggestion->getAlternate());
    }

    public function testSuggestGetters() {
        $alternate = 'bhava';
        $reason = 'Reduce to stem form';
        $sanskrit = new Suggestion($alternate, $reason);
        $this->assertEquals($alternate, $sanskrit->getAlternate());
        $this->assertEquals($reason, $sanskrit->getReason());
    }
}

?>
