## Converter

This program will convert a parquet file to a csv file, and vice versa.

## Using

python concert.py [--parquet2csv parquet-filename csv-filename] | [--csv2parquet csb-filename parquet-filename] | [--get-schema parquet-filename] | [--help]

## Command line options

-   --parquet2csv - This option will convert a parquet file to a csv file.
-   --csv2parquet - This option will convert a csv file to a parquet file.
-   --get-schema - This option will show a schema of parquet file.
-   --help - Show message about options of program.

## Examples

1.  python --parqeut2csv test.parquet test.csv  (Will convert a test.parquet to a test.csv)
2.  python --get-scheme test.parquet (Will show a schema of test.parquet)
