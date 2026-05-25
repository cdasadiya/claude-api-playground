from pydantic import BaseModel, Field


class PythonTip(BaseModel):
    title: str = Field(description="Short title")
    explanation: str = Field(description="Detailed explanation")
    example: str = Field(description="Python code snippet")
