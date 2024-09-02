from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel


def write_report(filename, html):
    with open(filename, "w") as f:
        f.write(html)


class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str
