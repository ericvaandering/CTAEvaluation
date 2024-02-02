#! /bin/bash

# Get this in place with
# git clone https://github.com/ericvaandering/CTAEvaluation.git; cd CTAEvaluation/scripts; ./prepare_fermicloud_migrate.sh

cp ../docker/eos-xrootd-el9.repo /etc/yum.repos.d/

dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
dnf -y install protobuf
rpm -Uvh --nodeps $(repoquery --location grpc-cpp )
rpm -Uvh --nodeps $(repoquery --location grpc-devel )

dnf -y install postgresql14 postgresql14-libs
dnf -y install  https://download.oracle.com/otn_software/linux/instantclient/1912000/oracle-instantclient19.12-basiclite-19.12.0.0.0-1.x86_64.rpm

dnf -y install eos-client protobuf grpc-devel xrootd-client xrootd-client-libs libarchive

dnf -y install eos-test


scp cmscta01:~/rpms/"cta*" /tmp
mkdir ~/secrets/
scp cmscta01:~/secrets/cms10p-secrets.sh ~/secrets/
dnf -y install /tmp/cta-*.rpm

pip install --upgrade protobuf sqlalchemy psycopg2-binary python-libarchive

git checkout no_hardcode_migrate

scp cmscta01:~/secrets/migration.conf /etc/cta
scp cmscta01:/etc/cta/forwardable.keytab  /keytabs/eos.sss.keytab
scp cmscta01:/etc/cta/cta-cli.conf  /etc/cta
scp cmscta01:/etc/cta/cta-frontend-xrootd.conf  /etc/cta
scp cmscta01:/etc/cta/eos.grpc.keytab.works  /etc/cta/eos.grpc.keytab
