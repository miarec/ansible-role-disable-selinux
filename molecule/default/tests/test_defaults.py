import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_selinux(host):
    assert host.run('getenforce').stdout == "Disabled\n", "SELinux is not disabled"

def test_selinux_config(host):
    assert host.run('cat /etc/selinux/config | grep "SELINUX=disabled"').rc == 0, "/etc/selinux/config does not have `SELINUX=disabled`"
