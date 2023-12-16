from flask import jsonify
from flask.views import MethodView
from QueryController.analytics3 import Analytics3

class Analytics3_i_API(MethodView):
    def __init__(self):
        self.a3 = Analytics3()

    def get(self):
        result = self.a3.execute_i()
        return jsonify(result)



class Analytics3_ii_API(MethodView):
    def __init__(self):
        self.a3 = Analytics3()

    def get(self):
        result = self.a3.execute_ii()
        return jsonify(result)
