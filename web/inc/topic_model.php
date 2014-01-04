<?php
/** 
 * An object encapsulating topic information
 */
class Topic {
    var $simplified;  // Simplified Chinese text for the topic
    var $english;     // English translation for topic
    var $url;         // The URL of a page to display information about the topic
    var $title;         // The URL of a page to display information about the topic

    /**
     * Constructor for a Topic object
     *
     * @param $simplified  Simplified Chinese text for the topic
     * @param $english  English translation for topic
     * @param $url  URL for a page explaining more about the topic
     * @param $title  Title for the page
     */
    function Topic ($simplified, $english, $url, $title) {
        $this->simplified = $simplified;
        $this->english = $english;
        $this->url = $url;
        $this->title = $title;
    }

    /**
     * Accessor method for english.
     * @return The English translation for topic
     */
    function getEnglish() {
        return $this->english;
    }

    /**
     * Accessor method for simplified.
     * @return The simplified Chinese text for the topic
     */
    function getSimplified() {
        return $this->simplified;
    }

    /**
     * Accessor method for url.
     * @return The URL of a page to display information about the topic
     */
    function getUrl() {
        return $this->url;
    }

    /**
     * Accessor method for title.
     * @return A string value
     */
    function getTitle() {
        return $this->title;
    }

}

?>
