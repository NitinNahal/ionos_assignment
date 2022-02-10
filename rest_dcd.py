# Authored by - Nitin Nahal

from time import sleep
import requests

# IONOS DCD CLASS
class DCDAPI():

    def __init__(self):

        self.url_token = "https://api.ionos.com/cloudapi/v6/?pretty=true&depth=0"

        # Below are Prod APIs, to be opened when working on Production
        self.authentication = "Basic cGxhdGZvcm0tY29tcHV0ZS1hc3Nlc3NtZW50KzNAY2xvdWQuaW9ub3MuY29tOk5leWcuZ2ltNw=="
        self.list_datacenters = "https://api.ionos.com/cloudapi/v6/datacenters?pretty=true&depth=0&offset=0&limit=1000"
        self.create_datacenter = "https://api.ionos.com/cloudapi/v6/datacenters?pretty=true&depth=0"
        self.delete_datacenter = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}?pretty=true&depth=0"
        self.list_images = "https://api.ionos.com/cloudapi/v6/images?pretty=true&depth=1"
        self.list_volume = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/volumes"        
        self.create_volume = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/volumes"
        self.delete_volume = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/volumes/{volumeId}"
        self.list_servers = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers?pretty=true&depth=4"        
        self.create_server = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers?pretty=true&depth=0"
        self.delete_server = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers/{serverId}"

        self.create_nic = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers/{serverId}/nics"
        self.create_lan = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/lans"
        self.start_server = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers/{serverId}/start"
        self.JWT = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers/{serverId}/token"
        self.getConsole = "https://api.ionos.com/cloudapi/v6/datacenters/{datacenterId}/servers/{serverId}/remoteconsole"

        self.authentic = False

    def sendRequest(self, requestType, body, url, headers, valueNotRequired = False):
        try:
            if requestType == "GET" or requestType == "POST":
                if valueNotRequired == False:
                    response = requests.request(requestType, url, headers=headers, json=body)
                else:
                    requests.request(requestType, url, headers=headers, json=body)
                    return

            elif requestType == "DELETE":
                if valueNotRequired == False:
                    response = requests.request(requestType, url, headers=headers)
                    return response.status_code
                else:
                    requests.request(requestType, url, headers=headers)
                    return
            else:
                return None, None
            return response.status_code, response.json()

        except Exception as sendRequestException:
            print("sendRequestException : " + str(sendRequestException))

    def initializeAuthentication(self):
        try:
            headers = {
            'Authorization': self.authentication,
            "X-Contract_Number" : "0",
            }
            payload = ''
            res_status, res_output = self.sendRequest("GET", payload, self.url_token ,headers)

            if res_status == 200:
                #print("Request is Authentic")
                self.authentic = True
            else:
                self.authentic = False

        except Exception as initializeAuthenticationException:
            print("initializeAuthenticationException : " + str(initializeAuthenticationException))

    def getDataCentersList(self):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                res_status, res_output = self.sendRequest("GET", {}, self.list_datacenters, headers)
                if res_status == 200:
                    print("Get Query Response OK - \n" + str(res_output))                   
                else:
                    print("Get Query Response NOK - \n" + str(res_output))
        
        except Exception as getDataCentersListException:
            print("getDataCentersListException - " + str(getDataCentersListException))

    def getDataCentersImagesList(self):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                res_status, res_output = self.sendRequest("GET", {}, self.list_images, headers)
                if res_status == 200:
                    print("Get Query Response OK - \n" + str(res_output))                   
                else:
                    print("Get Query Response NOK - \n" + str(res_output))
        
        except Exception as getDataCentersImagesListException:
            print("getDataCentersImagesListException - " + str(getDataCentersImagesListException))

    def createDataCenter(self, resource_name):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                body = {
                    # "metadata": {},
                    "properties": {
                        "name": resource_name,
                        "description": "Test Data Center",
                        "location": "de/txl",
                        "secAuthProtection": "true"
                    },
                    "entities": {
                        "servers": {
                            "_links": {}
                        },
                        "volumes": {
                            "_links": {}
                        },
                        "loadbalancers": {
                            "_links": {}
                        },
                        "lans": {
                            "_links": {}
                        },
                        "networkloadbalancers": {
                            "_links": {}
                        },
                        "natgateways": {
                            "_links": {}
                        }
                    }
                }                
                res_status, res_output = self.sendRequest("POST", body, self.create_datacenter, headers)
                if res_status == 202:
                    #print("POST Query Response OK - \n" + str(res_output))         
                    return res_output["id"]          
                else:
                    print("POST Query Response NOK - \n" + str(res_output))
                    return None
        
        except Exception as createDataCenterException:
            print("createDataCenterException - " + str(createDataCenterException))

    def deleteDataCenter(self, dataCenterId):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                # payload = {
                #     "datacenterId" : dataCenterId
                # }          

                #payload = json.dumps(payload)                             
                newUrl = self.delete_datacenter.replace("{datacenterId}", dataCenterId)
                res_status = self.sendRequest("DELETE", {}, newUrl, headers)
                if res_status == 202:
                    print("Data Center Deleted")             
                else:
                    print("POST Query Response NOK")
        
        except Exception as deleteDataCenterException:
            print("deleteDataCenterException - " + str(deleteDataCenterException))

    def getDataCentersVolumeList(self, dataCenterId):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                newUrl = self.list_volume.replace("{datacenterId}", dataCenterId)
                res_status, res_output = self.sendRequest("GET", {}, newUrl, headers)
                if res_status == 200:
                    print("Get Query Response OK - \n" + str(res_output))                   
                else:
                    print("Get Query Response NOK - \n" + str(res_output))
        
        except Exception as getDataCentersVolumeListException:
            print("getDataCentersVolumeListException - " + str(getDataCentersVolumeListException))

    def createDataCenterVolume(self, dataCenterId, volume_name):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                body = {
                    #"metadata": {},
                    "properties": {
                        "name": volume_name,
                        "type": "HDD",
                        "size": 10,
                        "availabilityZone": "AUTO",
                        
                        "image": "5ffc2504-8313-11ec-bda6-02086196891f",
                        "imagePassword": "ionos123",
                        #"imageAlias": "debian:9",
                        "sshKeys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCvWOzJMqOBfLs+e+/acokXdnjmxShcLHp00OWfFFkRnYYgWQqYQTzVV3ubhCQtmchoqDqXNWx2SNlLfQxwtpkEFUSnUAbscepJ5kFuCDF6TvoNMxonrxRk/eS31pmksgK1Y1Lju95yqlap+58nCYEue6164gmqOIsXDjXDyqVcSKI9rOBlf9Fv+8qigO3E/zVmdeyPsySmk0gxXx2AsLQQsMOuzcZcBR+vMOmH+MOh2/PjGASotbW1cBq0HQU94tSwiUOLbAhD/KLiI4ijM6/Fcyn8J6XTk1ci2RWVJZRYN7qt/GEVBmcN1W2cA9ok8xJ9THXduz0l/yCRa9i7y2U9 root@debian",
                        "bus": "VIRTIO",
                        "cpuHotPlug": "true",
                        "ramHotPlug": "true",
                        "nicHotPlug": "true",
                        "nicHotUnplug": "true",
                        "discVirtioHotPlug": "true",
                        "discVirtioHotUnplug": "true",
                        #"licenceType": "LINUX",
                        #"backupunitId": "25f67991-0f51-4efc-a8ad-ef1fb31a481c",
                        #"userData": ""
                    }
                }
                newUrl = self.create_volume.replace("{datacenterId}", dataCenterId)
                res_status, res_output = self.sendRequest("POST", body, newUrl, headers)
                if res_status == 202:
                    #print("POST Query Response OK - \n" + str(res_output))         
                    return res_output["id"]          
                else:
                    print("POST Query Response NOK - \n" + str(res_output))
                    return None

        except Exception as createDataCenterVolumeException:
            print("createDataCenterVolumeException - " + str(createDataCenterVolumeException))

    def deleteDataCenterVolume(self, dataCenterId, volumeId):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                          
                newUrl = self.delete_volume.replace("{datacenterId}", dataCenterId).replace("{volumeId}", volumeId)
                res_status = self.sendRequest("DELETE", {}, newUrl, headers)
                if res_status == 202:
                    print("POST Query Response OK")             
                else:
                    print("POST Query Response NOK")
        
        except Exception as deleteDataCenterVolumeException:
            print("deleteDataCenterVolumeException - " + str(deleteDataCenterVolumeException))

    def getDataCenterServersList(self, dataCenterId):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                newUrl = self.list_servers.replace("{datacenterId}", dataCenterId)
                res_status, res_output = self.sendRequest("GET", {}, newUrl, headers)
                if res_status == 200:
                    #print("Get Query Response OK - \n" + str(res_output))     
                    return res_output
                else:
                    print("Get Query Response NOK - \n" + str(res_output))
        
        except Exception as getDataCenterServersListException:
            print("getDataCenterServersListException - " + str(getDataCenterServersListException))

    def createDataCenterServer(self, dataCenterId, server_name, volume_id):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                body = {
                    #"metadata": {},
                    "properties": {
                        #"templateUuid": "15f67991-0f51-4efc-a8ad-ef1fb31a480c",
                        "name": server_name,
                        "cores": 4,
                        "ram": 4096,
                        "availabilityZone": "AUTO",
                        # "bootCdrom": {
                        #     "id": "1"
                        # },
                        "bootVolume": {
                            "id": volume_id
                        },
                        "cpuFamily": "INTEL_SKYLAKE",
                        "type": "ENTERPRISE"
                    },
                }
                newUrl = self.create_server.replace("{datacenterId}", dataCenterId)
                res_status, res_output = self.sendRequest("POST", body, newUrl, headers)
                if res_status == 202:
                    #print("POST Query Response OK - \n" + str(res_output))         
                    return res_output["id"]          
                else:
                    print("POST Query Response NOK - \n" + str(res_output))
                    return None
        
        except Exception as createDataCenterServerException:
            print("createDataCenterServerException - " + str(createDataCenterServerException))

    def deleteDataCenterServer(self, dataCenterId, serverId):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                          
                newUrl = self.delete_server.replace("{datacenterId}", dataCenterId).replace("{serverId}", serverId)
                res_status = self.sendRequest("DELETE", {}, newUrl, headers)
                if res_status == 202:
                    print("POST Query Response OK")       
                else:
                    print("POST Query Response NOK")
        
        except Exception as deleteDataCenterServerException:
            print("deleteDataCenterServerException - " + str(deleteDataCenterServerException))

    def createDataCenterServerNIC(self, dataCenterId, server_name, resource_name, LanId):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                body = {
                    #"metadata": {},
                    "properties": {
                        "name": resource_name,
                        #"ips": {},
                        "dhcp": "true",
                        "lan": LanId,
                        "firewallActive": "false",
                        "firewallType": "INGRESS"
                    },
                    "entities": {
                        "flowlogs": {
                            "_links": {}
                        },
                        "firewallrules": {
                            "_links": {}
                        }
                    }
                }     
                newUrl = self.create_nic.replace("{datacenterId}", dataCenterId).replace("{serverId}", server_name)
                res_status, res_output = self.sendRequest("POST", body, newUrl, headers)
                if res_status == 202:
                    #print("POST Query Response OK - \n" + str(res_output))         
                    return res_output["id"]          
                else:
                    print("POST Query Response NOK - \n" + str(res_output))
                    return None
        
        except Exception as createDataCenterServerNICException:
            print("createDataCenterServerNICException - " + str(createDataCenterServerNICException))

    def createDataCenterServerLAN(self, dataCenterId, resource_name):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                body = {
                    #"metadata": {},
                    "entities": {
                        "nics": {
                            "_links": {}
                        }
                    },
                    "properties": {
                        "name": resource_name,
                        "public": "true"
                    }
                }    
                newUrl = self.create_lan.replace("{datacenterId}", dataCenterId)
                res_status, res_output = self.sendRequest("POST", body, newUrl, headers)
                if res_status == 202:
                    #print("POST Query Response OK - \n" + str(res_output))         
                    return res_output["id"]
                else:
                    print("POST Query Response NOK - \n" + str(res_output))
                    return None
        
        except Exception as createDataCenterServerLANException:
            print("createDataCenterServerLANException - " + str(createDataCenterServerLANException))

    def startServer(self, dataCenterId, server_name, valueNotRequired):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
   
                newUrl = self.start_server.replace("{datacenterId}", dataCenterId).replace("{serverId}", server_name)
                self.sendRequest("POST", {}, newUrl, headers, valueNotRequired)
                # if res_status == 202:

                #     print("POST Query Response OK - \n" + str(res_output))                 
                # else:
                #     print("POST Query Response NOK - \n" + str(res_output))
        
        except Exception as startServerException:
            print("startServerException - " + str(startServerException))

    def getJWT(self, dataCenterId, server_name):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                newUrl = self.JWT.replace("{datacenterId}", dataCenterId).replace("{serverId}", server_name)
                res_status, res_output = self.sendRequest("GET", {}, newUrl, headers)
                if res_status == 200:
                    #print("Get Query Response OK - \n" + str(res_output))
                    return res_output["token"]               
                else:
                    print("Get Query Response NOK - \n" + str(res_output))
        
        except Exception as getJWTException:
            print("getJWTException - " + str(getJWTException))

    def getRemoteConsole(self, dataCenterId, server_name, JWT_Token):
        try:

            # Get an authentication Token
            self.initializeAuthentication()      
            if self.authentic == False:
                raise Exception("Authenticate yourself")
            else:
                headers = {
                    'Authorization': self.authentication,
                    "X-Contract_Number" : "0",          
                }
                newUrl = self.getConsole.replace("{datacenterId}", dataCenterId).replace("{serverId}", server_name)
                res_status, res_output = self.sendRequest("GET", {}, newUrl, headers)
                if res_status == 200:
                    #print("Get Query Response OK - \n" + str(res_output))
                    return res_output["url"]               
                else:
                    print("Get Query Response NOK - \n" + str(res_output))
        
        except Exception as getRemoteConsoleException:
            print("getRemoteConsoleException - " + str(getRemoteConsoleException))