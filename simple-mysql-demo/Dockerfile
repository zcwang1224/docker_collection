FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=rootpass \
    MYSQL_DATABASE=test_db \
    MYSQL_USER=test_user \
    MYSQL_PASSWORD=test_pass

COPY init.sql /docker-entrypoint-initdb.d/

COPY my.cnf /etc/mysql/conf.d/my.cnf

# EXPOSE 3306