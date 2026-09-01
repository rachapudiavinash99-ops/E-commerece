def test_quiz_submission(client, student_auth_headers):
    # Answer question 1 (option 3 is Tuple) and question 2 (option 2 is False)
    payload = {
        "quiz_id": 1,
        "answers": {
            "1": [3],
            "2": [6]
        }
    }
    r = client.post("/api/quizzes/submit", json=payload, headers=student_auth_headers)
    assert r.status_code == 200
    data = r.json()
    assert "score" in data
    assert data["passed"] in [True, False]
