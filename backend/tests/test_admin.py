def test_admin_dashboard_metrics(client, admin_auth_headers):
    r = client.get("/api/admin/analytics", headers=admin_auth_headers)
    assert r.status_code == 200
    data = r.json()
    assert data["total_users"] >= 1
    assert data["total_courses"] >= 1


def test_admin_forbidden_for_students(client, student_auth_headers):
    r = client.get("/api/admin/analytics", headers=student_auth_headers)
    assert r.status_code == 403
