from DBconnection.dbconf import PostgresConnection
import pandas as pd

#Get the products that have been sold since X days?

class Query7:
    def __init__(self,days):
        self.con = PostgresConnection().getConnection()
        self.days=days
        print("Constructor called")


    '''def execute7(self):
        con=self.con
        cur=con.cursor()
        sql_query7=f"""  SELECT i.item_name, t.t_date
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key 
                WHERE t.t_date>(CURRENT_DATE - integer'{self.days}') """
        cur.execute(sql_query7)
        result7 = cur.fetchall()
        df7 = pd.DataFrame(result7, columns=['item_name', 'date'])
        df7 = df7.dropna()
        return df7.to_dict(orient='records')'''
    def execute7(self):
        con=self.con
        cur=con.cursor()
        sql_query7=f"""  SELECT i.item_name
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key 
                WHERE t.t_date>(CURRENT_DATE - integer'{self.days}') """
        cur.execute(sql_query7)
        result7 = cur.fetchall()
        df7 = pd.DataFrame(result7, columns=['item_name'])
        df7 = df7.dropna()
        return df7.to_dict(orient='list')


if __name__ == '__main__':
    query7=Query7(450)
    data=query7.execute7()
    print(data)




