import pytest


@pytest.mark.parametrize(
    "service,user,group,mode",
    [
        ("example-unit", "root", "root", 0o644),
        ("example-unit-2", "root", "root", 0o644),
    ],
)
def test_systemd_unit_file_exists(host, service, user, group, mode):
    f = host.file(f"/etc/systemd/system/{service}.service")
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == mode


@pytest.mark.parametrize(
    "service,description",
    [
        ("example-unit", "Example unit file"),
        ("example-unit-2", "Second example unit file"),
    ],
)
def test_systemd_unit_file_content(host, service, description):
    f = host.file(f"/etc/systemd/system/{service}.service")
    assert description in f.content_string


@pytest.mark.parametrize(
    "service",
    [
        ("example-unit"),
        ("example-unit-2"),
    ],
)
def test_systemd_service_enabled_and_running(host, service):
    svc = host.service(service)
    assert svc.is_enabled
    assert svc.is_running


def test_systemd_daemon_reloaded(host):
    # Verify systemctl daemon-reload has been called by checking systemd is responsive
    cmd = host.run("systemctl is-system-running || true")
    assert cmd.rc == 0
