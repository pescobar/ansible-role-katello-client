[![Build Status](https://travis-ci.org/pescobar/ansible-role-katello-client.svg?branch=master)](https://travis-ci.org/github/pescobar/ansible-role-katello-agent)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-pescobar.katello_client-blue.svg)](https://galaxy.ansible.com/pescobar/katello_client)

pescobar.katello_client
=========

register a node with Katello

**this role would only disable the default yum repos in CentOS . It's not tested with RedHat**

Role Variables
--------------

```
katello_client_katello_server_hostname: katello.example.com
katello_client_activationkey: compute_nodes_production
katello_client_org_id: sciCORE
katello_client_rhsm_baseurl: "https://{{ katello_client_katello_server_hostname }}/pulp/repos"
katello_client_force_register: false

katello_client_extra_packages:
  - katello-host-tools
  - katello-host-tools-tracer
  - katello-host-tools-fact-plugin

katello_client_install_agent: false  # katello-agent is deprecated so you probably don't want this

# set this var to true in case you want to use upstream repos for katello-client
# you usually won't do this because your katello instance also provides this repo
katello_client_yum_repo_add: false
katello_client_yum_repo_rpm: https://yum.theforeman.org/client/2.4/el7/x86_64/foreman-client-release.rpm

katello_client_disable_yum_fastest_mirror_plugin: true

# list of upstream repostories we will disable in the katello client
katello_client_repos_to_update:
  - name: base
    file: CentOS-Base
    description: default base yum repo
    mirrorlist: http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
    gpgcheck: true
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
    enabled: false
  - name: updates
    file: CentOS-Base
    description: default updates yum repo
    mirrorlist: http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
    gpgcheck: true
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
    enabled: false
  - name: extras
    file: CentOS-Base
    description: default extras yum repo
    mirrorlist: http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
    gpgcheck: true
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
    enabled: false
  - name: epel
    file: epel
    description: epel
    metalink: https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
    gpgcheck: 1
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
    enabled: false
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: pescobar.katello_agent }

License
-------

GPLv3


Molecule Tests
-------
The repo includes some molecule tests to check the complete process or registering a node.
Once you define the required variables you can try `molecule test` to verify it's working.
Travis-CI in github only does a syntax check.


Author Information
------------------

Pablo Escobar Lopez
