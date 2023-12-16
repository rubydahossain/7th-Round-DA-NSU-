from DBconnection.dbconf import PostgresConnection
import pandas as pd

''' 4. store and time dimensional inventory analytics.
i. Find the quantity of sales throughout 12 months in Dhaka division in 2017
ii. Compare the sales quantity of all the districts in each division in 2018 '''

class Analytics4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute_i(self):
        con = self.con
        cur = con.cursor()
        query_sql1 = """ SELECT s.division,t.month,t.year, SUM(f.quantity) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY ROLLUP(s.division,t.month,t.year)  
                         """

        cur.execute(query_sql1)
        query_result1 = cur.fetchall()
        dframe1 = pd.DataFrame(query_result1, columns=['division', 'month', 'year', 'quantity'])
        dframe1 = dframe1.dropna()
        dframe1['year'] = dframe1['year'].astype(int)
        dframe1 = dframe1.query("division== 'Dhaka' and year==2017")
        dframe1 = dframe1.sort_values('month', ascending=True)
        return dframe1.to_dict(orient='records')

    def execute_ii(self):
        con = self.con
        cur = con.cursor()
        query_sql3 = """ SELECT s.district,s.division,t.year, SUM(f.quantity) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY ROLLUP(s.district,s.division,t.year) 
                        ORDER BY s.division
                         """

        cur.execute(query_sql3)
        query_result3 = cur.fetchall()
        dframe3 = pd.DataFrame(query_result3, columns=['district', 'division', 'year', 'quantity'])
        dframe3 = dframe3.dropna()
        dframe3['year'] = dframe3['year'].astype(int)
        dframe3 = dframe3.query("year== 2018")
        return dframe3.to_dict(orient='records')


if __name__ == '__main__':
    analytics4=Analytics4()
    datai=analytics4.execute_i()
    dataii = analytics4.execute_ii()
    print(dataii)

