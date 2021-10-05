class Display_kpis:
    def desplay_kpis(df1):
        import pandas as pd
        from datetime import datetime, timedelta
        from matplotlib import pyplot as plt
        from matplotlib import dates as mpl_dates
        import matplotlib.dates as mdates
        import mplcursors
        
        from Collect_data_from_db import Collect_data_from_db as db_rq
        
        df1 = db_rq.collect_data_from_db(users,from_date)

        disp_clos=db_rq.disp_kpis()
        
        x_time='CREATE_DATE'

        df1[x_time] = pd.to_datetime(df1[x_time])
        df1.sort_values(x_time, inplace=True)
        app_name = list(dict.fromkeys(df1['APP_NAME']))
        #['PCC_serverB-serverA', 'PCC_serverC-serverA', 'DCC-serverA', 'CC-serverA']
        n_kpi=len(disp_clos)
        #n_s=len(service_names)
        p=1
        #plt.figure(figsize=(11, 2*n_kpi))
        i=1
        for n in disp_clos:
            if i%2:
                plt.figure(figsize=(10, 2.5*2))
                axs = plt.subplot(2,  1,  1)
            else:
                axs = plt.subplot(2,  1,  2)
                
            #axs = plt.subplot(n_kpi,  1,  i)   
            serv_print=''
            for app in app_name:
                service_names = list(dict.fromkeys( df1[df1['APP_NAME']==app]['SERV_NAME']))
                for serv in service_names:
                    yy=pd.to_numeric(df1[(df1['SERV_NAME']==serv) & (df1['APP_NAME']==app)][n])
                    xx=df1[(df1['SERV_NAME']==serv) & (df1['APP_NAME']==app)][x_time]                                    
                    plt.plot(xx,yy, label=app+" "+serv)
                    mplcursors.cursor(multiple=False, highlight=False, hover=False)
                plt.legend(loc = "upper left", prop={'size': 6})        
            axs.set_title(n, size=8)
            #plt.gcf().autofmt_xdate(rotation=10)
            plt.xticks(rotation=10)
            plt.gca().xaxis.set_major_formatter(mpl_dates.DateFormatter('%m/%d %H:%M:%M'))
            plt.xticks(fontsize=7)
            plt.yticks(fontsize=7)
            axs.xaxis.set_minor_locator(mdates.HourLocator())
            plt.tight_layout()   
            i=i+1
         
            
        plt.tight_layout()
        plt.show()