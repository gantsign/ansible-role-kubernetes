Ansible Role: Kubernetes
========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-kubernetes.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-kubernetes)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.kubernetes-blue.svg)](https://galaxy.ansible.com/gantsign/kubernetes)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-kubernetes/master/LICENSE)

Role to install the [Kubernetes](http://kubernetes.io) container cluster
manager.

Requirements
------------

* Ansible >= 2.3

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Xenial (16.04)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Node type: determines what features are installed.
# - worker:
#     - kubelet
#     - kubernetes-cni
# - master:
#     - kubelet
#     - kubectl
#     - kubernetes-cni
# - admin:
#     - kubelet
#     - kubectl
#     - kubeadm
#     - kubernetes-cni
kubernetes_node_type: worker

# The ID of the APT key for the Kubernetes repository
kubernetes_apt_key_id: 6A030B21BA07F4FB
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.kubernetes
      kubernetes_node_type: worker
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
