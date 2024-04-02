import sys

# POST||127.0.0.1:7777/back/create_user||Test||{"init_data":"query_id=AAHDeggyAAAAAMN6CDJEeJW4&user=%7B%22id%22%3A839416515%2C%22first_name%22%3A%22Ibragim%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22lbraqim%22%2C%22language_code%22%3A%22en%22%2C%22is_premium%22%3Atrue%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1711983273&hash=95ff8a1b754a7594e27f319a6f047f8a9dcf7fc3f4e134c125eb7dcbecfb10bf"}


def make_ammo(method, url, headers, case, body):
    """ makes phantom ammo """
    # http request w/o entity body template
    req_template = (
          "%s %s HTTP/1.1\r\n"
          "%s\r\n"
          "\r\n"
    )

    # http request with entity body template
    req_template_w_entity_body = (
          "%s %s HTTP/1.1\r\n"
          "%s\r\n"
          "Content-Length: %d\r\n"
          "\r\n"
          "%s\r\n"
    )

    if not body:
        req = req_template % (method, url, headers)
    else:
        req = req_template_w_entity_body % (method, url, headers, len(body), body)

    # phantom ammo template
    ammo_template = (
        "%d %s\n"
        "%s"
    )

    return ammo_template % (len(req), case, req)


def main():
    for stdin_line in sys.stdin:
        try:
            method, url, case, body = stdin_line.split("||")
            body = body.strip()
        except ValueError:
            method, url, case = stdin_line.split("||")
            body = None

        method, url, case = method.strip(), url.strip(), case.strip()

        headers = "Host: hostname.com\r\n" + \
            "User-Agent: tank\r\n" + \
            "Accept: */*\r\n" + \
            "Connection: Close"

        sys.stdout.write(make_ammo(method, url, headers, case, body))


if __name__ == "__main__":
    main()