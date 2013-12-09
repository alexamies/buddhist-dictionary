<?php
/**
 * Unit test for Character, CharacterModel, CharacterDAO, and VariantChar classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/character_dao.php';

class CharacterModelTest extends PHPUnit_Framework_TestCase {

    public function testCharacterModelGetters() {
        $unicode = 12008;
        $c = '⻨';
        $pinyin = 'mài';
        $radical = '⻨';
        $strokes = 7;
        $otherStrokes = 0;
        $english = 'Wheat';
        $notes = 'CJK Radical C-Simplified Wheat';
        $type = 'radical';
        $diacritic = NULL;
        $charModel = new CharacterModel($unicode, $c,  $pinyin, $radical, $strokes,
                                        $otherStrokes, $english, $notes, $type, $diacritic);
        $this->assertEquals($unicode, $charModel->getUnicode());
        $this->assertEquals($c, $charModel->getC());
        $this->assertEquals($pinyin, $charModel->getPinyin());
        $this->assertEquals($radical, $charModel->getRadical());
        $this->assertEquals($strokes, $charModel->getStrokes());
        $this->assertEquals($otherStrokes, $charModel->getOtherStrokes());
        $this->assertEquals($english, $charModel->getEnglish());
        $this->assertEquals($notes, $charModel->getNotes());
        $this->assertEquals($type, $charModel->getType());
        $this->assertEquals($diacritic, $charModel->getDiacritic());
    }

    public function testCharacterGetIntCode() {
        $character = new Character('!');
        $this->assertEquals(33, $character->getIntCode());

        $character = new Character('⻨');
        $this->assertEquals(12008, $character->getIntCode());
    }

    public function testCharacterIsCJKLetter() {
        $character1 = new Character('⻨');
        $this->assertEquals(TRUE, $character1->isCJKLetter());

        $character2 = new Character('一');
        $this->assertEquals(TRUE, $character2->isCJKLetter());

        $character3 = new Character('A');
        $this->assertEquals(FALSE, $character3->isCJKLetter());
    }

    public function testCharacterIsPunctuation() {
        $character1 = new Character('⻨');
        $this->assertEquals(FALSE, $character1->isPunctuation());

        $character1 = new Character('。');
        $this->assertEquals(TRUE, $character1->isPunctuation());
    }

    public function testGetCharacterByValue1() {
	$characterDAO = new CharacterDAO();
	$character = $characterDAO->getCharacterByValue("⺀");
        $this->assertEquals(11904, $character->getUnicode());
        $this->assertEquals("⺀", $character->getC());
        $this->assertEquals('dié', $character->getPinyin());
        $this->assertEquals(2, $character->getStrokes());
        $this->assertEquals(0, $character->getOtherStrokes());
        $this->assertEquals('Repeat', $character->getEnglish());
        $this->assertTrue(strlen($character->getNotes()) > 0);
        $this->assertEquals('radical', $character->getType());
        $this->assertEquals(0, count($character->getVariants()));
    }

    public function testGetCharacterByValue2() {
	$characterDAO = new CharacterDAO();
	$character = $characterDAO->getCharacterByValue('导');
        $this->assertEquals(23548, $character->getUnicode());
        $this->assertEquals('导', $character->getC());
        $this->assertEquals('dǎo dào', $character->getPinyin());
        $this->assertEquals(6, $character->getStrokes());
        $this->assertEquals(3, $character->getOtherStrokes());
        $this->assertTrue(strlen($character->getEnglish()) > 0);
        $this->assertEquals(NULL, $character->getNotes());
        $this->assertEquals('simplified', $character->getType());
        $variants = $character->getVariants();
        $this->assertEquals(1, count($variants));
        $variant = $variants[0];
        $this->assertEquals('导', $variant->getC1());
        $this->assertEquals('導', $variant->getC2());
        $this->assertEquals('Traditional', $variant->getRelationType());
    }

    public function testCharacterByUnicode() {
	$characterDAO = new CharacterDAO();
	$character = $characterDAO->getCharacterByUnicode(23548);
        $this->assertEquals(23548, $character->getUnicode());
        $this->assertEquals('导', $character->getC());
        $this->assertEquals('dǎo dào', $character->getPinyin());
        $this->assertEquals(6, $character->getStrokes());
        $this->assertEquals(3, $character->getOtherStrokes());
        $this->assertTrue(strlen($character->getEnglish()) > 0);
        $this->assertEquals(NULL, $character->getNotes());
        $this->assertEquals('simplified', $character->getType());
        $variants = $character->getVariants();
        $this->assertEquals(1, count($variants));
        $variant = $variants[0];
        $this->assertEquals('导', $variant->getC1());
        $this->assertEquals('導', $variant->getC2());
        $this->assertEquals('Traditional', $variant->getRelationType());
    }

    public function testCharactersByRadicals() {
	$characterDAO = new CharacterDAO();
	$characters = $characterDAO->getCharactersByRadicals('人');
        $this->assertTrue(count($characters) > 0);
    }

    public function testCharactersByValue() {
	$characterDAO = new CharacterDAO();
	$characters = $characterDAO->getCharactersByValue('汉英词典');
        $this->assertTrue(count($characters) == 4);
        $this->assertEquals('汉', $characters[0]->getC());
        $this->assertEquals('英', $characters[1]->getC());
        $this->assertEquals('词', $characters[2]->getC());
        $this->assertEquals('典', $characters[3]->getC());
    }

    public function testVariantCharGetters() {
        $c1 = '导';
        $c2 = '導';
        $relationType = 'Traditional';
        $variant = new VariantChar($c1, $c2, $relationType);
        $this->assertEquals($c1, $variant->getC1());
        $this->assertEquals($c2, $variant->getC2());
        $this->assertEquals($relationType, $variant->getRelationType());
    }

    // TO DO: add variant dao tests

}
?>
