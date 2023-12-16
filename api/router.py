from flask import Blueprint

from QueryServices.query1service import Query1DivisionAPI
from QueryServices.query1service import Query1DistrictAPI
from QueryServices.query1service import Query1YearAPI
from QueryServices.query1service import Query1MonthAPI

from QueryServices.query2service import Query2API
from QueryServices.query3service import Query3API
from QueryServices.query4service import Query4API
from QueryServices.query5service import Query5API
from QueryServices.query6service import Query6API
from QueryServices.query7service import Query7API
from QueryServices.query8service import Query8API
from QueryServices.query9service import Query9API
from QueryServices.query10service import Query10API


from QueryServices.analytics1service import Analytics1_i_API
from QueryServices.analytics1service import Analytics1_ii_API

from QueryServices.analytics2service import Analytics2_i_API
from QueryServices.analytics2service import Analytics2_ii_API

from QueryServices.analytics3service import Analytics3_i_API
from QueryServices.analytics3service import Analytics3_ii_API

from QueryServices.analytics4service import Analytics4_i_API
from QueryServices.analytics4service import Analytics4_ii_API

from QueryServices.analytics5service import Analytics5_i_API
from QueryServices.analytics5service import Analytics5_ii_API


query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/query1/division', view_func=Query1DivisionAPI.as_view("Division wise total sales"))
query_api.add_url_rule('/query1/district', view_func=Query1DistrictAPI.as_view("District wise total sales"))
query_api.add_url_rule('/query1/year', view_func=Query1YearAPI.as_view("Year wise total sales"))
query_api.add_url_rule('/query1/month', view_func=Query1MonthAPI.as_view("Month wise total sales"))

query_api.add_url_rule('/query2', view_func=Query2API.as_view("Transaction type wise total sales"))
query_api.add_url_rule('/query3', view_func=Query3API.as_view("Total sales in Barisal"))
query_api.add_url_rule('/query4', view_func=Query4API.as_view("Total sales in 2015"))
query_api.add_url_rule('/query5', view_func=Query5API.as_view("Total sales of Barisal in 2015"))
query_api.add_url_rule('/query6', view_func=Query6API.as_view("The top three products most often purchased from each store"))
query_api.add_url_rule('/query7', view_func=Query7API.as_view("Products sold since X days"))
query_api.add_url_rule('/query8', view_func=Query8API.as_view("The quarter that is the worst for each product item"))
query_api.add_url_rule('/query9', view_func=Query9API.as_view("Total sales of items geographically (division-wise)"))
query_api.add_url_rule('/query10', view_func=Query10API.as_view("Average sales of products sales per store monthly"))


query_api.add_url_rule('/analytics1/parti', view_func= Analytics1_i_API.as_view("Total sales of different store sizes in Dhaka, April, 2016"))
query_api.add_url_rule('/analytics1/partii', view_func= Analytics1_ii_API.as_view("Total sales comparison between large sized stores in all divisions in May, 2019"))

query_api.add_url_rule('/analytics2/parti', view_func= Analytics2_i_API.as_view("Total sales of each customer in 2021"))
query_api.add_url_rule('/analytics2/partii', view_func= Analytics2_ii_API.as_view("Total sales of customers from Chittagong division in Q4, 2014"))

query_api.add_url_rule('/analytics3/parti', view_func= Analytics3_i_API.as_view("Total sales of each item in Q1 of 2015"))
query_api.add_url_rule('/analytics3/partii', view_func= Analytics3_ii_API.as_view("Total sales of items most sold in all months of 2017"))

query_api.add_url_rule('/analytics4/parti', view_func= Analytics4_i_API.as_view("Quantity of sales throughout 12 months in Dhaka division in 2017"))
query_api.add_url_rule('/analytics4/partii', view_func= Analytics4_ii_API.as_view("Sales quantity of all the districts in each division in 2018"))

query_api.add_url_rule('/analytics5/parti', view_func= Analytics5_i_API.as_view("Quantity of the 5 best selling items in Q2 of 2015"))
query_api.add_url_rule('/analytics5/partii', view_func= Analytics5_ii_API.as_view("Most popular items sold in all years"))


