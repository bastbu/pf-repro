from promptflow import tool
import common.parent_a.mod_a
import common


@tool
def my_python_tool(input1: str) -> str:
    return input1
