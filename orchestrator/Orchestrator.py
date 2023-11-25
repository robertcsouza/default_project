
from bots.factory import Factory



class Orchestrator:
  def __init__(self) -> None:
    ...    

  @staticmethod 
  def __get_avalible_bots() -> list[str]:
    #TODO make this method to dynamic
    return ["INITIAL"]
    
    
 
  def get_bots(self,product:str):
      bots_names = self.__get_avalible_bots()
      bots = []
      for bot_name in bots_names:
        bot = Factory._get_bots(bot=bot_name)
        bots.append(bot)
      
      return  bots