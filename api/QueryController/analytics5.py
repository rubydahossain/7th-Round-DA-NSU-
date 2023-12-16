from DBconnection.dbconf import PostgresConnection
import pandas as pd

''' 5. item and time dimensional inventory analytics.
i. Find the the quantity of the 5 best selling items in Q2 of 2015
ii. Find the most popular items sold in all years '''

class Analytics5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute_i(self):
        con = self.con
        cur = con.cursor()
        query_sql4 = """ SELECT i.item_name,t.quarter,t.year, SUM(f.quantity) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(i.item_name,t.quarter,t.year)  
                        ORDER BY i.item_name
                         """

        cur.execute(query_sql4)
        query_result4 = cur.fetchall()
        dframe4 = pd.DataFrame(query_result4, columns=['item_name', 'quarter', 'year', 'quantity'])
        dframe4 = dframe4.dropna()
        dframe4['year'] = dframe4['year'].astype(int)
        dframe4 = dframe4.query("quarter== 'Q2' and year==2015")

        dframe4 = dframe4.sort_values('quantity', ascending=False).head(5)
        return dframe4.to_dict(orient='records')

    def execute_ii(self):
        con = self.con
        cur = con.cursor()
        query_sql5 = """ SELECT i.item_name,t.year, SUM(f.quantity) 
                        FROM ecomdb_star_schema.fact_table f 
                        JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key
                        JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key
                        GROUP BY CUBE(i.item_name,t.year)  
                        ORDER BY i.item_name
                         """

        cur.execute(query_sql5)
        query_result5 = cur.fetchall()
        dframe5 = pd.DataFrame(query_result5, columns=['item_name', 'year', 'quantity'])
        dframe5 = dframe5.dropna()
        dframe5['year'] = dframe5['year'].astype(int)

        dframe5 = dframe5.sort_values(['year', 'quantity'], ascending=[True, False]).groupby('year').head(1)
        return dframe5.to_dict(orient='records')


if __name__ == '__main__':
    analytics5=Analytics5()
    datai=analytics5.execute_i()
    dataii = analytics5.execute_ii()
    print(dataii)

