import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_katello_agent_package(host):
    assert host.package("katello-agent").is_installed


def test_subscription_manager_package(host):
    assert host.package("subscription-manager").is_installed


def test_goferd_service(host):
    s = host.service("goferd")
    assert s.is_running
    assert s.is_enabled
