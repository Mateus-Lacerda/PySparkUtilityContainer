# make files and sql dirs
mkdir -p files
mkdir -p sqls
mkdir -p results

# create a template files with example data
touch files/example.csv
echo "id,name,age\n1,John,25\n2,Doe,30" > files/example.csv

# create a template sql with example data
touch sqls/example.sql
echo "SELECT * FROM example" > sqls/example.sql

# create a template result file with example data
touch results/result.csv
echo "id,name,age\n1,John,25\n2,Doe,30" > results/result.csv