from DBconnection.dbconf import PostgresConnection
import pandas as pd

#Get transaction(cash/mobile/card) wise total sales

class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute2(self):
        con=self.con
        cur=con.cursor()
        sql_query2="""SELECT t.trans_type, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.trans_dim t on t.payment_key=f.payment_key 
                GROUP BY CUBE(t.trans_type) 
                ORDER BY t.trans_type"""
        cur.execute(sql_query2)
        result2 = cur.fetchall()
        df2 = pd.DataFrame(result2, columns=['trans_type', 'total_sales_price'])
        df2['total_sales_price'] = df2['total_sales_price'].astype('float64')
        df2 = df2.dropna()
        return df2.to_dict(orient='records')


if __name__ == '__main__':
    query2=Query2()
    data=query2.execute2()
    print(data)




