import asyncio
from typing import Self
import tomllib


class Runner:
    def __init__(self, cfg: dict) -> None:
        self.cfg = cfg

    async def run(self) -> None:
        tasks = self.cfg.get("tasks", [])
        async with asyncio.TaskGroup() as tg:
            for task in tasks:
                match task:
                    case {"type": "echo", "msg": msg}:
                        tg.create_task(self._echo(msg))
                    case {"type": "sleep", "secs": secs}:
                        tg.create_task(asyncio.sleep(secs))
                    case _:
                        print("unknown task", task)

    async def _echo(self, msg: str) -> None:
        print(msg)


def main() -> None:
    with open("capstone/src/config.toml", "rb") as f:
        cfg = tomllib.load(f)
    asyncio.run(Runner(cfg).run())


if __name__ == "__main__":
    main()


