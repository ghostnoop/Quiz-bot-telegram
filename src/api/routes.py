from sanic.response import json
from sanic_cors import cross_origin

from .services import service_back_call, service_after_quiz


def setup_routes(app):

    @app.post('/afterquiz')
    @cross_origin(app)
    async def after_quiz_create(request):
        response = await service_after_quiz(request.json)
        if response is True:
            return json({'message': "OK"}, status=201)
        else:
            return json({'message': response}, status=400)

    @app.post('/backcall')
    @cross_origin(app)
    async def back_call_create(request):
        response = await service_back_call(request.json)
        if response is True:
            return json({'message': "OK"}, status=201)
        else:
            return json({'message': response}, status=400)
