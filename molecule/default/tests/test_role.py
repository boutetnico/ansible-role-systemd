import pytest


def test_systemd_unit_file_exists(host):
    f = host.file("/etc/systemd/system/example-unit.service")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_systemd_service_enabled_and_running(host):
    svc = host.service("example-unit")
    assert svc.is_enabled
    assert svc.is_running
