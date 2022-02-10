# **IONOS Project**
<br/>

---

## **Table of contents**
---
- Infra Preparation - IONOS DCD
- Task 1 - Create a Python Script (Cuboid)
- Task 2 - Web App
- Task 3 - Automating Task 1 and Task 2
- Tech Stack
- Summary
---
## **Infra Preparation - IONOS DCD**
---
- Data Centre Name : **DevOps Tasks**
- There are 3 VMs in this DC :
  
  1. Deployment (Core - 2, RAM - 2GB, HDD - 10GB, OS - Debian 9)
  2. DB (Core - 2, RAM - 4GB, HDD - 10GB, OS - Debian 9)
  3. Web (Core - 1, RAM - 2GB, HDD - 10GB, OS - Debian 9)
   
<br/>

- All three VMs are connected to LAN with public Internet, LAN ID is 2.
- IP Addresses : 

  1. Deployment - 185.56.151.28
  2. DB - 85.215.219.61
  3. Web - 85.215.209.204

<br/>

- All VMs are having SSH public keys for Elmar and Thomas. They were previosuly present at the time of creating the VM (so I didnot override them, incase you are not able to access, please let me know)
- All Code base is also present on deployment server i.e. Deployment - 185.56.151.28
- Kindly see below specifications for Code, Repo link - https://github.com/NitinNahal/ionos_assignment.git , Based on task there are three different branches on repo : 
  
    1. Task 1 Code - /root/ionos_assignment_task_1 (Repo branch - **feature/task_1**)
    2. Task 2 Code - /root/ionos_assignment_task_2 (Repo branch - **feature/task_2**)
    3. Task 3 Code - /root/ionos_assignment_task_3 (Repo branch - **feature/task_3**)

<br/>

