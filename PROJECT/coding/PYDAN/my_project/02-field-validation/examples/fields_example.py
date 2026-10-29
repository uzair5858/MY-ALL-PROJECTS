from pydantic import basemodel # type : ignore 
from typing import list , dict , optional 

class cart (basemodel):
    user_id: int 
    items: list[str]
    quantites: dict[str , int]


    class blogpost (basemodel):
        title: str 
        content: str
        image_url: optional[str] = None