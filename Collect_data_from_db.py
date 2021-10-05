class  Collect_data_from_db:
    def collect_data_from_db(users,from_date):
        import pandas as pd
        import cx_Oracle   
        
        disp_server=Collect_data_from_db.app_names(users)
        
        # Test to see if the cx_Oracle is recognized
        print(cx_Oracle.version)   # 

        cx_Oracle.clientversion()  

        conn = cx_Oracle.connect('user/password@tnsname')

        if len(disp_server) < 2 :
            try:
                query = f"select e.app_name, e.username,  k.* from kpi_table k, app_env e where k.app_env_id=e.app_env_id and e.app_name='{disp_server[0]}' and k.create_date>to_date('{from_date}', 'YYYY-MM-DD HH24:MI:SS')"
                df1 = pd.read_sql(con = conn, sql = query)
            finally:
                conn.close()
        else:
            try:
                query = f"select e.app_name, e.username,  k.* from kpi_table k, app_env e where k.app_env_id=e.app_env_id and e.app_name in {disp_server} and k.create_date>to_date('{from_date}', 'YYYY-MM-DD HH24:MI:SS')"
                df1 = pd.read_sql(con = conn, sql = query)
            finally:
                conn.close()

        return df1
     
    def disp_kpis():
        #kpi to be ploted
        disp_kpis=['kpi1', 'kpi2', 'kpi3', 'kpi4', 'kpi5', 'kpi6', 'kpi7', 'kpi8', 'kpi9', 'kpi10', 'kpi11', 'kpi12', 'kpi13',
       'kpi14', 'kpi15', 'kpi16', 'kpi17', 'kpi18', 'kpi19', 'kpi20', 'kpi21', 'kpi22']
        return disp_kpis
    
    def app_names(APP_NAMES):
        app_name=['serverA_1', 'serverA_2', 'serverB_70', 'serverB_80','serverB_90']
        app=[]
        for a in APP_NAMES:        
            match = [s for s in app_name if a in s]
            for m in match:
                app.append(m)
        return tuple(app)