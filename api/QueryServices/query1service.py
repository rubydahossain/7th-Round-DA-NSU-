from flask import jsonify
from flask.views import MethodView
from QueryController.query1 import Query1

class Query1DivisionAPI(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute_division()
        return jsonify(result)

class Query1DistrictAPI(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute_district()
        return jsonify(result)

class Query1YearAPI(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute_year()
        return jsonify(result)

class Query1MonthAPI(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute_month()
        return jsonify(result)