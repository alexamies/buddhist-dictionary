<?php
/**
 * Unit test for CharacterModel class.
 */
require dirname(__FILE__) . '/../../web/inc/variant_model.php';

class VariantCharTest extends PHPUnit_Framework_TestCase {

    public function testGetters() {
        $c1 = '导';
        $c2 = '導';
        $relationType = 'Traditional';
        $variant = new VariantChar($c1, $c2, $relationType);
        $this->assertEquals($c1, $sanskrit->getC1());
        $this->assertEquals($c2, $sanskrit->getC2());
        $this->assertEquals($relationType, $sanskrit->getRelationType());
    }
}
?>
