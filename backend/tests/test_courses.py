def test_get_courses_and_filter(client):
    r = client.get("/api/courses")
    assert r.status_code == 200
    data = r.json()
    assert "items" in data
    assert len(data["items"]) >= 1

    # Search filter
    r_search = client.get("/api/courses?query=Python")
    assert r_search.status_code == 200
    search_data = r_search.json()
    assert len(search_data["items"]) >= 1
    assert any("Python" in c["title"] for c in search_data["items"])


def test_get_course_detail_by_slug(client):
    r = client.get("/api/courses/python-312-masterclass-fundamentals-to-architecture")
    assert r.status_code == 200
    data = r.json()
    assert data["slug"] == "python-312-masterclass-fundamentals-to-architecture"
    assert data["instructor"]["full_name"] == "Guido Rossum"
