def test_kubectl(host):
    command = 'kubectl version --client=true'
    assert host.run('. /etc/profile && ' + command).rc == 0
