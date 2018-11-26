katello-agent
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
         - { role: katello-agent }

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
