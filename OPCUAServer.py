# OPCUA Server gemaakt door JBsystems groep 8

# Make sure that you have installed the opcua lib
from opcua import Server
from random import randint
import datetime
import time

#initializing the server
server = Server()

# the OPCUA server will be hosted on localhost port 4841
# If this port is already taken you can change it to 4840 or 4820
# If the other ports don't work open the cmd and type netstat and check if any other port is available
url = "opc.tcp://0.0.0.0:4841"

# setup
server.set_endpoint(url)
name = "OPCUA_SIMULATTION_SERVER_JBSYSTEM_GROEP_08"
addspace = server.register_namespace(name)

node = server.get_objects_node()

# Parameters settings
Param = node.add_object(addspace, "Parameters")

# each individual node setting
deliveryOptions = ["Afvoer1", "Afvoer2", "Opslag1"]
Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

# set 
Temp.set_writable()
Press.set_writable()
Time.set_writable()

# starting server 
server.start()
print("Server started at {}".format(url))

# Server simulation details
iteratie = 0
count = len(deliveryOptions)
print(count)

# After each tick of the server the following data occures
while True:    
  
    Temperature = randint(0, 100)
    Pressure = randint(200, 999)
    TIME = datetime.datetime.now()

    print(deliveryOptions[iteratie],Temperature,Pressure,TIME)
    iteratie += 1

    if iteratie == count:
     print (iteratie)
     iteratie = 0
    else:    
     print (iteratie)
     
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    # Time that server waits for new tick
    time.sleep(2)