- We will discuss more on individual code, in specific sections.
---
## **Task 1**
---
- Repo branch - **feature/task_1**
- Code - /root/ionos_assignment_task_1/**utils.py**
- Trigger - python3 utils.py
- Sample run (Test Cases):
  
  ```
  root@debian:~/ionos_assignment_task_1# python3 utils.py
  Starting .....
  Please provide following inputs, assuming all values are in same units.
  Surface Area is Total Surface area
  Enter the value of edge a : 1
  Enter the value of edge b : 2
  Enter the value of edge c : 3
  Volume - 6.0
  Surface Area - 22.0
  Perimeter - 6.0  

  root@debian:~/ionos_assignment_task_1# python3 utils.py
  Starting .....
  Please provide following inputs, assuming all values are in same units.
  Surface Area is Total Surface area
  Enter the value of edge a : 0
  Enter the value of edge b : 2
  Enter the value of edge c : 3
  Exception in taking input - Value of Edge cannot be < 1
  Volume -
  Surface Area -
  Perimeter -

  root@debian:~/ionos_assignment_task_1# python3 utils.py
  Starting .....
  Please provide following inputs, assuming all values are in same units.
  Surface Area is Total Surface area
  Enter the value of edge a : nitin
  Exception in taking input - could not convert string to float: 'nitin'
  Volume -
  Surface Area -
  Perimeter -

  root@debian:~/ionos_assignment_task_1#  
  ```
- **Cuboid** is a Class which provides functionality to compute Volumne, Surface Area and Perimeter. This class has been re-used in solution of Task 2.
---
## **Task 2**
---
- Repo branch - **feature/task_2**
- Code - Deployment - 185.56.151.28 /root/ionos_assignment_task_2/*files*
- Trigger - No trigger required, web app is up and running. Follow link - http://85.215.209.204:8080/  This is a Django Application to help you perform some live calculations.
- Web App supports : 
  
    1. Calculate Volume, Surface Area, Perimeter and save results in DB.
    2. Show last 30 results of calculations from DB.
    3. This Website is token protected so, please use Web UI to test.
    
<br/>

- Sample run (Test Cases):
  
  ```
  - This is API to get the calculations :
  http://85.215.209.204:8080/upData/calculations/

  Results -

  Length : 19.0  Breadth : 20.0  Height : 21.0  Surface Area : 23980  Volume : 7980.0  Perimeter : 60.0  Date : 2022-02-08 09:15:19.098315+00:00

  Length : 3.0  Breadth : 2.0  Height : 4.0  Surface Area : 52.0  Volume : 24.0  Perimeter : 9.0  Date : 2022-02-08 08:57:49.036372+00:00

  Length : 1.0  Breadth : 4.0  Height : 3.0  Surface Area : 38.0  Volume : 12.0  Perimeter : 8.0  Date : 2022-02-05 15:43:59.053471+00:00

  Length : 1.0  Breadth : 2.0  Height : 3.0  Surface Area : 22.0  Volume : 6.0  Perimeter : 6.0  Date : 2022-02-05 15:43:47.627863+00:00

  Length : 3.0  Breadth : 4.0  Height : 5.0  Surface Area : 6.0  Volume : 7.0  Perimeter : 5.0  Date : 2022-02-05 12:52:34.808872+00:00

  Length : 1.0  Breadth : 2.0  Height : 4.0  Surface Area : 5.0  Volume : 6.0  Perimeter : 7.0  Date : 2022-02-05 12:52:23.883656+00:00

  ```

---
## **Task 3**
---
- Repo branch - **feature/task_3**
- Code - Deployment - 185.56.151.28 /root/ionos_assignment_task_3/*files*
- Trigger :

    1. Navigate to /root/ionos_assignment_task_3/
    2. python3 trigger_auto.py
  
<br/>

- Automation supports : 
  
    1. Creating a similar infrastructure with 2 VMs, DB and WEB
    2. Provisioning LAN, NIC, Volume with each VM. Composition is 4GB RAM, 4 cores, 10GB HDD per VM.
    3. LAN ID created is 1.
    4. Once VM setup is complete, you will be able to see the allocated IP address in output.
    5. After that Script will trigger :    
    
       - ansible playbook -> trigger_DB. yml to install DB related packages and softwares necessary for application in task 2 to run. You will see creation of DB, Access, database.
       - ansible playbook -> trigger_WEB.yml yo install WEB related packages and softwares necessary for application in task 2 to run. You will see Web hosting, Git code clone, start of web server.

    <br/>

    6. All Logs are visible during execution run.
    7. SSH Password when prompted is same as that of Task 2 VMs (will be sharing in seperate mail).
  
    8. In any situation if any step fails, automation aborts.
    9. Once completed, you will be able to see the new duplicate application URL where you can check results.
    10. At the end user will be prompted  - "". Make sure you have viewed the application url which is shown as this will clean this datacentre and its related resources.
    11. Automation Complete.
    

<br/>

- Sample run (Test Case):
  
  ```
  root@debian:~/ionos_assignment_task_3# python3 trigger_auto.py
  Data Center Created - 2284b05d-b91a-439c-b6d2-e64811f54934
  LAN Created - 1
  Going to created servers ... this will take a little while...
  Servers Created
  Going to fetch Ip details
  Server Details
  {'WEB': '85.215.221.30', 'DB': '85.215.249.115'}
  Hosts file created


  Going to start with Software Load in DB and Web, please press y/Y to continue : y

  Going to create DB ...
  SSH password:


  PLAY [trigger_DB] ******************************************************************



  TASK [Gathering Facts] *************************************************************

  ok: [DB]



  TASK [Installing Mysql  and dependencies] ******************************************

  changed: [DB] => (item=python3-setuptools)

  changed: [DB] => (item=python3-pip)

  changed: [DB] => (item=python3-pymysql)

  changed: [DB] => (item=python3-mysqldb)

  changed: [DB] => (item=mysql-server)

  changed: [DB] => (item=mysql-client)

  changed: [DB] => (item=default-libmysqlclient-dev)



  TASK [Check if this old version is absent PyMySQL] *********************************

  ok: [DB]



  TASK [Enable remote login to mysql] ************************************************

  changed: [DB]



  TASK [Change the authentication plugin of MySQL root user to mysql_native_password] ***

  changed: [DB]



  TASK [Flush Privileges] ************************************************************

  changed: [DB]



  TASK [Create user with password, all database privileges and 'WITH GRANT OPTION'] ***

  changed: [DB]



  TASK [Flush Privileges] ************************************************************

  changed: [DB]



  TASK [Restart mysql] ***************************************************************

  changed: [DB]



  TASK [Create DB] *******************************************************************

  changed: [DB]



  RUNNING HANDLER [Restart mysql] ****************************************************

  changed: [DB]



  PLAY RECAP *************************************************************************

  DB                         : ok=11   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0




  Going to create WEB ...
  SSH password:


  PLAY [trigger_WEB] *****************************************************************



  TASK [Gathering Facts] *************************************************************

  ok: [WEB]



  TASK [Installing  packages and dependencies] ***************************************

  changed: [WEB] => (item=python3-setuptools)

  changed: [WEB] => (item=python3-pip)

  changed: [WEB] => (item=python3-mysqldb)

  changed: [WEB] => (item=mysql-server)

  changed: [WEB] => (item=mysql-client)

  changed: [WEB] => (item=default-libmysqlclient-dev)

  changed: [WEB] => (item=supervisor)

  changed: [WEB] => (item=git)



  TASK [Install Packages related to WEB] *********************************************

  changed: [WEB]



  TASK [Download the code from the GitRepo] ******************************************

  changed: [WEB]



  TASK [Enable DB] *******************************************************************

  changed: [WEB]



  TASK [Make DB tables] **************************************************************

  changed: [WEB]



  TASK [Align DB with Web application] ***********************************************

  changed: [WEB]



  TASK [Creating a config file] ******************************************************

  changed: [WEB]



  TASK [Re read the package] *********************************************************

  changed: [WEB]



  TASK [Start the Web application] ***************************************************

  changed: [WEB]



  PLAY RECAP *************************************************************************

  WEB                        : ok=10   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0



  Please verify above logs

  Your new website is at  : http://85.215.221.30:8080/     Please check.
  Process Complete ! Once you verify above please press y/Y to continue to delete this datacenter : y
  Data Center Deleted
  Waiting for cleanup ....
  Process complete. Thanks for running this automation  
  ```

---
## **Tech Stack**
---
- Python
- Ansible
- Database - MySQL
- Web - Django
- Code Repository - Git
- OS - LINUX (Debian 9)
---
## **Summary**
---
**Thank you**, for giving this opportunity. It was a nice Automation week. Please share your feedback at *nitin.nahal14@gmail.com*