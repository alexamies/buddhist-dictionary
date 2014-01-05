<?php
/** 
 * An object encapsulating phrase memory entries.
 */
class Phrase {
    var $id;             // An id for the phrase entry
    var $chinese_phrase; // Simplified Chinese text for the related word or phrase
    var $pos_tagged;     // The phrase tagged with PoS tags, including word and phrase gloss
    var $sanskrit;       // The Sanskrit equivalent, if known
    var $source_no;      // The id of the corpus source document
    var $source_name;    // The name of the source document

    /**
     * Constructor for a Phrase object
     *
     * @param $id	       An id for the phrase entry
     * @param $chinese_phrase  Plain text Chinese
     * @param $pos_tagged      The phrase tagged with PoS tags, including word and phrase gloss
     * @param $sanskrit	       The Sanskrit equivalent, if known
     * @param $source_no       The id of the corpus source document
     * @param $source_name     The name of the source document
     */
    function Phrase ($id, $chinese_phrase, $pos_tagged, $sanskrit, $source_no, $source_name) {
      $this->id = $id;
      $this->chinese_phrase = $chinese_phrase;
      $this->pos_tagged = $pos_tagged;
      $this->sanskrit = $sanskrit;
      $this->source_no = $source_no;
      $this->source_name = $source_name;
    }

    /**
     * Accessor method for the id for the phrase entry
     *
     * @return an integer value
     */
    function getId() {
        return $this->id;
    }

    /**
     * Accessor method for the plain text Chinese
     *
     * @return a string value
     */
    function getChinesePhrase() {
        return $this->chinese_phrase;
    }

    /**
     * Accessor method for the phrase tagged with PoS tags, including word and phrase gloss
     *
     * @return a string value
     */
    function getPosTagged() {
        return $this->pos_tagged;
    }

    /**
     * Accessor method for the Sanskrit equivalent, if known
     *
     * @return a string value or null
     */
    function getSanskrit() {
        return $this->sanskrit;
    }

    /**
     * Accessor method for the id of the corpus source document
     *
     * @return an integer value
     */
    function getSourceNo() {
        return $this->source_no;
    }

    /**
     * Accessor method for the name of the source document
     *
     * @return a string value
     */
    function getSourceName() {
        return $this->source_name;
    }
}
?>
