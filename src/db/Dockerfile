# DockerFile to build my sql image

FROM mysql:latest

EXPOSE 3306

COPY init.sql /docker-entrypoint-initdb.d/
