def test_code_task_evaluation(client, student_auth_headers):
    # Correct solution code
    code_submission = """
def calculate_discount(original_price: float, discount_percent: float) -> float:
    return round(original_price - (original_price * (discount_percent / 100.0)), 2)
"""
    payload = {
        "task_id": 1,
        "code": code_submission
    }
    r = client.post("/api/tasks/submit", json=payload, headers=student_auth_headers)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "passed"
    assert data["score"] == 10
    assert data["passed_test_cases"] == data["total_test_cases"]


def test_code_task_security_sandbox(client, student_auth_headers):
    malicious_code = """
import os
os.listdir('/')
"""
    payload = {
        "task_id": 1,
        "code": malicious_code
    }
    r = client.post("/api/tasks/submit", json=payload, headers=student_auth_headers)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "syntax_error"
    assert "prohibited" in data["output"].lower()
