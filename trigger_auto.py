# Authored by - Nitin Nahal

from doctest import OutputChecker
from time import sleep
from rest_dcd import DCDAPI
import subprocess

try:

    # CREATE A DB
    # Create a new Object
    api_rep = DCDAPI()

    # Create a Data Center
    dataCenterId = api_rep.createDataCenter("DevOps Autotest")

    # If Data Center Created, proceed
    if dataCenterId != None:
        print("Data Center Created - " + str(dataCenterId))
    else:
        print("Data Center not created")
        exit()

    # CREATE A LAN
    lanId = api_rep.createDataCenterServerLAN(dataCenterId, "LAN")
    sleep(10)

    # If Data Center Created, proceed
    if lanId == None:
        print("LAN Not Created")
        exit()
    else:
        print("LAN Created - " + str(lanId))

    server_specs = {"DB" : "", "WEB" : ""}
    print("Going to created servers ... this will take a little while...")

    for every in server_specs.keys():

        volumeId = api_rep.createDataCenterVolume(dataCenterId, every)
        sleep(10)

        if volumeId == None:
            print("Volume Not Created")
            exit()

        serverId = api_rep.createDataCenterServer(dataCenterId, every, str(volumeId))
        sleep(120)

        if serverId == None:
            print("Server Not Created")
            exit()       

        nicId = api_rep.createDataCenterServerNIC(dataCenterId, serverId, every, lanId)
        sleep(20)

        if nicId == None:
            print("NIC Not Created")
            exit()       

        api_rep.startServer(dataCenterId, serverId, valueNotRequired = True)
        sleep(20)
        JWT_token = api_rep.getJWT(dataCenterId, serverId)
        sleep(20)
        url = api_rep.getRemoteConsole(dataCenterId, serverId, JWT_token)    

        if JWT_token == None or url == None:
            print("Unable to retrieve Console")
            exit()
    
    print("Servers Created")
    print("Going to fetch Ip details")
    server_details = api_rep.getDataCenterServersList(dataCenterId)

    for every in server_details["items"]:
        this_resource = str(every["properties"]["name"])
        server_specs[this_resource] = every["entities"]["nics"]["items"][0]["properties"]["ips"][0]

    print("Server Details")
    print(server_specs)

    #server_specs = {'DB': '85.215.210.164', 'WEB': '85.215.243.107'}
    with open("hosts.ini", "w") as f:
        for key, values in server_specs.items():
            newEntry = str(key)  + "    ansible_host=" + str(values) + "\n"
            f.write(newEntry)

    print("Hosts file created\n\n")

    response_user = input("Going to start with Software Load in DB and Web, please press y/Y to continue : ")
    if response_user == 'y' or response_user == 'Y':
        
        print("\nGoing to create DB ...")
        cmd_DB = ["ansible-playbook", "-i", "hosts.ini", "-k", "-u", "root","-l", "DB", "trigger_DB.yml"]
        process = subprocess.Popen(cmd_DB, stdout=subprocess.PIPE)
        while True:
            output_DB = str(process.stdout.readline(), encoding="utf-8")
            if process.poll() is not None:
                break
            else:
                print(output_DB)

        print("\nGoing to create WEB ...")
        cmd_DB = ["ansible-playbook", "-i", "hosts.ini", "-k", "-u", "root","-l", "WEB", "trigger_WEB.yml"]
        process = subprocess.Popen(cmd_DB, stdout=subprocess.PIPE)
        while True:
            output_DB = str(process.stdout.readline(), encoding="utf-8")
            if process.poll() is not None:
                break
            else:
                print(output_DB)

    else:
        print("Invalid input. Aborting ...")
        exit()

    print("Please verify above logs\n")
    print("Your new website is at  : http://" + str(server_specs["WEB"]) + ":8080/\t Please check.")
    response_user = input("Process Complete ! Once you verify above please press y/Y to continue to delete this datacenter : ")
    if response_user == 'y' or response_user == 'Y':
        api_rep.deleteDataCenter(dataCenterId)
        sleep(80)
        print("Process complete. Thanks for running this automation")
    else:
        print("Invalid input, Datacenter not deleted, Aborting ...")
        exit()


except Exception as trigger_auto_e:
    print("trigger_auto_e : " + str(trigger_auto_e))