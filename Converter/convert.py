import argparse
import os
from pyarrow import parquet, csv



def parquet2csv(parquet_name, csv_name):
    table = parquet.read_table(f"files/{parquet_name}")
    csv.write_csv(table, f"files/{csv_name}")

def csv2parquet(csv_name, parquet_name):
    table = csv.read_csv(f"files/{csv_name}")
    parquet.write_table(table, f"files/{parquet_name}")

def get_schema(parquet_name):
    table = parquet.read_table(f"files/{parquet_name}")
    print(table.schema)

parser = argparse.ArgumentParser()

parser.add_argument('--parquet2csv', nargs=2, help='This option will convert a parquet file to a csv file')
parser.add_argument('--csv2parquet', nargs=2, help='This option will convert a csv file to a parquet file')
parser.add_argument('--get-schema', dest='schema', help='This option will show a schema of parquet file')

func_names = parser.parse_args()

if func_names.parquet2csv:
    parquet2csv(func_names.parquet2csv[0], func_names.parquet2csv[1])
elif func_names.csv2parquet:
    csv2parquet(func_names.csv2paquet[0], func_names.scv2parquet[1])
elif func_names.schema:
    get_schema(func_names.schema)
