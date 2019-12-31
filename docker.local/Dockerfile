FROM centos:7

COPY ["docker/build_config/repository/ius-release-el7.rpm", "/tmp/ius-release-el7.rpm"]

COPY ["docker/build_config/httpd/cvs_api.conf", "/etc/httpd/conf.d/cvs_api.conf"]

RUN yum -y install /tmp/ius-release-el7.rpm \
    && yum -y update \
    && yum -y install python36u python36u-pip python36u-mod_wsgi python36u-devel gcc mariadb-devel
    
RUN pip3.6 install --no-cache-dir django==2.2.5 requests pyquery mysqlclient djangorestframework

RUN rm -rf /tmp/ius-release-el7.rpm \
    && yum -y clean all

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
