What is converter?
-------------

Converter makes it easy to convert CSV-file to Parquet-file and back. For your convenience this application supports calling from command line.


Quick start
-----------
To install required libraries use:

    python pip install -r requirements.txt
    
To convert CSV-file to Parquet-file you should call next request from command line:

    python converter.py --csv2parquet filename.csv filename.parquet
    
A new file will be create in the same directory.
To convert Parquet-file to CSV-file you should call next request from command line:

    python converter.py --parquet2csv filename.parquet filename.csv
    
If you want to get the scheme of Parquet-file:

    python converter.py --get_schema filename.parquet   
    
To get some help:

    python converter.py --help      
    

Contributing
------------

Help in testing, development, documentation and other tasks is
highly appreciated and useful to the project.
