<?php
/**
 * Unit test for CharacterModel class.
 */
require dirname(__FILE__) . '/../../web/inc/sanskrit_model.php';

class SuggestionTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
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
        $sanskrit = new Suggestion($id, $word_id, $latin, $iast, $devan, $pali, $traditional, 
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
}
?>
