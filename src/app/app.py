from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from spark.spark import Spark
from typing import Union
from pydantic import BaseModel

class QueryRequest(BaseModel):
    q: str

class DataFrameRequest(BaseModel):
    data: Union[list, dict]
    schema: str

class TempViewRequest(BaseModel):
    df: str  # Ajuste o tipo conforme a implementação real
    name: str

class App:
    def __init__(self):
        self.SPARK = Spark()
        self.app = FastAPI()
        self.setup_static_files()
        self.setup_routes()
        self.setup_visual_routes()

    def setup_static_files(self):
        # Monta o diretório estático
        self.app.mount("/static", StaticFiles(directory="src/static"), name="static")

    def setup_routes(self):
        # Rotas para servir páginas HTML
        @self.app.get("/", response_class=HTMLResponse)
        async def read_index():
            return FileResponse("src/static/index.html")

        @self.app.get("/upload", response_class=HTMLResponse)
        async def read_upload():
            return FileResponse("src/static/upload.html")

        @self.app.get("/visualize", response_class=HTMLResponse)
        async def read_visualize():
            return FileResponse("src/static/visualize.html")

        @self.app.get("/query", response_class=HTMLResponse)
        async def read_query():
            return FileResponse("src/static/query.html")

        # Rotas da API
        @self.app.get("/health")
        def health():
            return {"status": "ok"}

        @self.app.get("/api/v1/query")
        async def query(q: str):
            if not q:
                raise HTTPException(status_code=400, detail="Query parameter 'q' is required.")
            try:
                result = self.SPARK.query(q)
                return {"result": result}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.put("/api/v1/create_dataframe")
        async def create_df(request: DataFrameRequest):
            try:
                result = self.SPARK.create_df_from_dict(request.data, request.schema)
                return {"result": result}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.put("/api/v1/create_temp_view")
        async def create_temp_view(request: TempViewRequest):
            try:
                result = self.SPARK.create_temp_view(request.df, request.name)
                return {"result": result}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.post("/upload_file")
        async def upload_file(file: UploadFile = File(...), name: str = None):
            try:
                os.makedirs("data", exist_ok=True)
                file_location = f"data/{file.filename}"
                with open(file_location, "wb") as f:
                    f.write(await file.read())
                self.SPARK.create_df_from_file(file_location, name or file.filename)
                return {"filename": file.filename}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    def setup_visual_routes(self):
        @self.app.get("/table/{table_name}")
        def table(table_name: str):
            try:
                table = self.SPARK.query(f"SELECT * FROM {table_name}")
                return {"table": table}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.get("/table/{table_name}/describe")
        def describe(table_name: str):
            try:
                table = self.SPARK.query(f"DESCRIBE {table_name}")
                return {"table": table}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    app_instance = App().app
    uvicorn.run(app_instance, host="0.0.0.0", port=8000)