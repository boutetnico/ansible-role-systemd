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
| systemd_dependencies        | true     |                          | list      | See `defaults/main.yml`.                      |
| systemd_package             | true     | `systemd`               | string    |                                               |
| systemd_package_state       | true     | `present`                | string    |                                               |
| systemd_config              | true     |                          | dict      | Configuration object. See `defaults/main.yml`.|

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-systemd

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
