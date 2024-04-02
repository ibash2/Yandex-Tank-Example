import requests
import sys

def print_request(request):
    method = request.method.encode()
    path_url = request.path_url.encode()
    headers = (''.join('{0}: {1}\r\n'.format(k, v) for k, v in request.headers.items())).encode()
    body = (request.body) or ""
    req = b''.join(
        [
            method,
            b' ',
            path_url,
            b' HTTP/1.1\r\n',
            headers,
            b'\r\n',
            body
        ]
        )
    req_size = str(len(req)).encode()
    return b''.join([req_size,b'\n',req,b'\r\n'])

#POST multipart form data
def post_multipart(host, port, namespace, files, headers, payload):
    req = requests.Request(
        'POST',
        'https://{host}:{port}{namespace}'.format(
            host = host,
            port = port,
            namespace = namespace,
        ),
        headers = headers,
        data = payload,
        files = files
    )
    prepared = req.prepare()
    return print_request(prepared)

if __name__ == "__main__":
    #usage sample below
    #target's hostname and port
    #this will be resolved to IP for TCP connection
    host = '127.0.0.1'
    port = '7777'
    namespace = '/back/create_user'
    #below you should specify or able to operate with
    #virtual server name on your target
    headers = {
        'Host': 'ya.ru'
    }
    payload = {"init_data":"query_id=AAHDeggyAAAAAMN6CDJEeJW4&user=%7B%22id%22%3A839416515%2C%22first_name%22%3A%22Ibragim%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22lbraqim%22%2C%22language_code%22%3A%22en%22%2C%22is_premium%22%3Atrue%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1711983273&hash=95ff8a1b754a7594e27f319a6f047f8a9dcf7fc3f4e134c125eb7dcbecfb10bf"}
    
    files = {
        # name, path_to_file, content-type, additional headers
        # 'file': ('image.jpeg', open('./image.jpeg', 'rb'), 'image/jpeg ', {'Expires': '0'})
    }
    # files = None

    sys.stdout.buffer.write(post_multipart(host, port, namespace, files, headers, payload))