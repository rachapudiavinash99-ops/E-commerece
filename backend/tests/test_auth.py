import secrets

def test_register_and_login(client):
    unique_email = f"user_{secrets.token_hex(4)}@codepulse.io"
    reg_payload = {
        "email": unique_email,
        "password": "Password123!",
        "full_name": "New Student",
        "role": "student"
    }
    r = client.post("/api/auth/register", json=reg_payload)
    assert r.status_code == 201
    data = r.json()
    assert "access_token" in data
    assert data["email"] == unique_email

    # Login
    login_payload = {
        "email": unique_email,
        "password": "Password123!"
    }
    r_login = client.post("/api/auth/login", json=login_payload)
    assert r_login.status_code == 200
    login_data = r_login.json()
    assert "access_token" in login_data

    # Test /me
    headers = {"Authorization": f"Bearer {login_data['access_token']}"}
    r_me = client.get("/api/auth/me", headers=headers)
    assert r_me.status_code == 200
    assert r_me.json()["email"] == unique_email


def test_login_invalid_password(client):
    r = client.post("/api/auth/login", json={"email": "admin@codepulse.io", "password": "WrongPassword"})
    assert r.status_code == 401
