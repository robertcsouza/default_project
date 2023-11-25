from asyncio import Protocol
from dataclasses import dataclass
from typing import Any, Literal, Optional
from requests import Request

from orchestrator.utils.Enums import StatusCode

@dataclass 
class Response:
    status_code:int
    json:Optional[any] = None
    text:Optional[str] = None

@dataclass 
class Request:
    method:Literal["GET","POST","PUT","DELETE"]
    url:str
    json:Optional[Any]=None
    data:Optional[Any]=None
    
    
class Fetch(Protocol):
    def __call__(self,request:Request) -> Response:
        ...