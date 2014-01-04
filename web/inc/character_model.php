<?php
/** 
 * Utility methods for dealing with CJK characters.
 */
class Character {

  var $c;  // The character
  var $punctuation = array('。'  => 'Period', 
                           '.'  => 'Period (ASCII)', 
                           '，' => 'Comma',
                           ',' => 'Comma (ASCII)',
                           '；' => 'Semicolon',
                           ';' => 'Semicolon (ASCII)',
                           '：' => 'Colon',
                           '∶' => 'Colon',
                           ':' => 'Colon (ASCII)',
                           '？' => 'Question Mark',
                           '?' => 'Question Mark (ASCII)',
                           '《' => 'Left Quotation Mark (Angle)',
                           '》' => 'Right Quotation Mark (Angle)',
                           '“' => 'Left Quotation Mark (Double)',
                           '”' => 'Right Quotation Mark (Double)',
                           '‘' => 'Left Quotation Mark (Single)',
                           '’' => 'Right Quotation Mark (Single)',
                           "'" => 'Quotation Mark (ASCII)',
                           "\"" => 'Quotation Mark (ASCII)',
                           "！" => 'Exclamation Mark',
                           "!" => 'Exclamation Mark (ASCII)',
                           "【" => 'CJK Left heavy square bracket',
                           "】" => 'CJK Left square bracket',
                           "〔" => 'CJK Left square bracket',
                           "〕" => 'CJK Right angle bracket',
                           "║" => 'CJK double pipe'
                          );

  /**
   * Constructor for a Character object
   * @param $c	The character
   */
  function Character($c) {
    $this->c = $c;
  }

  /**
   * Gets the integer code for the character
   * @return An integer value
   */
  function getIntCode() {
    $h = ord($this->c[0]);
    if ($h <= 0x7F) {
      return $h;
    } else if ($h < 0xC2) {
      return false;
    } else if ($h <= 0xDF) {
      return ($h & 0x1F) << 6 | (ord($this->c[1]) & 0x3F);
    } else if ($h <= 0xEF) {
      return ($h & 0x0F) << 12 | (ord($this->c[1]) & 0x3F) << 6
              | (ord($this->c[2]) & 0x3F);
    } else if ($h <= 0xF4) {
      return ($h & 0x0F) << 18 | (ord($this->c[1]) & 0x3F) << 12
              | (ord($this->c[2]) & 0x3F) << 6
              | (ord($this->c[3]) & 0x3F);
    } else {
      return false;
    }
  }

  /**
   * Returns true if this character is a CJK letter.  
   *
   * This will be true if the Unicode value for is in the 
   * Kangxi Radicals (> 2F00 and < 2FDF) or
   * CJK Radicals Supplement (> 2E80 and < 2EFF) or
   * CJK Unified Ideographs (> 4E00 and < 4FAF) or 
   * CJK Compatibility Ideographs (> F900 and < FACF)
   * CJK Compatibility Ideographs (> 2F800 and < 2FA0F)
   * CJK Unified Ideographs Extension A (> 3400 and < 4DAF)
   * CJK Unified Ideographs Extension B (> 20000 and < 2A6CF)
   * However, it will fail for radicals 
   * @return true or false
   */
  function isCJKLetter() {
    $val = $this->getIntCode();
    return (($val >= 12032) && ($val <= 12255)) || 
           (($val >= 11904) && ($val <= 12031)) || 
           (($val >= 19968) && ($val <= 40879)) || 
           (($val >= 63744) && ($val <= 64207)) || 
           (($val >= 194560) && ($val <= 195087)) || 
           (($val >= 13312) && ($val <= 19887)) ||
           (($val >= 131072) && ($val <= 173775));
  }

  /**
   * Returns true if this character is punctuation, such as a period, comma, etc
   * @return Either true or false
   */
  function isPunctuation() {
    $c = $this->c;
    return isset($this->punctuation[$c]);
  }
}
?>
