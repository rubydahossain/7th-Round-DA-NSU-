from DBconnection.dbconf import PostgresConnection
import pandas as pd

'''2. customer and time dimensional financial analytics.
i. Find the total sales of each customer in 2021

ii. Find the total sales of customers from Chittagong division in Q4 of 2014'''

class Analytics2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute_i(self):
        con = self.con
        cur = con.cursor()
        sql_query5 = """ SELECT c.name,t.year, SUM(f.total_price) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.customer_dim c on c.customer_key=f.customer_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(c.name,t.year)  
                        ORDER BY c.name
                         """

        cur.execute(sql_query5)
        result5 = cur.fetchall()
        table5 = pd.DataFrame(result5, columns=['customer_name', 'year', 'total_sales_price'])
        table5 = table5.dropna()
        table5['year'] = table5['year'].astype(int)
        table5['total_sales_price'] = table5['total_sales_price'].astype('float64')
        table5 = table5.query("year==2021")
        return table5.to_dict(orient='records')

    def execute_ii(self):
        con = self.con
        cur = con.cursor()
        sql_query7 = """ SELECT c.name,c.division,t.quarter,t.year, SUM(f.total_price) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.customer_dim c on c.customer_key=f.customer_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(c.name,c,division,t.quarter,t.year)  
                        ORDER BY c.name
                         """

        cur.execute(sql_query7)
        result7 = cur.fetchall()
        table7 = pd.DataFrame(result7, columns=['customer_name', 'division', 'quarter', 'year', 'total_sales_price'])
        table7 = table7.dropna()
        table7['year'] = table7['year'].astype(int)
        table7['total_sales_price'] = table7['total_sales_price'].astype('float64')
        table7 = table7.query("division=='Chittagong' and quarter=='Q4' and year==2014")
        return table7.to_dict(orient='records')




if __name__ == '__main__':
    analytics2=Analytics2()
    datai=analytics2.execute_i()
    dataii = analytics2.execute_ii()
    print(dataii)

