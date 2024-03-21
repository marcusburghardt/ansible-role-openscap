ansible-role-openscap
=========

This role will ensure the development environment for contributing with the OpenSCAP Ecosystem projects is properly installed and configured.
You can skip, **for now**, the long reading documentation and start coding earlier. ;)
  
All the variables you may want to change are defined in "defaults/main.yml".
You can change directly there or, more elegantly and recommended, overridden them in your Playbook.

**This role will**:
- Install all the necessary packages:
    - Packages required for development, tests and extra tools.
- Install Python Modules:
    - Install extra python modules necessary for CMakeTests or JSON, for example.
- Configure git:
    - Define the main editor
    - Ensure the name and email which will appear on commits
    - Ensure proper definition for autocrlf. 
- Configure the basic environment:
    - Create the main folder (~/OpenSCAP)
    - Update the PATH variable, if necessary.
    - Create the Forks sub-folder, if any forked repository is enabled.
- Configure Labs:
    - Copy the Vagrantfiles to ~/OpenSCAP/Labs/VMs
    - Copy instructions files for Labs and Tests related to VMs in Labs/VMs.
    - TODO: Copy instructions files for Labs and Tests related to Containers in Labs/Containers.
- Populate the environment:
    - Clone the "fork" repositories, if any is present and enabled.
    - Clone and "lab" repositories, if any is present and enabled.
    - Copy the general instructions files to ~/OpenSCAP

TODO
----
- Open for constructive ideas.

To install this role
---------------------
```bash
ansible-galaxy role install marcusburghardt.ansible_role_openscap
```

Requirements
------------

- python3

Role Variables
--------------

You can customize your environment in a very simple and centralized way editing some variables in:
- defaults/main.yml

However, I strongly recommend to override these variables in your Playbook. 
This is much more elegant and gives you more flexibility. ;)

To do so, explore the "defaults/main.yml", which is very well documented to clarify the
purpose and effect of any variable. Then, just copy what your want to change in your Playbook
and adjust it as desired. Take a look in the Example Playbook section.

In some rare cases, you may change some configuration to reflect your local environment in:
- vars/*.yml
If this was necessary for you by any reason, consider to propose a PR to improve the role.


Dependencies
------------

None

Example Playbook
----------------

This playbook will prepare everything with the essential variables.
You can find a sample in `files/Ansible_Samples`, named `ansible_openscap.yml`.

For this example, lets call this playbook file as `ansible_openscap.yml`, with the following content:

```
- hosts: linux
  vars:
    - available_tasks:
      - { enabled: true, name: 'install_packages' }
      - { enabled: true, name: 'configure_git' }
      - { enabled: true, name: 'configure_env' }
      - { enabled: true, name: 'populate_env' }
      - { enabled: true, name: 'configure_labs' }
      - { enabled: true, name: 'install_python_modules' }
  roles:
    - marcusburghardt.ansible_role_openscap
```
Note that this ansible role was created by a group of specific tasks (available_tasks). You can disable and enable the tasks combination according to your demands.
Considering the inventory file `hosts_openscap` is in the same folder, with the following content:
```
[linux:children]
install_packages
configure_git
configure_env
populate_env
configure_labs
install_python_modules

...lines omitted for better reading...
``` 
OBS.: You can also find a sample in `files/Ansible_Samples`, named `hosts_openscap`.

Now, run this command to see the magic happen:
```bash
ansible-playbook -K ansible_openscap.yml 
```

Maybe you would like to set some ansible configurations for this environment.  
For instance, define a local folder to hold downloads roles.  
You can find an example of ansible.cfg file in `files/Ansible_Samples` folder, named `ansible.cfg`.

License
-------

This Source Code Form is subject to the terms of the Mozilla Public  
License, v. 2.0. If a copy of the MPL was not distributed with this  
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Author Information
------------------

Marcus Burghardt
- https://github.com/marcusburghardt/
- https://www.linkedin.com/in/marcusburghardt/
