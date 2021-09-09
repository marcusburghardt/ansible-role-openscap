# Context
Here are quick references to possible useful commands in a day-to-day work

# OpenSCAP
oscap --version

## Getting Information
$ cd build
$ oscap info ssg-fedora-ds.xml

## Evaluation
$ sudo oscap xccdf eval --profile ospp ssg-fedora-ds.xml
$ sudo oscap xccdf eval --profile ospp --results-arf /tmp/arf.xml --report /tmp/report.html --oval-results ssg-fedora-ds.xml

## Generate remediation
$ oscap xccdf generate fix --fix-type ansible --result-id "" /tmp/arf.xml > /tmp/playbook.yml
$ oscap xccdf generate fix --fix-type bash --result-id "" /tmp/arf.xml > /tmp/bash-fix.sh
