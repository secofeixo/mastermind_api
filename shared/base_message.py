from pydantic import BaseModel


class Message(BaseModel):
    """
    Data class that defines the schema of the API
    error and information messages.
    """
    message: str
