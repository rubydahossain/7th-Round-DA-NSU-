from flask import jsonify
from flask.views import MethodView
from QueryController.analytics4 import Analytics4

class Analytics4_i_API(MethodView):
    def __init__(self):
        self.a4 = Analytics4()

    def get(self):
        result = self.a4.execute_i()
        return jsonify(result)



class Analytics4_ii_API(MethodView):
    def __init__(self):
        self.a4 = Analytics4()

    def get(self):
        result = self.a4.execute_ii()
        return jsonify(result)
