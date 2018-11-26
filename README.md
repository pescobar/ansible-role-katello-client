[![Build Status](https://travis-ci.org/pescobar/ansible-role-katello-agent.svg?branch=master)](https://travis-ci.org/pescobar/ansible-role-katello-agent)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-pescobar.katello_agent-blue.svg)](https://galaxy.ansible.com/pescobar/katello_agent)

pescobar.katello_agent
=========

register a node with Katello

Role Variables
--------------

```
katello_hostname: katello.example.com
katello_activationkey: compute_nodes
katello_org_id: sciCORE
katello_force_register: false
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: katello_agent }

License
-------

GPLv3


Molecule Tests
-------
The repo includes some molecule tests to check the complete process or registering a node.
Once you define the required variables you can try `molecule test` to verify it's working
Travis-CI in github only does a syntax check.


Author Information
------------------

Pablo Escobar Lopez
