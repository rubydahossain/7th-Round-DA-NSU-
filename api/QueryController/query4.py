from DBconnection.dbconf import PostgresConnection
import pandas as pd

#Get Total sales in 2015

class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute4(self):
        con=self.con
        cur=con.cursor()
        sql_query4="""SELECT t.year, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                GROUP BY CUBE(t.year) 
                ORDER BY t.year"""
        cur.execute(sql_query4)
        result4 = cur.fetchall()
        df4 = pd.DataFrame(result4, columns=['year', 'total_sales_price'])
        df4['total_sales_price'] = df4['total_sales_price'].astype('float64')
        df4 = df4.dropna()
        df4=df4.query("year==2015")
        return df4.to_dict(orient='records')


if __name__ == '__main__':
    query4=Query4()
    data=query4.execute4()
    print(data)
