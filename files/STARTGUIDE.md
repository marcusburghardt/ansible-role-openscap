# Context
Working with OpenSource and Security we are immersed in an intensive learning environment.
But if you want to already start doing some code and contributing, this guide is for you. ;)

I would personally advice to not be worried about all the concepts, syntaxes, standards and
structure by now. Naturally you will get aware of this along the time, when the challenges are appearing as learning opportunities.

In very short sentences, this is a macro overview to understand the OpenSCAP projects:

1 - Governments, Authorities, Organizations, Companies and any other stakeholder define Security Standards based on best practices of hardening.
However, these definitions are usually high-level. It means that many times it is clear what is desired but is not always clear how to achieve a desired state.

2 - So, we have ComplianceAsCode project, more specifically in the `content` repository.
What we do here is to create technical rules to ensure the systems properly achieve a desired state which finally increase the respective system security.

3 - Once we have these technical rules defined, we need a Scanner tool which will interpret these rules and make sure the analysed system is in compliance with the desired state. 
Here the OpenSCAP Scanner tool enter in the game.

4 - So, basically the ComplianceAsCode (`content`) generates rules to translated standards requirements in technical rules which are lately consumed by a Scanner (`OpenSCAP`). That said, OpenSCAP and Content are directly related to each other. This is why this Ansible role is called `openscap`, which is not a reference to OpenSCAP scanner itself, but all the projects under the OpenSCAP umbrella, like:
- Content - https://github.com/ComplianceAsCode/content/
- OpenSCAP - https://github.com/OpenSCAP/openscap
- scap-workbench - https://github.com/OpenSCAP/scap-workbench
- oscap-anaconda-addon - https://github.com/OpenSCAP/oscap-anaconda-addon
- and more...

5 - Once we have a content and a scanner, we can detect compliance gaps. But this is actually (intentionally) only informative. In some cases, stakeholders want to also fix the detected gaps in a reliable, effective, efficient and elegant way. Due that the `ComplianceAsCode` also deliver remediation for many rules mostly in Bash but also in Ansible.

We can summarize a little more these 5 points saying that:
- OpenSCAP projects can, in an easier way, detect and close compliance GAPs for many security standards.

So, as far the initial release of this role is more focused on ComplianceAsCode content, it should be totally compatible to work with other OpenSCAP projects.

# Main Concepts
## Rules and Profiles
Although there are many different Security Standards, they tend to have quite a lot of similarities in some level.
It means that the most granular unit inside the Content repository are the **rules**.
The rule is actually the technical instruction for the scanner (OpenSCAP).

For efficiency, we group these rules in **Profiles** which finally represent a group of rules applicable for a specific product (RHEL, Ubuntu, OpenShift, etc) to achieve the compliance of a specific standard. Here are some examples of profiles:
- pci-dss.profile
- stig.profile
- stig.profile

You can better explore this practicing the suggested LABs in:
`~/OpenSCAP/Labs/VMs/INSTRUCTIONS_LABS.md`

## Build Process
Most of the rules created in the Content project take advantage of nice resources for optimization and automation, like templates, jinja2, python scripts, etc.

You will naturally be familiar with these resources along the time.
But it is nice to know about this now to understand why do we have a build process in a project which supposedly, in a first glance, only generate content.
So, the build process interpret and process everything together to finally generate the consumable artifacts for the Scanner (OpenSCAP).

You can go deep on that later, if desired:
- https://complianceascode.readthedocs.io/en/latest/manual/developer/02_building_complianceascode.html
- https://complianceascode.readthedocs.io/en/latest/manual/developer/07_understanding_build_system.html

# Contributing
Now you have the most important concepts, here is the fast track to start contributing:

## Fork a Repository
Go to the desired repository using your own GITHUB account and Fork it.
Once it is forked, include the forked repository in the `git_repos` list of your playbook, like in this example:
```
    git_repos:
      - { enabled: True, type: 'fork', name: 'ComplianceAsCode(fork)->content',
          repo: 'https://github.com/marcusburghardt/content.git',
          dest: 'ComplianceAsCode/content',
          remote: 'https://github.com/ComplianceAsCode/content.git',
          remote_name: 'upstream' }
```
Observe the `remote` parameter here, which is pointing to the main project in Upstream. This will be very useful later.

Run your playbook again and check the Forks folder:
```bash
ansible-playbook -K ansible_openscap
cd ~/OpenSCAP/Forks/ComplianceAsCode/content
```

You are totally free to choose another `dest` if desired. ;)

## Check the remotes
Inside your forked repository, check the `remotes`:
```bash
git remote -v
```

## Update your fork
It is always interesting to update your fork before start coding:
```bash
git checkout master
git pull upstream master
git push
```

## Create a new branch
It is strongly recommended to not work in the master branch. So, create a new one:
```bash
git checkout -b my_new_branch
```

Now you can start coding in your new branch.
If you want to check your existing branches:
```bash
git branch
```

## Send a Pool Request
Once your patch is ready, you have to submit it to the main project, where maintainers and other contributors can review, accept (`merge`) or aks adjusts.
Use `git add` to include the desired changes in the staging area.
Once it is done, commit it:
```bash
git commit -m
git log --graph
```

Now you have to push this commit to Github:
```bash
git push
```

Once your commit is in Github, access your fork from the Github webpage and follow the instructions to create a Pool Request (PR).

Now you can follow the project and wait for feedbacks.

## Update a patch
It is really common, regardless the level of experience, that we have some improvements to do in the "first version" of our patch. Because that the review process in OpenSource projects is so important. Not to judge codes, but to continually improve together.

So, if you need to update your patch, continue working in your branch and when finished it is necessary to update your PR.

Usually, if it is a small change, just amend your last commit and that is it:
```bash
git add ...
git commit --amend
git push --force
```

This will automatically update your PR in the Upstream project.

## Rebase your branch
Sometimes we are not able, for any reason, to update a PR very soon. On the other hand, the project is active and many merges may happen this meantime. If the merges are not conflicting with your patch, it is usually fine. However, it is a good practice to rebase your patch if some days have passed.

```bash
git checkout master
git pull upstream master
git push
git checkout my_new_branch
git rebase master
```

Then follow the steps from **Update a patch**.

# Testing rules
If you changed an existing rule of even created a new one, it sounds reasonable to test it locally. For that you can provisioning VMs using the Vagrantfiles in this repository.

Here is an example of how to provisioning a Fedora VM and testing the rule `audit_rules_login_events_lastlog` on it.

```bash
cd ~/OpenSCAP/Labs/VMs/Fedora
vagrant up
cd ~/OpenSCAP/Forks/ComplianceAsCode/content
./build_product --datastream-only fedora

./tests/test_suite.py rule --libvirt qemu:///session cac_fedora34 --datastream ./build/ssg-fedora-ds.xml audit_rules_login_events_lastlog
```

You can know more about the testing VMs in `~/OpenSCAP/Labs/VMs/INSTRUCTIONS_VMS.md`.

And you can go deep on that later, if desired:
- https://complianceascode.readthedocs.io/en/latest/tests/README.html
- https://complianceascode.github.io/template/2021/03/25/tests_howto.html

# Reviewing a PR locally
```bash
git fetch upstream pull/ID/head:REVIEWBRANCH
git checkout REVIEWBRANCH
```
At this point you can do all tests you consider necessary. Once they are finished, remove the branch.
```bash
git branch -d REVIEWBRANCH
```
# OpenSCAP
More information about how to contribute in the OpenSCAP scanner can be found here:
- https://github.com/OpenSCAP/openscap/blob/maint-1.3/docs/contribute/contribute.adoc