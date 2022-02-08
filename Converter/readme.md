## Converter

This program will convert a parquet file to a csv file, and vice versa.

## Running

  python concert.py [--parquet2csv "parquet-filename" "csv-filename"] | [--csv2parquet "csb-filename" "parquet-filename"] | [--get-schema 'parquet-filename"] | [--help]

## Command line options

-   --parquet2csv - convert a parquet file to a csv file.
-   --csv2parquet - convert a csv file to a parquet file.
-   --get-schema - show a schema of parquet file.
-   --help - show message about options of program.

## Examples

1.  python --parqeut2csv test.parquet test.csv  (Will convert a test.parquet to a test.csv)
2.  python --get-scheme test.parquet (Will show a schema of test.parquet)
