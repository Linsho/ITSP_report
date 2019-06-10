"""main code."""
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json
import cgi
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema import FormatChecker
import iso8601
import traceback

database = {}


class NotFound(Exception):
    """404 not found error."""

    pass


class BadRequest(Exception):
    """400 bat request error."""

    pass


class RequestHandler(BaseHTTPRequestHandler):
    """resuest handler."""

    def do_GET(self):
        """GET handler."""
        parsed_path = urlparse(self.path)
        path_elements = parsed_path.path.split('/')[1:]

        try:
            if path_elements[0] == 'api':
                if len(path_elements) < 2:
                    raise NotFound
                if path_elements[1] == 'v1':
                    if len(path_elements) < 3:
                        raise NotFound
                    if path_elements[2] == 'event':
                        if len(path_elements) == 3 or \
                           len(path_elements) == 4 and path_elements[3] == "":
                            response = {"events": []}
                            for id, data in database.items():
                                response["events"].append({
                                    "id": id,
                                    "deadline": data["deadline"].isoformat(),
                                    "title": data["title"],
                                    "memo": data["memo"]
                                })
                            self.send_response(200)
                            self.send_header('Content-type',
                                             'application/json')
                            self.end_headers()

                            response_body = json.dumps(response)
                            self.wfile.write(response_body.encode('utf-8'))
                            return
                        elif len(path_elements) == 4 or \
                                len(path_elements) == 5 and \
                                path_elements[4] == "":
                            id = int(path_elements[3])
                            if id not in database:
                                raise BadRequest("invalid request id")
                            data = database[id]
                            response = {
                                "id": id,
                                "deadline": data["deadline"].isoformat(),
                                "title": data["title"],
                                "memo": data["memo"]
                            }
                            self.send_response(200)
                            self.send_header('Content-type',
                                             'application/json')
                            self.end_headers()

                            response_body = json.dumps(response)
                            self.wfile.write(response_body.encode('utf-8'))
                            return
                        else:
                            raise BadRequest("invalid request uri format")
                    else:
                        raise NotFound
                else:
                    raise NotFound
            else:
                raise NotFound

        except BadRequest as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "failure",
                "message": e.args[0],
            }
            response_body = json.dumps(response)
            self.wfile.write(response_body.encode('utf-8'))

            return
        except NotFound as e:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "failure",
                "message": "404 not found",
            }
            response_body = json.dumps(response)
            self.wfile.write(response_body.encode('utf-8'))
            return

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            self.send_response(500)
            self.end_headers()
            return

    def do_POST(self):
        """POST handler."""
        parsed_path = urlparse(self.path)
        path_elements = parsed_path.path.split('/')[1:]
        try:
            if len(path_elements) < 1:
                raise NotFound
            if path_elements[0] == 'api':
                if len(path_elements) < 2:
                    raise NotFound
                if path_elements[1] == 'v1':
                    if len(path_elements) < 3:
                        raise NotFound
                    if path_elements[2] == 'event':
                        if 'content-type' not in self.headers:
                            raise BadRequest("request is not contain \
content-type")
                        ctype, pdict = cgi.parse_header(
                            self.headers.get('content-type'))
                        if ctype != 'application/json':
                            raise BadRequest("content-type is not \
application/json")
                        length = int(self.headers.get('content-length'))
                        request = json.loads(self.rfile.read(length))
                        id = len(database)
                        schema = {
                            "type": "object",
                            "properties": {
                                "deadline": {
                                    "type": "string",
                                    "format": "date-time",
                                },
                                "title": {"type": "string"},
                                "memo": {"type": "string"}
                            }
                        }
                        validate(request, schema,
                                 format_checker=FormatChecker())
                        data = {
                            "deadline":
                            iso8601.parse_date(request["deadline"]),
                            "title": request["title"],
                            "memo": request["memo"]
                        }
                        database[id] = data
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        response = {
                            "status": "success",
                            "message": "registered",
                            "id": id
                        }
                        response_body = json.dumps(response)
                        self.wfile.write(response_body.encode('utf-8'))
                        return
                    else:
                        raise NotFound
                else:
                    raise NotFound
            else:
                raise NotFound

        except BadRequest as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "failure",
                "message": e.args[0],
            }
            response_body = json.dumps(response)
            self.wfile.write(response_body.encode('utf-8'))

            return
        except NotFound as e:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "failure",
                "message": "404 not found",
            }
            response_body = json.dumps(response)
            self.wfile.write(response_body.encode('utf-8'))
            return

        except ValidationError as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "failure",
                "message": e.args[0]
            }
            response_body = json.dumps(response)
            self.wfile.write(response_body.encode('utf-8'))
            return
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            self.send_response(500)
            self.end_headers()
            return


def main():
    """main."""
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
