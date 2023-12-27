def parse_cookies(cookie_string: str):
    """
    Parses a cookie string into a list of cookie dicts.
    """
    cookies = []
    for c in cookie_string.split(";"):
        c = c.strip()
        if c:
            k, v = c.split("=", 1)
            cookies.append({"name": k, "value": v})
    return cookies

def stringify_cookies(cookies) -> str:
    """
    Creates a cookie string from a list of cookie dicts.
    """
    return ";".join([f"{c['name']}={c['value']}" for c in cookies])


