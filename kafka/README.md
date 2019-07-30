# Ansible Role: kafka

安装kafka集群

## 介绍
kafka是HashiCorp公司推出的一款开源工具，用于实现分布式系统的服务发现与配置。与其他类似产品相比，提供更“一站式”的解决方案。kafka内置有KV存储，服务注册/发现，健康检查，HTTP+DNS API，Web UI等多种功能。

官方地址： https://www.kafka.io/
github: https://github.com/hashicorp/kafka
官方文档地址：https://www.kafka.io/docs

## 要求

此角色仅在RHEL及其衍生产品上运行。

## 测试环境

ansible `2.2.1.0`
os `Centos 6.7 X64`

## 角色变量
    kafka_file: "kafka_{{ scala_version }}-{{ kafka_version }}.tgz"
    kafka_file_path: "{{ software_files_path }}/{{ kafka_file }}"
    kafka_file_url: "http://mirrors.tuna.tsinghua.edu.cn/apache/kafka/{{ kafka_version }}/{{ kafka_file }}"

    kafka_user: "kafka"
    kafka_home: "{{ software_install_path }}/kafka"

    kafka_brokerid: "{{ 300 | random(start=200) }}"
    kafka_port: 9092
    kafka_jmx_port: 
    kafka_ssl_port: ''

    kafka_name: "kafka{{ kafka_port if kafka_port != 9092 else '' }}"
    kafka_logdirs: "/kafka_data/logs{% if kafka_port != 9092  %}-{{ kafka_port }}{% endif %}"
    kafka_conf: "{{ kafka_home }}/config/server{% if kafka_port != 9092  %}-{{ kafka_port }}{% endif %}.properties"
    kafka_zk_quorum: "localhost:2181/kafka"

    kafka_server_logsdir: "/var/log/{{ kafka_name }}"
    kafka_heap_opts: "-Xmx1G -Xms1G"
    kafka_standalone: false

## 依赖
java
zookeeper

## github地址
https://github.com/kuailemy123/Ansible-roles/tree/master/kafka

## Example Playbook

    以standalone方式安装集群
    - hosts: node1
      vars:
        - kafka_standalone: true
      roles:
        - { role: kafka }
        - { role: kafka, kafka_port: 9093 }

    分布式安装集群
---
- name: deploy java
  hosts: ansible
  vars:
    kafka_zk_quorum: '10.17.0.187:2181,10.17.0.188:2181,10.17.0.189:2181'
  roles:
    - kafka

#kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --topic kafka-mq-2 -partitions 1 --replication-factor 2
#kafka-topics.sh --describe --zookeeper 127.0.0.1:2181
#kafka-console-producer.sh --broker-list 10.17.0.189:9092 --topic kafka-mq-2
#kafka-console-consumer.sh  --topic kafka-mq-2 --from-beginning --bootstrap-server 10.17.0.189:9092
