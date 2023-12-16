from DBconnection.dbconf import PostgresConnection
import pandas as pd

#Get the top three products that are most often purchased each store(or item supplier)


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute6(self):
        con=self.con
        cur=con.cursor()
        sql_query6="""  SELECT s.store_key, f.item_key, SUM(f.quantity)
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                GROUP BY CUBE(s.store_key,f.item_key)  
                ORDER BY s.store_key    """
        cur.execute(sql_query6)
        result6 = cur.fetchall()
        df6 = pd.DataFrame(result6, columns=['store_key', 'item_key', 'quantity'])
        df6 = df6.dropna()
        df6=df6.sort_values(['store_key', 'quantity'], ascending=[True,False]).groupby('store_key').head(3)
        return df6.to_dict(orient='records')


if __name__ == '__main__':
    query6=Query6()
    data=query6.execute6()
    print(data)




