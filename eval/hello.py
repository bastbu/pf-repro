from promptflow import tool
import common.parent_b.mod_b


@tool
def my_python_tool(input1: str) -> str:
    return input1
