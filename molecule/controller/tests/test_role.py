import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kubectl(host):
    command = 'kubectl version --client=true'
    assert host.run('. /etc/profile && ' + command).rc == 0
