# ITSP_report
ITSP中間レポート課題

## Build

このコードを実行するためには`pipenv`が必要です。
https://docs.pipenv.org/en/latest/


```
pipenv install
```

## Run

```
pipenv run python main.py
```

## Test

```
pipenv run py.test test.py
```

## 仕様

```
# イベント登録 API request
POST /api/v1/event
{"deadline": "2019-06-11T14:00:00+09:00", "title": "レポート提出", "memo": ""}

# イベント登録 API response
200 OK
{"status": "success", "message": "registered", "id": 1}

400 Bad Request
{"status": "failure", "message": form error message}

404 Not Found

{"status": "failure", "message": "404 not found"}
```

```
# イベント全取得 API request
GET /api/v1/event

# イベント全取得 API response
200 OK
{"events": [
    {"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "レポート提出", "memo": ""},
    ...
]}

404 Not Found

{"status": "failure", "message": "404 not found"}
```

```
# イベント1件取得 API request
GET /api/v1/event/${id}

# イベント1件取得 API response
200 OK
{"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "レポート提出", "memo": ""}

400 Bad Request

{"status": "failure", "message": "invalid request id"}


404 Not Found

{"status": "failure", "message": "404 not found"}```
