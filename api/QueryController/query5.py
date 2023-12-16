from DBconnection.dbconf import PostgresConnection
import pandas as pd

#	Get Total sales of Barisal in 2015

class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute5(self):
        con=self.con
        cur=con.cursor()
        sql_query5="""SELECT s.division,t.year, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                GROUP BY ROLLUP(s.division,t.year) """
        cur.execute(sql_query5)
        result5 = cur.fetchall()
        df5 = pd.DataFrame(result5, columns=['division', 'year', 'total_sales_price'])
        df5['total_sales_price'] = df5['total_sales_price'].astype('float64')
        df5 = df5.dropna()
        df5 = df5.query("division== 'Barishal' and year==2015")
        return df5.to_dict(orient='records')


if __name__ == '__main__':
    query5=Query5()
    data=query5.execute5()
    print(data)
