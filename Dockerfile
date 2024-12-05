# Use uma imagem base estável com Python
FROM python:3.10-slim-buster

# Defina o diretório de trabalho
WORKDIR /app

# Defina as variáveis de ambiente
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark/spark-3.2.0-bin-hadoop3.2
ENV PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH

# Instale dependências do sistema
RUN apt-get update && \
    apt-get install -y wget tar && \
    rm -rf /var/lib/apt/lists/*

# Crie o diretório para o JDK
RUN mkdir -p /usr/lib/jvm

# Baixe e instale o OpenJDK 8 a partir do Eclipse Temurin
RUN wget -qO- https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u322-b06/OpenJDK8U-jdk_x64_linux_hotspot_8u322b06.tar.gz | tar -xzC /usr/lib/jvm && \
    ln -s /usr/lib/jvm/jdk8u322-b06 /usr/lib/jvm/java-8-openjdk-amd64 && \
    java -version

# Verifique a instalação do Java
RUN java -version

# Faça o download e extraia o Spark
RUN mkdir -p /opt/spark && \
    wget -q https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz && \
    tar -xvf spark-3.2.0-bin-hadoop3.2.tgz -C /opt/spark && \
    rm spark-3.2.0-bin-hadoop3.2.tgz && \
    ls /opt/spark/spark-3.2.0-bin-hadoop3.2

# Atualize o pip
RUN pip install --upgrade pip

# Instale dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copie o código da aplicação
COPY ./src ./src

# Exponha a porta que o FastAPI usará
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "-u", "src/entrypoint.py"]