# Context
Here are quick references to possible useful commands in a day-to-day work

# OpenSCAP
>oscap --version

## Getting Information
>cd build
>oscap info ssg-fedora-ds.xml

## Evaluation
>sudo oscap xccdf eval --profile ospp ssg-fedora-ds.xml
>sudo oscap xccdf eval --profile ospp --results-arf /tmp/arf.xml --report /tmp/report.html --oval-results ssg-fedora-ds.xml
>sudo oscap xccdf eval --profile ospp --rule xccdf_org.ssgproject.content_rule_accounts_umask_interactive_users --results-arf /tmp/arf.xml --report /tmp/report.html --oval-results ssg-fedora-ds.xml

## Remote Evaluation
oscap-ssh root@<REMOTE HOST> 22 xccdf eval --verbose DEVEL --results-arf /tmp/oscap-test-arf.xml --benchmark-id xccdf_org.ssgproject.content_benchmark_RHEL-9 --profile cis --progress --oval-results --report /tmp/oscap-test.html --rule xccdf_org.ssgproject.content_rule_set_password_hashing_algorithm_systemauth build/ssg-rhel9-ds.xml

## Generate remediation
### Ansible
>oscap xccdf generate fix --fix-type ansible --result-id "" /tmp/arf.xml > /tmp/playbook.yml

### Bash
>oscap xccdf generate fix --fix-type bash --result-id "" /tmp/arf.xml > /tmp/bash-fix.sh
