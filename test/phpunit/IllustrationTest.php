<?php
/**
 * Unit test for Illustration class.
 */
require dirname(__FILE__) . '/../../web/inc/illustration_dao.php';

class IllustrationTest extends PHPUnit_Framework_TestCase {

    public function testIllustrationGetters() {
        $med_res = 'xuanzang400.jpg';
        $titleZhCn = '玄奘';
        $titleEn = 'Xuanzang';
        $author = 'Alex Amies';
        $authorURL = 'http://chinesenotes.com';
        $license = 'CCA';
        $licenseUrl = 'http://creativecommons.org/licenses/by/2.5/';
        $licenseFullName = 'Creative Commons with Attribution 2.5';
        $highResolution = 'xuanzang1000.jpg';
        $il = new Illustration($med_res, 
                           $titleZhCn, 
                           $titleEn, 
                           $author,
                           $authorURL,
                           $license,
                           $licenseUrl,
                           $licenseFullName,
                           $highResolution);
        $this->assertEquals($med_res, $il->getMediumResolution());
        $this->assertEquals($titleZhCn, $il->getTitleZhCn());
        $this->assertEquals($titleEn, $il->getTitleEn());
        $this->assertEquals($author, $il->getAuthor());
        $this->assertEquals($authorURL, $il->getAuthorURL());
        $this->assertEquals($license, $il->getLicense());
        $this->assertEquals($licenseUrl, $il->getLicenseUrl());
        $this->assertEquals($licenseFullName, $il->getLicenseFullName());
        $this->assertEquals($highResolution, $il->getHighResolution());
    }

    public function testGetAllIllustrations() {
        $illustrationDAO = new IllustrationDAO();
        $illustrations = $illustrationDAO->getAllIllustrations();
        $this->assertTrue(count($illustrations) > 0);
    }

    public function testGetAllIllustrationByMedRes() {
        $med_res = 'upper_left_dot.png';
        $illustrationDAO = new IllustrationDAO();
        $il = $illustrationDAO->getAllIllustrationByMedRes($med_res);
        $this->assertEquals($med_res, $il->getMediumResolution());
        $this->assertEquals('左上点', $il->getTitleZhCn());
        $this->assertEquals('Upper Left Dot', $il->getTitleEn());
        $this->assertEquals('Alex Amies', $il->getAuthor());
        $this->assertEquals('http://chinesenotes.com', $il->getAuthorURL());
        $this->assertEquals('CCA', $il->getLicense());
        $this->assertEquals('http://creativecommons.org/licenses/by/2.5/', $il->getLicenseUrl());
        $this->assertEquals('Creative Commons with Attribution 2.5', $il->getLicenseFullName());
    }
}
?>
