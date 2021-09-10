# Context
The official recommendation for test environments (VMs or Containers) are documented here:
- https://complianceascode.readthedocs.io/en/latest/tests/README.html

So, regarding the VMs installations, the instructions using the `install_vm.py` script should be considered if in doubt.

Since the `install_vm.py` is relatively easy to prepare Fedora or CentOS VMs, it may be not so intuitive for other distros mainly because it would require the user to inform repositories and kickstart files too.

Since we, as developers, usually need these VMs for quick tests, as supportive resources for the actual goals, I simplified the approach using `Vagrant` and as result I can highlight the following main advantages compared to `install_vm.py` approach:

- Faster provisioning
    - `install_vm.py` actually installs the system passing by all traditional tasks like partitioning, pre-install, install (download packages), post-install, etc. This, in my test environment, took about **9 minutes**.
    - Using `Vagrantfile` for Fedora, I achieved the same state in **1 minute**.

- More flexibility;
    - In a traditional VM it is necessary to care about **snapshots** after a fresh install. It is also necessary keep the VM there, even when not necessary. Otherwise, a new installation will be necessary.
    - Using `Vagrant`, it is possible to easily and quickly start a brand new VM on demand, without worry about dangerous tests on there, snapshots, etc. `Just destroy and create another as much as you want`.
- Less maintenance;
    - `Vagrant` is a very popular solution for provisioning of quick labs, with a active community, good documentation and rich arsenal of features which can be easily enjoyed.

# Prepare a VM
Currently this role has tested Vagrantfiles for `ComplianceAsCode` in the following distros:
- Fedora
- RHEL
- Ubuntu

However, is pretty easy to include more distros. Just copy an existing Vagrantfile, adjust what is necessary and you are ready.

Please, consider to send your PR to contribute in this Ansible role.

## Provisioning a VM
>cd ~/OpenSCAP/Labs/VMs/Fedora
>vagrant up

## Stopping a VM
When you want to stop a VM but keep its content due some Work In Progress, for instance:
>cd ~/OpenSCAP/Labs/VMs/Fedora
>vagrant halt
>vagrant up

## Destroying a VM
When the VM is no longer necessary or you just want a new one:
>cd ~/OpenSCAP/Labs/VMs/Fedora
>vagrant destroy

# Access a VM
## Via Vagrant
>cd ~/OpenSCAP/Labs/VMs/Fedora
>vagrant ssh

## Via SSH
First get the VM IP Address. There are many ways to do that, here is a CLI option:
```
arp -n | grep $(virsh -q domiflist cac_fedora34 | awk '{print $5}') | awk '{print $1}'
```
Once you have the IP, you can directly SSH them using the following users:
>ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@<IP>

- No password required since the ssh-key was already included during the provisioning.

>ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null vagrant@<IP>

- No password required since the ssh-key was already included during the provisioning.
- vagrant user password, if necessary: vagrant

>ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null admin@<IP>
- Password: admin123

## Via virt-manager
>virt-manager

or

>virsh console cac_fedora34

If is the first time you use it, might be necessary to add a connection for `QEMU/KVM user session`
