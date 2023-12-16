from DBconnection.dbconf import PostgresConnection
import pandas as pd

'''1. store and time dimensional financial analytics.
i. Compare the total sales between all store sizes in Dhaka in April, 2016
ii. Compare the total sales between large sized stores in all divisions in May, 2019'''

class Analytics1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute_i(self):
        con = self.con
        cur = con.cursor()
        sql_query2 = """ SELECT s.division,s.store_size,t.month,t.year, SUM(f.total_price) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(s.division,s.store_size,t.month,t.year)  
                        ORDER BY s.division, s.store_size
                         """

        cur.execute(sql_query2)
        result2 = cur.fetchall()
        table2 = pd.DataFrame(result2, columns=['division', 'store_size', 'month', 'year', 'total_sales_price'])
        table2 = table2.dropna()
        table2['year'] = table2['year'].astype(int)
        table2['total_sales_price'] = table2['total_sales_price'].astype('float64')
        table2 = table2.query("division=='Dhaka' and month==4 and year==2016")
        return table2.to_dict(orient='records')

    def execute_ii(self):
        con = self.con
        cur = con.cursor()
        sql_query4 = """ SELECT s.division,s.store_size,t.month,t.year, SUM(f.total_price) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(s.division,s.store_size,t.month,t.year)  
                        ORDER BY s.division
                         """

        cur.execute(sql_query4)
        result4 = cur.fetchall()
        table4 = pd.DataFrame(result4, columns=['division', 'store_size', 'month', 'year', 'total_sales_price'])
        table4 = table4.dropna()
        table4['year'] = table4['year'].astype(int)
        table4['total_sales_price'] = table4['total_sales_price'].astype('float64')
        table4 = table4.query("month==5 and year==2019")
        table4 = table4.query("store_size=='high'")
        return table4.to_dict(orient='records')




if __name__ == '__main__':
    analytics1=Analytics1()
    datai=analytics1.execute_i()
    dataii = analytics1.execute_ii()
    print(dataii)

