Ansible Role: Kubernetes
========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-kubernetes.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-kubernetes)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.kubernetes-blue.svg)](https://galaxy.ansible.com/gantsign/kubernetes)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-kubernetes/master/LICENSE)

Role to install the [Kubernetes](http://kubernetes.io) container cluster
manager.

Requirements
------------

* Ansible >= 2.7

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Node type: determines what features are installed.
# - controller:
#     - kubectl
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

Tab Completion & Aliases for Zsh
--------------------------------

### Using Ansible

We recommended using the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role to enable
Zsh support for Kubernetes (this must be configured for each user).

```yaml
- hosts: servers
  roles:
    - role: gantsign.kubernetes
      kubernetes_node_type: worker

    - role: gantsign.antigen
      users:
        - username: example
          antigen_libraries:
            - name: oh-my-zsh
          antigen_bundles:
            # Use the Oh My Zsh plugin for kubectl
            - name: kubectl
            # Use the GantSign plugin for kubeadm
            - name: kubeadm
              url: gantsign/zsh-plugins
              location: kubeadm
```

### Using Antigen

If you prefer to use [Antigen](https://github.com/zsh-users/antigen) directly
add the following to your Antigen configuration:

```bash
antigen use oh-my-zsh
antigen bundle kubectl
antigen bundle gantsign/zsh-plugins kubeadm
```

**Important:** there's a [bug](https://github.com/zsh-users/antigen/issues/583)
with the current version of Antigen that prevents it working with the `kubectl`
plugin. We recommend using version `2.0.2` of Antigen until the issue is fixed.

### Manual configuration

To manually configure Zsh tab completion add the following to your `.zshrc`:

```bash
eval "$(kubectl completion zsh)"
eval "$(kubeadm completion zsh)"
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

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
