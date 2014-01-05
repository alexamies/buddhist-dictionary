<?php
/**
 * Unit test for PhraseDAO classes.
 */
require_once dirname(__FILE__) . '/../../web/inc/phrase_dao.php';

class PhraseTest extends PHPUnit_Framework_TestCase {

    public function testGetPhrase() {
        $id = 1;
        $chinese_phrase = "何以故";
        $pos_tagged = "何/DT[hé why] 以/P[yǐ | because] 故/NN[gù | purpose] <why?>";
        $sanskrit = "tatkasya hetoḥ";
        $source_no = 2;
        $source_name = "Diamond Sūtra";
        $dao = new PhraseDAO();
        $phrase = $dao->getPhrase($id);
        $this->assertTrue($phrase != null);
        $this->assertEquals($id, $phrase->getId());
        $this->assertEquals($chinese_phrase, $phrase->getChinesePhrase());
        $this->assertEquals($pos_tagged, $phrase->getPosTagged());
        $this->assertEquals($sanskrit, $phrase->getSanskrit());
        $this->assertEquals($source_no, $phrase->getSourceNo());
        $this->assertEquals($source_name, $phrase->getSourceName());
    }
}
