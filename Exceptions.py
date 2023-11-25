
class ExceptionApi(Exception):
  def __init__(self, message:str,status:str) -> None:
    self.message = message
    self.status = status
    super().__init__(message)
