from pyspark.sql import SparkSession
import os
import re
import tempfile
import shutil
class Spark:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("PySpark Application") \
            .master("local[*]") \
            .config("spark.driver.host", "localhost") \
            .getOrCreate()
        self.spark.sparkContext.setLogLevel("ERROR")  # Reduz logs para evitar excessos

    def sanitize_view_name(self, name: str) -> str:
        # Remove caracteres que não são letras, números ou underscores
        return re.sub(r'\W+', '_', name)

    def create_df_from_file(self, file_path: str, file_name: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo {file_path} não encontrado.")
        
        df = self.spark.read.csv(file_path, header=True, inferSchema=True)
        sanitized_name = self.sanitize_view_name(file_name)
        print(f"Creating temp view: {sanitized_name}")
        df.createOrReplaceTempView(sanitized_name)
        return df

    def query(self, query: str, csv: bool = False):
        try:
            df = self.spark.sql(query)
            if csv:
                temp_dir = tempfile.mkdtemp()
                temp_path = os.path.join(temp_dir, "output.csv")
                df.coalesce(1).write.option("header", "true").csv(temp_path, mode='overwrite')
                
                # Find the CSV file in the directory
                csv_file_path = [os.path.join(temp_path, f) for f in os.listdir(temp_path) if f.endswith(".csv")][0]
                
                # Read the CSV file back into a string
                with open(csv_file_path, 'r') as f:
                    data = f.read()
                
                # Clean up the temporary directory
                shutil.rmtree(temp_dir)
                return data
            return df.collect()
        except Exception as e:
            return {"error": str(e)}