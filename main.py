from fastapi import FastAPI, Header

api = FastAPI(
    title="My API v1.0.1",
    description="My own API powered by FastAPI.",
    version="1.0.1")

@api.get('/')
def get_index():
    """Returns greetings
    """
    return {'greetings': 'welcome'}