from flask import jsonify

from orchestrator.utils.Enums import StatusCode
class ApiResult():
    @staticmethod
    def result(data=None):
        if not data:
            return jsonify({"status":"success","message":"Operation performed successfully"})
        return jsonify({"status":"success","message":"Operation performed successfully","data":data})
    @staticmethod
    def exception_auth(data=None):    
        return jsonify({"status":"Fail","message":"Operation Fail","data":data}),401    
    @staticmethod
    def exception(data=None,status=StatusCode.INTERNAL):    
        print(status)
        return jsonify({"message":"Operation Fail","data":data,"status":status.name}),status.value