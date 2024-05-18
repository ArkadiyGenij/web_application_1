from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        with open('index.html', 'rb') as file:
            content = file.read().decode('utf-8')
        return content

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(page_content.encode('utf-8'))


if __name__ == '__main__':
    webServer = HTTPServer(('localhost', 8080), MyServer)
    print("Server started http://localhost:8080/")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
