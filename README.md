ansible-role-openscap
=========

This role will ensure the development environment for contributing with the OpenSCAP
Ecosystem projects is properly installed and configured. So, you can skip (for now)
the long reading documentation and start coding earlier. ;)
  
All the variables you may want to change are defined in "defaults/main.yml".
You can change directly there or, more elegantly, overridden them in your playbook.  

This role will:
- Install all the necessary packages;
    - Packages required for development, tests and extra tools.
- Configure git;
    - Define the main editor
    - Ensure the name and email which will appear on commits
    - Ensure proper definition for autocrlf.
- Configure the basic environment:
    - Create the main folder (~/OpenSCAP)
    - Update the PATH variable, if necessary.
    - Create the Upstream sub-folder, if any upstream repository is enabled.
    - Create the Forks sub-folder, if any forked repository is enabled.
- Populate the environment
    - Clone and update the "main" (Upstream) repositories, if any is enabled.
    - Clone the "fork" repositories, if any is present and enabled.
    - Clone and "lab" repositories, if any is present and enabled.
    - Copy the general instructions files to ~/OpenSCAP
- Configure Labs
    - Copy the Vagrantfiles to ~/OpenSCAP/Labs/VMs
    - Copy instructions files for Labs and Tests related to VMs in Labs/VMs.
    - TODO: Copy instructions files for Lats and Tests related to Containers in Labs/Containers.
- Configure VSCODE
    - OBS.: It is totally optional, but strongly recommended to use VSCode.
    - Add the official repositories.
    - Install and configure VSCode to already add ~/OpenSCAP in the Workspace.
    - Install the main useful extensions.
    - Make sure VSCode is updated.
- Install Python Modules
    - Install extra python modules necessary for CMakeTests or Json.

TODO:
- 

To install this role:  
$ ansible-galaxy role install marcusburghardt.ansible_role_openscap


Requirements
------------

- python3

Role Variables
--------------

You can customize your environment in a very simple and centralized way editing some variables in:
- defaults/main.yml

However, I strongly recommend to override these variables in your playbook. 
Also, this is much more elegant besides give you more flexibility. ;)

To do so, explore the "defaults/main.yml", which is very well documented to clarify the
purpose and effect of any variable. Then, just copy what your want to change in your playbook
and adjust it as desired. Take a look in the Example Playbook section.

In some rare cases, you may change some configuration to reflect your local environment in:
- vars/*.yml


Dependencies
------------

None

Example Playbook
----------------

This playbook will prepare everything with the essential variables.
You can find a sample in "files/Ansible_Samples", named "ansible_openscap.yml".

For this example, lets call this playbook file as "ansible_openscap.yml":

---
- hosts: linux
  vars:
    - available_tasks:
      - { enabled: True, name: 'install_packages' }
      - { enabled: True, name: 'configure_git' }
      - { enabled: True, name: 'configure_env' }
      - { enabled: True, name: 'populate_env' }
      - { enabled: True, name: 'configure_vscode' }
      - { enabled: True, name: 'configure_labs' }
      - { enabled: True, name: 'install_python_modules' }
  roles:
    - marcusburghardt.ansible_role_openscap

Considering the inventory file is in the same folder and is called "hosts_openscap".
OBS.: You can also find a sample in "files/Ansible_Samples", named "hosts_openscap".

Now, run this command to see the magic happen:  
$ ansible-playbook -K -i hosts_vscode ansible_vscode.yml  

Maybe you would like to set some ansible configurations for this environment.  
For instance, define a local folder to hold downloads roles.  
You can find an example of ansible.cfg file in "files/Ansible_Samples" folder, named "ansible.cfg".

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
