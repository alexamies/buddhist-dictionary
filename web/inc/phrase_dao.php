<?php

require_once 'database_utils.php' ;
require_once 'phrasemodel.php' ;

/**
 * Data access object for phrase entries
 */
class PhraseDAO {
	
    /**
     * Gets the phrase for the given id
     *
     * @param $id An id for the phrase entry
     * @return    A Phrase object
     */
    function getPhrase($id) {
        $databaseUtils = new DatabaseUtils();
        $databaseUtils->getConnection();

        // Perform SQL select operation 
        $id = $databaseUtils->escapeString($id);
        $query = "SELECT id, chinese_phrase, pos_tagged, sanskrit, source_no, source_name " .
                 "FROM phrases " .
                 "WHERE (id = $id)";
        //error_log("getPhrase, query: " . $query);
        $result =& $databaseUtils->executeQuery($query);
        $phrase = null;
        if ($row = $databaseUtils->fetch_array($result)) {
            $phrase = new Phrase($row[0], $row[1], $row[2], $row[3], $row[4], $row[5]);
        }
        $databaseUtils->free_result($result);
        $databaseUtils->close();
        return $phrase;
    }
}
?>
