from bots.initial import Initial



class Factory:

    @staticmethod
    def _get_bots(bot:str):

        if bot == 'INITIAL':
            return Initial()
        else:
            raise ValueError('bot not found.')
