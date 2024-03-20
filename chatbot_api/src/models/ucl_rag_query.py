from pydantic import BaseModel


class UclQueryInput(BaseModel):
    text: str


class UclQueryOutput(BaseModel):
    input: str
    output: str
    intermediate_steps: list[str]
