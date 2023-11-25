from flask import Blueprint, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import werkzeug
from orchestrator.Orchestrator import Orchestrator
from orchestrator.utils.ApiResult import ApiResult as api
from Exceptions import ExceptionApi
bp = Blueprint('views',__name__)

orchestrator = Orchestrator()
@bp.route('/')
def index():
    return api.result(data={'online':True})

@bp.errorhandler(werkzeug.exceptions.BadRequest)
@bp.errorhandler(Exception)
@bp.errorhandler(ExceptionApi)
def handle_exception(e):
    
    if isinstance(e,ExceptionApi):
        print(e)
        return api.exception(data=e.message,status=e.status)
    return api.exception(data=e.args)