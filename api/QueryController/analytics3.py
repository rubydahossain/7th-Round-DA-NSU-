from DBconnection.dbconf import PostgresConnection
import pandas as pd

''' 3. item and time dimensional financial analytics.
i. Find the total sales of each item in Q1 of 2015

ii. Find the total sales of items most sold in all months of 2017 '''

class Analytics3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute_i(self):
        con = self.con
        cur = con.cursor()
        sql_query8 = """ SELECT i.item_name,t.quarter,t.year, SUM(f.total_price) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(i.item_name,t.quarter,t.year)  
                        ORDER BY i.item_name
                         """

        cur.execute(sql_query8)
        result8 = cur.fetchall()
        table8 = pd.DataFrame(result8, columns=['item_name', 'quarter', 'year', 'total_sales_price'])
        table8 = table8.dropna()
        table8['year'] = table8['year'].astype(int)
        table8['total_sales_price'] = table8['total_sales_price'].astype('float64')
        table8 = table8.query("quarter=='Q1' and year==2015")
        return table8.to_dict(orient='records')

    def execute_ii(self):
        con = self.con
        cur = con.cursor()
        sql_query9 = """ SELECT i.item_name,t.month,t.year, SUM(f.total_price) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(i.item_name,t.month,t.year)  
                        ORDER BY i.item_name
                         """

        cur.execute(sql_query9)
        result9 = cur.fetchall()
        table9 = pd.DataFrame(result9, columns=['item_name', 'month', 'year', 'total_sales_price'])
        table9 = table9.dropna()
        table9['year'] = table9['year'].astype(int)
        table9 = table9.query("year==2017")


        table9 = table9.sort_values(['total_sales_price'], ascending=[False]).groupby('month').head(1)
        table9 = table9.sort_values(['month'], ascending=[True])

        table9['total_sales_price'] = table9['total_sales_price'].astype('float64')
        return table9.to_dict(orient='records')




if __name__ == '__main__':
    analytics3=Analytics3()
    datai=analytics3.execute_i()
    dataii = analytics3.execute_ii()
    print(datai)

