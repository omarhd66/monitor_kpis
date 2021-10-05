# monitor_kpis

# This code diplay nicely KPI graphs

The kpis are collected remotly from oracle database and stored in a dataframe

there are 22 kpi to display

in this exemple there are two type of servers, serverA and serverB. there are two servers for the fist type, serverA1 and serverA2, and tree servers of the second type, serverB1, serverB2 and serverB3. for each server there are a number of services, for exemple serverA1 have 3 services (serverC-serverA, omar-serverA and hd-serverA) so for this server tree type of services will be displayed for each kpi. we have 22 kpi which means 22*3 coupres for this server will be ploted by the script

the script dosn't have a hardcoded services, it dosn't know in advance how many service a server have, it looks by itseft for this info on the colum SERV_NAME and then for each service and for each kpi plot a graph

# the table below shows the dependencies


![image](https://user-images.githubusercontent.com/30199904/136044609-c150ef91-d9ff-4e4e-aacb-6c268c2d5835.png)


You can diplay all KPIs for all server by calling Diplay_kpis() function like this:

  %matplotlib notebook

  from Display_kpis import Display_kpis as kpis

  kpis.desplay_kpis(['serverA','serverB'],'2021-10-03 00:00:00')


![image](https://user-images.githubusercontent.com/30199904/136042412-80465809-754e-42c2-a0f5-cf1c6904d9c8.png)

if you are interested only by one server type :

  kpis.desplay_kpis(['serverA'],'2021-10-03 00:00:00')

![image](https://user-images.githubusercontent.com/30199904/136050634-9c2b11c2-ab34-4498-b6f4-306aae9c3c71.png)


Or if you want only display kpi of one server, you have just to mention that on the function :

  kpis.desplay_kpis(['serverB_90'],'2021-10-03 00:00:00')

![image](https://user-images.githubusercontent.com/30199904/136051090-ffadce9e-fec4-42fd-bdf0-9ae618aafd8b.png)


You can also specify some servers you want to display, like this :

  kpis.desplay_kpis(['serverB_80', 'serverA_1'],'2021-10-03 00:00:00')

![image](https://user-images.githubusercontent.com/30199904/136050853-a28f4ea3-7b76-469c-9458-a6246dc976e7.png)

