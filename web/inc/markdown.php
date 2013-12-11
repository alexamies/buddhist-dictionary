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
  public function Markdown($text) {
    $this->text = $text;
  }

  /**
   * Accessor method for the HTML
   * @return A string value
   */
  public function getHTML() {
    
    $html = preg_replace('{^\xEF\xBB\xBF|\x1A}', '', $this->text);  // Replace BOM
    $html = preg_replace('{\r\n?}', "\n", $html);  // Mac and Windows to Unix linebreaks

    $html = $this->replaceHeaders($html);
    $html = $this->formParagraphs($html);

    return $html;
  }

  /**
   * Form paragraphs from blank lines
   *
   * @return A string value
   */
  protected function formParagraphs($html) {
    $html = preg_replace('{^(.*)\n\s*\n}m', "<p>$1</p>", $html);
    return $html;
  }

  /**
   * H1 and H2 Headers -> H2 headers
   *
   * @return A string value
   */
  protected function replaceHeaders($text) {
    $html = preg_replace('{^(\#{1,2})[ ]+(.+?)[ ]*\#*\n+}xm', "<h2>$2</h2>\n", $text);  
    $html = preg_replace('{^(\#{3})[ ]+(.+?)[ ]*\#*\n+}xm', "<h3>$2</h3>\n", $html);
    return $html;
  }

}
?>
