hdfs dfs -rm -r /get_movies
hdfs dfs -mkdir /get_movies
hdfs dfs -put data/movies.csv /get_movies
hdfs dfs -put data/ratings.csv /get_movies
hdfs dfs -rm -r /get_movies/out

while [ -n "$1" ]
do
case "$1" in
-regexp) param="$2"
regexp="--regexp $param"
shift ;;
-year_from) param="$2"
year_from="--year_from $param"
shift ;;
-year_to) param="$2"
year_to="--year_to $param"
shift ;;
-genres) param="$2"
genres="--genres $param"
shift ;;
-N) param="$2"
n="--N $param"
shift ;;
esac
shift
done

spark-submit get_movies.py $regexp $year_from $year_to $genres $n
