<?php
/**
 * Unit test for CharacterModel class.
 */
require dirname(__FILE__) . '/../../web/inc/radical_model.php';

class RadicalTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
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
}
?>
