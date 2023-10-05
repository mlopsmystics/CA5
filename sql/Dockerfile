FROM postgres:latest

EXPOSE 5432

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

RUN mkdir -p /ca4

COPY /main.sql /sql/

CMD ["postgres", "-D", "/ca4/"]
