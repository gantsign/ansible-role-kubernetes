import pytest


@pytest.mark.parametrize('command', [
    'kubelet --version',
    'kubectl version --client=true'
])
def test_commands(host, command):
    cmd = host.run('. /etc/profile && ' + command)
    assert cmd.rc == 0
