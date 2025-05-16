FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=appdb
COPY *.sql /docker-entrypoint-initdb.d/
