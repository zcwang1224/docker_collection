FROM mariadb

#ENV MARIADB_ROOT_PASSWORD=rootpass \
#    MARIADB_DATABASE=test_db \
#    MARIADB_USER=test_user \
#    MARIADB_PASSWORD=test_pass

COPY init.sql /docker-entrypoint-initdb.d/

COPY my.cnf /etc/mysql/conf.d/my.cnf