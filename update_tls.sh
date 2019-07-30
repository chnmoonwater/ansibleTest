ansible -i hosts all -m copy -a "src=/data/certs/token.csv dest=/etc/kubernetes"
ansible -i hosts all -m copy -a "src=/data/certs/kubernetes.pem dest=/etc/kubernetes/ssl"
ansible -i hosts all -m copy -a "src=/data/certs/kubernetes-key.pem dest=/etc/kubernetes/ssl"
ansible -i hosts all -m shell -a 'update-ca-trust'
