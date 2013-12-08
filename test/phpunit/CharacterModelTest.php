<?php
/**
 * Unit test for CharacterModel class.
 */
require dirname(__FILE__) . '/../../web/inc/character.php';

class CharacterModelTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
        $unicode = 12008;
        $c = '⻨';
        $pinyin = 'mài';
        $radical = '⻨';
        $strokes = 'http://chinesenotes.com';
        $license = 'CCA';
        $licenseUrl = 'http://creativecommons.org/licenses/by/2.5/';
        $licenseFullName = 'Creative Commons with Attribution 2.5';
        $highResolution = 'xuanzang1000.jpg';
        $charModel = new CharacterModel($unicode, 
                           $c, 
                           $pinyin, 
                           $radical,
                           $strokes,
                           $license,
                           $licenseUrl,
                           $licenseFullName,
                           $highResolution);
        $this->assertEquals($unicode, $charModel->getUnicode());
        $this->assertEquals($c, $charModel->getC());
        $this->assertEquals($pinyin, $charModel->getPinyin());
        $this->assertEquals($radical, $charModel->getRadical());
        $this->assertEquals($strokes, $charModel->getStrokes());
        $this->assertEquals($license, $charModel->getLicense());
        $this->assertEquals($licenseUrl, $charModel->getLicenseUrl());
        $this->assertEquals($licenseFullName, $charModel->getLicenseFullName());
        $this->assertEquals($highResolution, $charModel->getHighResolution());
    }
}
?>
