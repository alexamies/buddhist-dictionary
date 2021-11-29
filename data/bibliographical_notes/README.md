# Bibliographical Notes Database

Currently the database is limited to the Esoteric Section of the Taisho. The
tables are given in CSV format. The main file is
`taisho_estoteric_section_bibliographic_notes.csv`. Import this into your
favorite spreadhsheet program or load into a database using the instructions
below.

## Loading into a Database

The format of the data is suitable for any relational database.

### BigQuery

Load the files into BigQuery, following instructions at 
https://cloud.google.com/bigquery/docs/batch-loading-data#bq

From the top level of this project execute the command

```shell
FORMAT=CSV # comma separated variable
PROJECT_ID=[your project] # The alphanumberic ID of your GCP project
DATASET=[your dataset] # To group tables, create a new one if needed
TABLE=bibliographic_notes # The name of the table that will be created
SOURCE=data/bibliographical_notes/taisho_estoteric_section_bibliographic_notes.csv # File to load
SCHEMA=data/bibliographical_notes/bibliographic_notes_schema.json # Schema is in this file
bq load \
--source_format=$FORMAT \
--skip_leading_rows=1 \
${PROJECT_ID}:${DATASET}.${TABLE} \
${SOURCE} \
${SCHEMA}
```

## Querying the Database

Number of records:

```sql
SELECT
  COUNT(reference_no)
FROM
  bibliographic_notes
```

Query for translators, order by number of works translated and also include
the number scrolls:

```sql
SELECT
  attribution_en,
  COUNT(reference_no) AS num_works,
  SUM(no_scrolls) AS num_scrolls
FROM
  bibliographic_notes
GROUP BY
  attribution_en
ORDER BY 
  num_works DESC 
```

Query for dynasty, order by number of works translated and also include
the number scrolls:

```sql
SELECT
  dynasty_en,
  COUNT(reference_no) AS num_works,
  SUM(no_scrolls) AS num_scrolls
FROM
  bibliographic_notes
GROUP BY
  dynasty_en
ORDER BY 
  num_works DESC 
```

Query for dynasty, order by number of works translated and also include
the number scrolls:

```sql
SELECT
  previous_source,
  COUNT(reference_no) AS num_works,
  SUM(no_scrolls) AS num_scrolls
FROM
  bibliographic_notes
GROUP BY
  previous_source
ORDER BY 
  num_works DESC 
```
