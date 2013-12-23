<?php
/**
 * Unit test for CharacterModel class.
 */
require dirname(__FILE__) . '/../../web/inc/radical_dao.php';

class RadicalTest extends PHPUnit_Framework_TestCase {

    public function testRadicalGetters() {
        $id = 22;
        $traditional = '人';
        $simplified = '人';
        $pinyin = 'rén';
        $strokes = 2;
        $simplifiedStrokes = 2;
        $otherForms = '亻 ⺅';
        $english = 'Person';
        $radical = new Radical($id, $traditional, $simplified, $pinyin, $strokes,
                               $simplifiedStrokes, $otherForms, $english);
        $this->assertEquals($id, $radical->getId());
        $this->assertEquals($traditional, $radical->getTraditional());
        $this->assertEquals($simplified, $radical->getSimplified());
        $this->assertEquals($pinyin, $radical->getPinyin());
        $this->assertEquals($strokes, $radical->getStrokes());
        $this->assertEquals($simplifiedStrokes, $radical->getSimplifiedStrokes());
        $this->assertEquals($otherForms, $radical->getOtherForms());
        $this->assertEquals($english, $radical->getEnglish());
    }

    public function testGetAllRadicals() {
        $radicalDAO = new RadicalDAO();
        $radicals = $radicalDAO->getAllRadicals();
        $radical = $radicals[14];
        $this->assertEquals(15, $radical->getId());
        $this->assertEquals('冫', $radical->getTraditional());
        $this->assertEquals('bīng', $radical->getPinyin());
        $this->assertEquals(2, $radical->getStrokes());
        $this->assertEquals('冰 氷', $radical->getOtherForms());
    }

    public function testGetRadical() {
        $radicalDAO = new RadicalDAO();
        $radical = $radicalDAO->getRadical('人');
        $this->assertEquals(9, $radical->getId());
        $this->assertEquals('人', $radical->getTraditional());
        $this->assertEquals('rén', $radical->getPinyin());
        $this->assertEquals(2, $radical->getStrokes());
        $this->assertEquals('亻 ⺅', $radical->getOtherForms());
        $this->assertEquals('Person', $radical->getEnglish());
    }
}
?>
