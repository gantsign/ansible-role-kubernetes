Ansible Role: Kubernetes
========================

[![Tests](https://github.com/gantsign/ansible-role-kubernetes/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-kubernetes/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.kubernetes-blue.svg)](https://galaxy.ansible.com/gantsign/kubernetes)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-kubernetes/master/LICENSE)

Role to install the [Kubernetes](http://kubernetes.io) container cluster
manager.

Requirements
------------

* Ansible Core >= 2.12

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

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

# The ID of the APT key for the Kubernetes repository (optional)
kubernetes_apt_key_id:
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

This project uses the following tooling:
* [Molecule](http://molecule.readthedocs.io/) for orchestrating test scenarios
* [Testinfra](http://testinfra.readthedocs.io/) for testing the changes on the
  remote
* [pytest](http://docs.pytest.org/) the testing framework
* [Tox](https://tox.wiki/en/latest/) manages Python virtual
  environments for linting and testing
* [pip-tools](https://github.com/jazzband/pip-tools) for managing dependencies

A Visual Studio Code
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) is
provided for developing and testing this role.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
