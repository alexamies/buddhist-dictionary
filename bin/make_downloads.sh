#!/bin/bash
## Generates the JSON files for dictionary terms.
OUTPUT_DIR=downloads
python3 bin/tsv2json.py "data/dictionary/words.txt" $OUTPUT_DIR/ntireader_words.json "NTI Reader dictionary" "NTI Reader" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/buddhist_named_entities.txt" $OUTPUT_DIR/buddhist_named_entities.json "NTI Reader Buddhist named entities (people, places, text titles, etc)"  "Buddhist named entities" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/translation_memory_buddhist.txt" $OUTPUT_DIR/translation_memory_buddhist.json "NTI Reader Buddhist quotations" "Literary Chinese quotations" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
