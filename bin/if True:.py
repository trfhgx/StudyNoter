from mitmproxy.tools import main
from mitmproxy.tools.dump import DumpMaster
import threading
import asyncio
import time
from PIL import Image
import io
import json

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




block_hosts = [ "instagram.com", "discord.com", 'twitter.com']

class Addon(object):

    def request(self, flow):
        if any(i in flow.request.pretty_url for i in block_hosts):
            print('blocked')
            flow.kill()

    def response(self, flow):
        pass


if __name__ == "__main__":
    options = main.options.Options(listen_host='192.168.100.4', listen_port=8081, http2=True)
    m = DumpMaster(options, with_termlog=False, with_dumper=False)
    m.addons.add(Addon())
    m.run()




# see source mitmproxy/master.py for details
def loop_in_thread(loop, m):
    asyncio.set_event_loop(loop)  # This is the key.
    m.run_loop(loop.run_forever)


