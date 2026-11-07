# ansible-role-disable-selinux

Ansible role to disable SELinux on RedHat family operating systems


Example Playbook
----------------

eg:

``` yaml
    - name: Disable SELinux
      hosts: localhost
      become: yes
      roles:
        - ansible-role-disable-selinux
```

## Testing

This role uses [Molecule](https://molecule.readthedocs.io/) with Docker for testing.
[uv](https://docs.astral.sh/uv/) is used for dependency management.

### Prerequisites

- Docker
- uv (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Running Tests

```bash
# Run full test suite
uv run molecule test

# Test against specific distro
MOLECULE_DISTRO=ubuntu2404 uv run molecule test
MOLECULE_DISTRO=rockylinux9 uv run molecule test
```

### Available Distros

| Distribution   | Variable Value  |
|----------------|-----------------|
| Ubuntu 22.04   | `ubuntu2204`    |
| Ubuntu 24.04   | `ubuntu2404`    |
| Rocky Linux 9  | `rockylinux9`   |
| RHEL 9         | `rhel9`         |

### Linting

```bash
uv run ansible-lint
```
