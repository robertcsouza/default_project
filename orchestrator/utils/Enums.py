from enum import Enum

class StatusCode(Enum):
    SUCCESS = 200
    INTERNAL = 500
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
