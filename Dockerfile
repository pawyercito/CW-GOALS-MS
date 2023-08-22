FROM ubuntu:22.04


ENV DEBIAN_FRONTEND=noninteractive
# Configura la zona horaria como variable de entorno
ENV TZ=America/Guayaquil

# Actualiza e instala paquetes necesarios
RUN apt-get update && \
    apt-get install -y python3-pip tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Crea el directorio de trabajo y copia los archivos necesarios
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /usr/src/app/logs
COPY . /usr/src/app

EXPOSE 2110

ENTRYPOINT ["python3"]
CMD ["-m", "swagger_server"]
