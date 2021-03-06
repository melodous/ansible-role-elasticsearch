Welcome to elasticsearch Ansible Role’s documentation!
======================================================

Role Name
---------

Ansible role to install elasticsearch nodes on containers

### Requirements

Docker

### Dependencies

N/A

### Example Playbook

    - hosts: servers
      roles:
        - { role: elasticsearch }

pip ansible role default variables
----------------------------------

#### Sections

-   elasticsearch packaging
-   ElasticSearch configuration
-   ElasticSearch monitoring management

### elasticsearch packaging

`elasticsearch_docker_imagen`

> ElasticSearch docker image

    elasticsearch_docker_image: melodous/elasticsearch

`elasticsearch_version`

> ElasticSearch docker image version (TAG)

    elasticsearch_version: 5.4.1

`es_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default elasticsearch.

    es_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: elasticsearch

### ElasticSearch configuration

`es_group`

> ElasticSearch group name

    es_group: elasticsearch

`es_group_id`

> ElasticSearch group id

    es_group_id: 1000

`es_user`

> ElasticSearch user name

    es_user: elasticsearch

`es_user_id`

> ElasticSearch user id

    es_user_id: 1000

`conf_dir`

> Configuration directory

    conf_dir: "/usr/share/elasticsearch/config"

    es_config: {}

Example:

    es_config:
      node.name: "{{ ansible_hostname }}"
      cluster.name: "{{ es_cluster_name }}"
      node.data: true
      node.master: false
      bootstrap.memory_lock: true
      discovery.zen.ping.unicast.hosts: "{{ groups.esmasters | join(',') }}"

    data_dirs:
      - "/usr/share/elasticsearch/data"

`log_dir`

> Directory to save elasticsearch logs

    log_dir: "/usr/share/elasticsearch/logs"

    es_cluster_name: elasticsearch

`es_instance_name`

> Name of the instance

    es_instance_name: "{{ ansible_hostname }}"

`es_heap_size`

> Size of java virtual machine head

    es_heap_size: 256m

`es_jvm_custom_parameters`

> Custom parameters for java virtual machine

    es_jvm_custom_parameters: ''

`es_data_lvm_vgname`

> volume group name for elasticsearch data fs

    es_data_lvm_vgname: vg_es

`es_data_lvm_pvs`

> physical volume tha will be added to volume group

    es_data_lvm_pvs: /dev/sdb

`es_data_lvm_pesize`

> physical extend size

    es_data_lvm_pesize: 4

`es_data_lvm_lvname`

> Logical volume name for data fs

    es_data_lvm_lvname: lv_es_data

    es_data_lvm_lvsize: 100%FREE

`es_data_lvm_fs`

> Mount point for the filesystems that will be used by elasticsearch as
> data storage

    es_data_lvm_fs: /var/lib/elasticsearch

`es_backup`

> Configure snapshots for ElasticSearch cluster You must configure NFS
> mount point for all clusters members

    es_backup: false

`es_backup_nfs`

> NFS mount point for snapshots

    es_backup_nfs: false

`es_backup_mountpoint`

> mountpoint for the nfs share

    es_backup_mountpoint: "{{ es_data_lvm_fs }}/backup"

`es_backup_repo_name`

> logical name for repository in ES Cluster

    es_backup_repo_name: backup

### ElasticSearch monitoring management

`elasticsearch_monitoring`

> Enable or disable elasticsearch monitoring
>
>     elasticsearch_monitoring: true

Changelog
---------

**elasticsearch**

This project adheres to Semantic Versioning and human-readable
changelog.

### elasticsearch master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### elasticsearch v0.0.6 - 2017/08/14

##### Changed

-   Fixed perms on nfs mount point

### elasticsearch v0.0.5 - 2017/08/14

##### Added

-   Added repository configuration

### elasticsearch v0.0.4 - 2017/07/17

##### Changed

-   Fixed error playbook.yml

### elasticsearch v0.0.3 - 2017/07/14

##### Added

-   Fixed error on filter\_plugins

### elasticsearch v0.0.2 - 2017/07/14

##### Added

-   Added custom plugin

### elasticsearch v0.0.1 - 2017/07/13

##### Added

-   Initial version

Copyright
---------

elasticsearch

Copyright (C) 2017/07/13 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
