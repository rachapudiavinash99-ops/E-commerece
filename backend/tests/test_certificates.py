def test_certificate_public_verification(client):
    r = client.get("/api/certificates/verify/CERT-CP-2026-DEMO99")
    assert r.status_code == 200
    data = r.json()
    assert data["is_valid"] is True
    assert "Devin Miller" in data["student_name"]
    assert "Python" in data["course_title"]
