from flask import jsonify
from flask.views import MethodView
from QueryController.analytics2 import Analytics2

class Analytics2_i_API(MethodView):
    def __init__(self):
        self.a2 = Analytics2()

    def get(self):
        result = self.a2.execute_i()
        return jsonify(result)



class Analytics2_ii_API(MethodView):
    def __init__(self):
        self.a2 = Analytics2()

    def get(self):
        result = self.a2.execute_ii()
        return jsonify(result)
