"""
MCP server that exposes a single Windows perfmon counter resource.

The client provides the object and counter as separate parameters,
e.g. object="Processor(_Total)", counter="% Processor Time"

Requires: pip install fastmcp pywin32
Windows only.

Run it directly to test locally:
    python perfmon_server.py
"""

import logging
import time
import urllib.parse

import win32pdh
from fastmcp import FastMCP

logging.basicConfig(
    filename="perf_server.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

mcp = FastMCP("PerfMon Server")


def get_perf_counter(counter_path: str, sample_interval: float = 1.0) -> float:
    """
    Reads a single Windows perfmon counter and returns its value.

    counter_path example: r"\\Processor(_Total)\\% Processor Time"
    """
    query = win32pdh.OpenQuery()
    counter = win32pdh.AddCounter(query, counter_path)

    try:
        # Most counters (like % CPU time) need two samples to calculate
        # a value. The first sample alone is usually 0.
        win32pdh.CollectQueryData(query)
        time.sleep(sample_interval)
        win32pdh.CollectQueryData(query)

        _, value = win32pdh.GetFormattedCounterValue(counter, win32pdh.PDH_FMT_DOUBLE)
        return value
    finally:
        win32pdh.CloseQuery(query)


@mcp.resource("perf://counter/{object_name}/{counter_name}")
def perf_counter_resource(object_name: str, counter_name: str) -> dict:
    """
    Reads any perfmon counter, given its object and counter name.

    object_name example: "Processor(_Total)"
    counter_name example: "% Processor Time"

    Example URI:
        perf://counter/Processor(_Total)/%25%20Processor%20Time

    (counter_name is URL-encoded here because "%" has special meaning
    in URIs; spaces and parentheses are generally fine unencoded)
    """
    logging.info(
        "entering data resource; request asked for object_name=%s counter_name=%s",
        object_name,
        counter_name,
    )
    object_name = urllib.parse.unquote(object_name)
    counter_name = urllib.parse.unquote(counter_name)

    counter_path = f"\\{object_name}\\{counter_name}"
    value = get_perf_counter(counter_path)

    return {
        "object": object_name,
        "counter": counter_name,
        "value": value,
    }


if __name__ == "__main__":
    mcp.run()