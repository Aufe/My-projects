## Converter

This program will convert a parquet file to a csv file, and vice versa.

## Downloading

```
pip install -r requirements.txt
```

## Running

```
python concert.py [--parquet2csv <src-filename> "dst-filename"] | [--csv2parquet "src-filename" "dst-filename"] | [--get-schema "filename"] | [--help]
```

## Command line options

-   --parquet2csv - convert a parquet file to a csv file.
-   --csv2parquet - convert a csv file to a parquet file.
-   --get-schema - show a schema of parquet file.
-   --help - show message about options of program.

## Examples

```
python --parqeut2csv test.parquet test.csv  (Will convert a test.parquet to a test.csv)
python --get-scheme test.parquet (Will show a schema of test.parquet)
```
