from DBconnection.dbconf import PostgresConnection
import pandas as pd
# Get the total sales of items geographically (division-wise)
class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute9(self):
        con=self.con
        cur=con.cursor()
        sql_query9=""" SELECT i.item_name, s.division, SUM(f.total_price)
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key
                GROUP BY CUBE(i.item_name,s.division)  
                ORDER BY i.item_name """
        cur.execute(sql_query9)
        result9 = cur.fetchall()
        df9 = pd.DataFrame(result9, columns=['item', 'division', 'total_sales'])
        df9 = df9.dropna()
        df9['total_sales']=df9['total_sales'].astype('float64')
        #df9=df9.sort_values(['item'], ascending=True).groupby('division').aggregate({'total_sales':'sum'})
        return df9.to_dict(orient='records')


if __name__ == '__main__':
    query9=Query9()
    data=query9.execute9()
    print(data)




