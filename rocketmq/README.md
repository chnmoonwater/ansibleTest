---
- name: deploy consul
  hosts: ansible
  vars:
    rocket_type: nameserver
  roles:
    - rocketmq

---
- name: deploy consul
  hosts: 10.17.0.187
  vars:
    rocket_type: broker
    namesrvAddr:
      -  {'host': 10.17.0.187, 'port': 9876}
      -  {'host': 10.17.0.188, 'port': 9876}
      -  {'host': 10.17.0.189, 'port': 9876}
  roles:
    - rocketmq

- name: deploy consul
  hosts: 10.17.0.188
  vars:
    rocket_type: broker
    brokerName: broker-b
    brokerId: 1
    namesrvAddr:
      -  {'host': 10.17.0.187, 'port': 9876}
      -  {'host': 10.17.0.188, 'port': 9876}
      -  {'host': 10.17.0.189, 'port': 9876}
  roles:
    - rocketmq

- name: deploy consul
  hosts: 10.17.0.187
  vars:
    rocket_type: broker
    brokerName: broker-b
    brokerRole: SLAVE
    listenPort: 10921
    brokerId: 1
    namesrvAddr:
      -  {'host': 10.17.0.187, 'port': 9876}
      -  {'host': 10.17.0.188, 'port': 9876}
      -  {'host': 10.17.0.189, 'port': 9876}
  roles:
    - rocketmq

- name: deploy consul
  hosts: 10.17.0.188
  vars:
    rocket_type: broker
    brokerName: broker-a
    brokerRole: SLAVE
    listenPort: 10921
    brokerId: 1
    namesrvAddr:
      -  {'host': 10.17.0.187, 'port': 9876}
      -  {'host': 10.17.0.188, 'port': 9876}
      -  {'host': 10.17.0.189, 'port': 9876}
  roles:
    - rocketmq

- name: deploy consul
  hosts: 10.17.0.189
  vars:
    rocket_type: console
    namesrvAddr:
      -  {'host': 10.17.0.187, 'port': 9876}
      -  {'host': 10.17.0.188, 'port': 9876}
      -  {'host': 10.17.0.189, 'port': 9876}
  roles:
    - rocketmq
