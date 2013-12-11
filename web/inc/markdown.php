<?php
/** 
 * Renders markdown into HTML.
 */
class Markdown {

  var $text;  // The markdown text

  /**
   * Constructor for a Markdown object
   *
   * @param $text   The plain text
   */
  function Markdown($text) {
    $this->text = $text;
  }

  /**
   * Accessor method for the HTML
   * @return A string value
   */
  function getHTML() {
    return $this->text;
  }
}
?>
