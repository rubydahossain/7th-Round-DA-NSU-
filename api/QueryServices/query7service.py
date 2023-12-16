from flask import jsonify,request
from flask.views import MethodView
from QueryController.query7 import Query7

class Query7API(MethodView):
    def get(self):
        return jsonify({"message":"Call post method with input value 'days'"})

    def post(self):
        days = request.json['days']
        self.q7= Query7(days)
        result = self.q7.execute7()
        return jsonify(result)

if __name__ == '__main__':
    query7=Query7(450)
    data=query7.execute7()
    print(data)

