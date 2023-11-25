import json

def parse_json(str_to_parse:str) -> dict:
    return json.loads(str_to_parse)