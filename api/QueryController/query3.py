from DBconnection.dbconf import PostgresConnection
import pandas as pd

#Get Total sales in Barisal

class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute3(self):
        con=self.con
        cur=con.cursor()
        sql_query3="""SELECT s.division, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key 
                GROUP BY CUBE(s.division) 
                ORDER BY s.division"""
        cur.execute(sql_query3)
        result3 = cur.fetchall()
        df3 = pd.DataFrame(result3, columns=['division', 'total_sales_price'])
        df3['total_sales_price'] = df3['total_sales_price'].astype('float64')
        df3 = df3.dropna()
        df3=df3.query("division=='Barishal'")
        return df3.to_dict(orient='records')


if __name__ == '__main__':
    query3=Query3()
    data=query3.execute3()
    print(data)




