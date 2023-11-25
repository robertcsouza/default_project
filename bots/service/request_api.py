from json import JSONDecodeError
import json
from requests import Session
from Exceptions import ExceptionApi
from bots.service.types import Fetch, Response,Request
from orchestrator.utils.Enums import StatusCode
from orchestrator.utils.languages import NOT_FOUND, UNAUTHORIZED
class RequestApi:
    
    def __init__(self) -> None:
        self.session = Session()
    
    def fetch(self,request:Request) -> Response:
        response = self.session.request(method=request.method,url=request.url,json=request.json)
        return Response(status_code=response.status_code,text=response.text)

    def get_response(self,fetch:Fetch,request:Request):
        try:
            response = fetch(request)
            if response.status_code == 401:
                raise ExceptionApi(message=UNAUTHORIZED,status=StatusCode.UNAUTHORIZED)
            if response.status_code == 404:
                raise ExceptionApi(message=NOT_FOUND,status=StatusCode.NOT_FOUND)   
            json_decoded = json.loads(response.text)
            return json_decoded
        except JSONDecodeError:
            return response.text
        except ExceptionApi as exceptionApi:
            raise exceptionApi
        except Exception as exception:
            raise ExceptionApi(message=exception.args,status=StatusCode.INTERNAL)
        