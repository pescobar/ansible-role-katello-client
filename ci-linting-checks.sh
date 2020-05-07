#!/bin/bash
ansible --version
yamllint --version
ansible-lint --version
yamllint .
ansible-lint -v --exclude=./roles --exclude=./collections .
