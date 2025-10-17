"""PEP 669: sys.monitoring low-overhead hooks.

Run with Python >=3.12
"""

import sys


EVENTS = sys.monitoring.events
PROBE_ID = 1  # arbitrary non-zero id for our tool


def on_call(frame, _) -> None:
    co = frame.f_code
    print(f"CALL {co.co_name} @ {co.co_filename}:{frame.f_lineno}")


def foo():
    return 42


sys.monitoring.register_callback(PROBE_ID, EVENTS.CALL, on_call)
sys.monitoring.set_events(PROBE_ID, EVENTS.CALL)

foo()

sys.monitoring.set_events(PROBE_ID, 0)


