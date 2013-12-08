<?php
/**
 * Unit test for CharacterModel class.
 */
require_once dirname(__FILE__) . '/../../web/inc/character_rend_dao.php';

class CharacterRendModelTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
	$unicode = 11917;
	$fontNameEn = "Yan";
	$image = "yan/2e8d.png";
	$svg = "yan/2e8d.svg";
        $charRend = new CharacterRendModel($unicode, $fontNameEn,  $image, $svg);
        $this->assertEquals($unicode, $charRend->getUnicode());
        $this->assertEquals($fontNameEn, $charRend->getFontNameEn());
        $this->assertEquals($image, $charRend->getImage());
        $this->assertEquals($svg, $charRend->getSvg());
    }

    public function testGetCharacterRendByUnicode() {
        $unicode = 11917;
        $characterRendDAO = new CharacterRendDAO();
	$characterRendModel = $characterRendDAO->getCharacterRendByUnicode($unicode);
        $this->assertEquals($unicode, $characterRendModel->getUnicode());
        $this->assertEquals('Yan', $characterRendModel->getFontNameEn());
        $this->assertEquals('yan/2e8d.png', $characterRendModel->getImage());
        $this->assertEquals('yan/2e8d.svg', $characterRendModel->getSvg());
    }
}
?>
