kubectl create secret generic eos-sss --from-file=/etc/cta/eos.sss.keytab
kubectl create secret generic migration-grpc --from-file=/etc/cta/eos.grpc.keytab