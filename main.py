from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional


class Computer(BaseModel):
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float
    
api = FastAPI(openapi_tags=[
    {
        'name': 'home',
        'description': 'default functions'
    },
    {
        'name': 'items',
        'description': 'functions that are used to deal with items'
    }
])


@api.get('/', summary='Hello World', tags=['home'])
def get_index():
    """Returns greetings
    """
    return {'greetings': 'welcome'}

@api.put('/computer', name='Create a new computer')
def get_computer(computer: Computer):
    """Creates a new computer within the database
    """
    return computer

@api.get('/custom', name='Get custom header')
def get_content(custom_header: Optional[str] = Header(None, description='My own personal header')):
    return {
        'Custom-Header': custom_header
    }
    
@api.get('/items', tags=['home', 'items'])
def get_items():
    """returns an item
    """
    return {
        'item': "some item"
    }