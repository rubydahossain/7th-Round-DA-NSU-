from DBconnection.dbconf import PostgresConnection
import pandas as pd
# Get the average sales of products sales per store monthly
class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    '''def execute10(self):
        con=self.con
        cur=con.cursor()
        sql_query10="""SELECT i.item_name, t.month,  AVG(f.total_price)
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                GROUP BY CUBE(i.item_name,t.month)  
                ORDER BY i.item_name """
        cur.execute(sql_query10)
        result10 = cur.fetchall()
        df10 = pd.DataFrame(result10, columns=['item','month','average_sales_price'])
        df10 = df10.dropna()
        df10['average_sales_price']=df10['average_sales_price'].astype('float64')
        df10 = df10.sort_values(['item', 'month'], ascending=[True, True])
        return df10.to_dict(orient='records')'''

    def execute10(self):
        con=self.con
        cur=con.cursor()
        sql_query10=""" SELECT s.store_key, t.month,  AVG(f.total_price)
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                GROUP BY CUBE(s.store_key,t.month)  
                ORDER BY s.store_key """
        cur.execute(sql_query10)
        result10 = cur.fetchall()
        df10 = pd.DataFrame(result10, columns=['store_key','month','average_sales_price'])
        df10 = df10.dropna()
        df10['average_sales_price']=df10['average_sales_price'].astype('float64')
        df10 = df10.sort_values(['store_key', 'month'], ascending=[True,True])
        return df10.to_dict(orient='records')


if __name__ == '__main__':
    query10=Query10()
    data=query10.execute10()
    print(data)




