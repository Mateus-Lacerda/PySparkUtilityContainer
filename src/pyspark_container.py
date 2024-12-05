import argparse
import os
import sys

from functionalities import *

FILES_FOLDER = './files'
SQLS_FOLDER = './sqls'
RESULTS_FOLDER = './results'

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='A CLI for interacting with the pyspark container')
    
    parser.add_argument('--health', '-hl', action='store_true', help='Check the health of the service')
    parser.add_argument('--upload', '-u', action='store_true', help='Upload a file')
    parser.add_argument('--upload_from_folder', '-uff', action='store_true', help='Upload all from the files folder')
    parser.add_argument('--query', '-q', action='store_true', help='Query your files')
    parser.add_argument('--query_from_sql_file', '-qf', action='store_true', help='Query your files from a sql file')
    parser.add_argument('--write', '-w', action='store_true', help='Write the query result to a file')
    
    args = parser.parse_args()

    if not os.path.exists(FILES_FOLDER) or not os.path.exists(SQLS_FOLDER) or not os.path.exists(RESULTS_FOLDER):
        sys.argv = ['bash', 'setup.sh', '&&', 'python', 'src/pyspark_container.py'] + [f"--{arg}" for arg in vars(args).keys() if vars(args)[arg]]
        sys.exit(os.system(' '.join(sys.argv)))

    if args.health:
        print('Checking the health of the service')
        print(check_health())
    
    if args.upload:
        file_path = input('Enter the path to the file you want to upload: ')
        print(upload_file(file_path))

    if args.upload_from_folder:
        print('Uploading all files from the files folder')
        for file in os.listdir(FILES_FOLDER):
            print(upload_file(f'{FILES_FOLDER}/{file}'))
    
    if args.query:
        query = input('Enter the query you want to run: ')
        result = query_files(query)
        print(result)
        if args.write:
            with open(f'{RESULTS_FOLDER}/result.csv', 'w') as f:
                f.write(result)

    if args.query_from_sql_file:
        sql = input('Enter the name of the sql file you want to run: ')
        with open(f'{SQLS_FOLDER}/{sql}.sql') as f:
            query = f.read()
        print(query_files(query)) 
        if args.write:
            with open(f'{RESULTS_FOLDER}/{sql}.csv', 'w') as f:
                f.write(query_files(query))
    
    if not any(vars(args).values()):
        parser.print_help()