from flask import jsonify
from flask.views import MethodView
from QueryController.analytics5 import Analytics5

class Analytics5_i_API(MethodView):
    def __init__(self):
        self.a5 = Analytics5()

    def get(self):
        result = self.a5.execute_i()
        return jsonify(result)



class Analytics5_ii_API(MethodView):
    def __init__(self):
        self.a5 = Analytics5()

    def get(self):
        result = self.a5.execute_ii()
        return jsonify(result)
