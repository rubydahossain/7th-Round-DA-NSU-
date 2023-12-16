from DBconnection.dbconf import PostgresConnection
import pandas as pd

#Get division/district/year/month wise total sales

class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute_division(self):
        con=self.con
        cur=con.cursor()
        sql_query="""SELECT s.division, SUM(f.total_price) 
                      FROM ecomdb_star_schema.fact_table f 
                      JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key 
                      GROUP BY CUBE(s.division) 
                      ORDER BY s.division"""
        cur.execute(sql_query)
        result = cur.fetchall()
        df = pd.DataFrame(result, columns=['division', 'total_sales_price'])
        df['total_sales_price'] = df['total_sales_price'].astype('float64')
        df = df.dropna()
        return df.to_dict(orient='records')

    def execute_district(self):
        con=self.con
        cur=con.cursor()
        sql_query="""SELECT s.district, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key 
                GROUP BY CUBE(s.district) 
                ORDER BY s.district"""
        cur.execute(sql_query)
        result = cur.fetchall()
        df = pd.DataFrame(result, columns=['district', 'total_sales_price'])
        df['total_sales_price'] = df['total_sales_price'].astype('float64')
        df = df.dropna()
        return df.to_dict(orient='records')

    def execute_year(self):
        con=self.con
        cur=con.cursor()
        sql_query=""" SELECT t.year, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key 
                GROUP BY ROLLUP(t.year) 
                ORDER BY t.year """
        cur.execute(sql_query)
        result = cur.fetchall()
        df = pd.DataFrame(result, columns=['year', 'total_sales_price'])
        df['total_sales_price'] = df['total_sales_price'].astype('float64')
        df = df.dropna()
        return df.to_dict(orient='records')

    def execute_month(self):
        con=self.con
        cur=con.cursor()
        sql_query=""" SELECT t.month, SUM(f.total_price) 
                FROM ecomdb_star_schema.fact_table f 
                JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key 
                GROUP BY CUBE(t.month) 
                ORDER BY t.month """
        cur.execute(sql_query)
        result = cur.fetchall()
        df = pd.DataFrame(result, columns=['month', 'total_sales_price'])
        df['total_sales_price'] = df['total_sales_price'].astype('float64')
        df = df.dropna()
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query1=Query1()
    data1=query1.execute_division()
    data2 = query1.execute_district()
    data3 = query1.execute_year()
    data4 = query1.execute_month()
    print(data4)





