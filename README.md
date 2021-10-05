# monitor_kpis
pis
This code diplay nicely kpis graphs

The kpis are collected remotly from oracle database and stored in a dataframe

there are 22 kpi to display

in this exemple there are two type of servers, serverA and serverB. there are two servers for the fist type, serverA1 and serverA2, and tree servers of the second type, serverB1, serverB2 and serverB3. for each server there are a number of services, for exemple serverA1 have 3 services (serverC-serverA, omar-serverA and hd-serverA) so for this server tree type of services will be displayed for each kpi. we have 22 kpi which means 22*3 coupres for this server will be ploted the script

the script dosn't have a hardcoded services, it dosn't know in advance how many service a server have, it looks itseft for this info on the colum SERV_NAME and then for each service and for each kpi plot a graph

the table below shows the dependencies


![image](https://user-images.githubusercontent.com/30199904/136043934-80cac9c3-dffc-4555-9b1c-9c741cc6841a.png)

![image](https://user-images.githubusercontent.com/30199904/136042333-26b26a36-649b-4fe7-a78a-da848b18a6d8.png)

![image](https://user-images.githubusercontent.com/30199904/136042412-80465809-754e-42c2-a0f5-cf1c6904d9c8.png)

![image](https://user-images.githubusercontent.com/30199904/136042474-4fe93541-056a-4c3c-9fe6-240284c0a6a0.png)

