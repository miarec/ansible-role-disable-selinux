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
