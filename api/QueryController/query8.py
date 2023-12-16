from DBconnection.dbconf import PostgresConnection
import pandas as pd

# Get the season(quarter)that is the worst for each product item


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute8(self):
        con=self.con
        cur=con.cursor()
        sql_query8="""  SELECT i.item_name,t.quarter, SUM(f.quantity)
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                GROUP BY CUBE(i.item_name,t.quarter)  
                ORDER BY i.item_name   """
        cur.execute(sql_query8)
        result8 = cur.fetchall()
        df8 = pd.DataFrame(result8, columns=['item', 'quarter', 'quantity'])
        df8 = df8.dropna()
        df8=df8.sort_values(['quantity'], ascending=True).groupby('item').head(1)
        df8=df8. drop('quantity', axis=1)
        return df8.to_dict(orient='records')


if __name__ == '__main__':
    query8=Query8()
    data=query8.execute8()
    print(data)




