import inspect
from argparse import Namespace
from collections import defaultdict
from functools import partial

import teide.teide_lib as teide_lib
from scrapli import Scrapli


class MikNode:
    def __init__(self, host: str, username: str, password: str, port: int = 22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.platform = "mikrotik_routeros"
        self.libs = self.get_libs()

    def get_libs(self):
        return Namespace(
            **{
                name: partial(obj, self)
                for name, obj in inspect.getmembers(teide_lib, inspect.isfunction)
            }
        )

    def send_raw_command(self, cmd: str) -> str:
        with Scrapli(
            host=self.host,
            auth_username=self.username,
            auth_password=self.password,
            port=self.port,
            platform=self.platform,
            auth_strict_key=False,
        ) as conn:
            response = conn.send_command(cmd)
            return response.result

    def __getattr__(self, name):
        res = defaultdict(lambda: None, cli=self.libs)
        return res[name]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"host={self.host!r}, "
            f"username={self.username!r}, "
            f"password={self.password!r}, "
            f"port={self.port!r})"
        )
