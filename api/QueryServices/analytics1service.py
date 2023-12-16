from flask import jsonify
from flask.views import MethodView
from QueryController.analytics1 import Analytics1

class Analytics1_i_API(MethodView):
    def __init__(self):
        self.a1 = Analytics1()

    def get(self):
        result = self.a1.execute_i()
        return jsonify(result)



class Analytics1_ii_API(MethodView):
    def __init__(self):
        self.a1 = Analytics1()

    def get(self):
        result = self.a1.execute_ii()
        return jsonify(result)
