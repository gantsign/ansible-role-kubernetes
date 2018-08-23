import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('command', [
    'kubelet --version',
    'kubectl version --client=true'
])
def test_commands(host, command):
    cmd = host.run('. /etc/profile && ' + command)
    assert cmd.rc == 0
