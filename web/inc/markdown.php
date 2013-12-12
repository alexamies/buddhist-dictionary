<?php
/** 
 * Renders markdown into HTML. At the moment the set support is a subset of the markdown 
 * described at http://daringfireball.net/projects/markdown/syntax .
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
   * Accessor method for the HTML.
   *
   * This is the method that a client should call to transform markdown to HTML.
   *
   * @return A string value
   */
  public function getHTML() {
    $html = $this->prepareDoc($this->text);
    $html = $this->replaceHeaders($html);
    $html = $this->formParagraphs($html);
    $html = $this->replaceLinks($html);
    return $html;
  }

  /**
   * Form paragraphs from blank lines.
   *
   * @return A string value
   */
  protected function formParagraphs($text) {
    $html = preg_replace('{^(.*)\n\s*\n}m', "<p>$1</p>", $text);
    return $html;
  }

  /**
   * Basic formatting of doc.
   *
   * Replace BOM, Mac and Windows to Unix linebreaks
   *
   * @return A string value
   */
  protected function prepareDoc($text) {
    $text = preg_replace('{^\xEF\xBB\xBF|\x1A}', '', $text);
    $text = preg_replace('{\r\n?}', "\n", $text);
    return $text;
  }

  /**
   * Replace markdown style headers with HTML.
   *
   * H1 and H2 Headers are both mapped to H2 headers
   * So far the only markdown styles supported are:
   *
   * # Header 1
   * ## Header 2
   *
   * @return A string value
   */
  protected function replaceHeaders($text) {
    $html = preg_replace('{^(\#{1,2})[ ]+(.+?)[ ]*\#*\n+}xm', "<h2>$2</h2>\n", $text);  
    $html = preg_replace('{^(\#{3})[ ]+(.+?)[ ]*\#*\n+}xm', "<h3>$2</h3>\n", $html);
    return $html;
  }

  /**
   * Replace markdown style headers with HTML.
   *
   * The style of markdown links supported is
   * [an example](http://example.com/ "Title")
   *
   * It will be replaced with 
   *
   * <a href='http://example.com/' title="Title">an example</a>
   *
   * @return A string value
   */
  protected function replaceLinks($markdown) {
    $html = preg_replace('{\[(.*)\]\s*\((.*)\stitle="(.*)"\)}xm', 
                         '<a href="$2" title="$3">$1</a>', 
                         $markdown);  
    $html = preg_replace('{\[(.*)\]\s*\((.*)\stitle=\'(.*)\'\)}xm', 
                         '<a href="$2" title="$3">$1</a>', 
                         $html);  
    return $html;
  }

}
?>
