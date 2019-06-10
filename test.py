"""test code."""
import requests
import json
from jsonschema import validate
from jsonschema import FormatChecker


def test_normal_post():
    """Post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": ""
    }
    response = requests.post(url, json.dumps(request),
                             headers={'Content-Type': 'application/json'})
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert "status" in response_body
    assert response_body["status"] == "success"
    assert "message" in response_body
    assert response_body["message"] == "registered"
    assert "id" in response_body
    return response_body["id"]


def test_invalid_post1():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": 0
    }
    response = requests.post(url, json.dumps(request),
                             headers={'Content-Type': 'application/json'})
    print(response.json())
    response_body = response.json()
    assert response.status_code == 400
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_post2():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:000",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request),
                             headers={'Content-Type': 'application/json'})
    print(response.json())
    response_body = response.json()
    assert response.status_code == 400
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_post3():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:000",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 400
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_post1():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/a/v1/event/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_post2():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v/event/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_post3():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/even/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_post4():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_post5():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/api/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_post6():
    """Invalid post test."""
    host = "127.0.0.1:8080"
    url = 'http://{}/'.format(host)
    print(url)
    request = {
        "deadline": "2019-06-11T14:00:00+09:00",
        "title": "レポート提出",
        "memo": "0"
    }
    response = requests.post(url, json.dumps(request))
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_normal_get_all1():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert "events" in response_body
    assert isinstance(response_body["events"], list)
    assert len(response_body["events"]) > 0
    for e in response_body["events"]:
        assert "id" in e
        assert "deadline" in e
        assert "title" in e
        assert "memo" in e
        assert isinstance(e["id"], int)
        assert isinstance(e["deadline"], str)
        assert isinstance(e["title"], str)
        assert isinstance(e["memo"], str)
        schema = {
            "type": "string",
            "format": "date-time"
        }
        validate(e["deadline"], schema, format_checker=FormatChecker())


def test_normal_get_all2():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert "events" in response_body
    assert isinstance(response_body["events"], list)
    assert len(response_body["events"]) > 0
    for e in response_body["events"]:
        assert "id" in e
        assert "deadline" in e
        assert "title" in e
        assert "memo" in e
        assert isinstance(e["id"], int)
        assert isinstance(e["deadline"], str)
        assert isinstance(e["title"], str)
        assert isinstance(e["memo"], str)
        schema = {
            "type": "string",
            "format": "date-time"
        }
        validate(e["deadline"], schema, format_checker=FormatChecker())


def test_invalid_uri_get_all1():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/a/v1/event/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get_all2():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v/event/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get_all3():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/even/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get_all4():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get_all5():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get_all6():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_normal_get1():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/0'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert "id" in response_body
    assert "deadline" in response_body
    assert "title" in response_body
    assert "memo" in response_body
    assert isinstance(response_body["id"], int)
    assert isinstance(response_body["deadline"], str)
    assert isinstance(response_body["title"], str)
    assert isinstance(response_body["memo"], str)
    schema = {
        "type": "string",
        "format": "date-time"
    }
    validate(response_body["deadline"], schema, format_checker=FormatChecker())


def test_normal_get2():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert "id" in response_body
    assert "deadline" in response_body
    assert "title" in response_body
    assert "memo" in response_body
    assert isinstance(response_body["id"], int)
    assert isinstance(response_body["deadline"], str)
    assert isinstance(response_body["title"], str)
    assert isinstance(response_body["memo"], str)
    schema = {
        "type": "string",
        "format": "date-time"
    }
    validate(response_body["deadline"], schema, format_checker=FormatChecker())


def test_normal_get3():
    """Get all test."""
    id = test_normal_post()
    host = "127.0.0.1:8080"
    url = ('http://{}/api/v1/event/'+str(id)+'/').format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 200
    assert "id" in response_body
    assert "deadline" in response_body
    assert "title" in response_body
    assert "memo" in response_body
    assert isinstance(response_body["id"], int)
    assert isinstance(response_body["deadline"], str)
    assert isinstance(response_body["title"], str)
    assert isinstance(response_body["memo"], str)
    schema = {
        "type": "string",
        "format": "date-time"
    }
    validate(response_body["deadline"], schema, format_checker=FormatChecker())


def test_invalid_uri_get1():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/a/v1/event/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get2():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v/event/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get3():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/even/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get4():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get5():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_uri_get6():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/0/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 404
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_get1():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/114514/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 400
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body


def test_invalid_get2():
    """Get all test."""
    test_normal_post()
    host = "127.0.0.1:8080"
    url = 'http://{}/api/v1/event/-1919810/'.format(host)
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    response_body = response.json()
    assert response.status_code == 400
    assert "status" in response_body
    assert response_body["status"] == "failure"
    assert "message" in response_body
    assert "id" not in response_body
