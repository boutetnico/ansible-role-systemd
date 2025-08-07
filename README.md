[![tests](https://github.com/boutetnico/ansible-role-systemd/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-systemd/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.systemd-blue.svg)](https://galaxy.ansible.com/boutetnico/systemd)

ansible-role-systemd
====================

This role configures systemd unit files.

Requirements
------------

Ansible 2.15 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default                  | Choices   | Comments                                      |
|------------------------------|----------|--------------------------|-----------|-----------------------------------------------|
| systemd_unit_files           | true     |                          | list      |                                               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-systemd

          systemd_unit_files:
            - name: example-unit
              config:
                Unit:
                  Description: Example unit file
                Service:
                  ExecStart: /bin/bash -c "while true; do sleep 3600; done"
                  Restart: always
                  User: root
                  Group: root
                  LimitNOFILE: 65536
                  TimeoutStopSec: 10
                Install:
                  WantedBy: multi-user.target

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
