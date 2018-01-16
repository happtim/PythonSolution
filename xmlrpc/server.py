from SimpleXMLRPCServer import SimpleXMLRPCServer  
global a  
  
def load():  
    global a  
    a = [1 ,2, 24]  
    return a  
  
def findai(i,f):  
    global a
    print a[i]
    print f
    return a[i]  
  
server = SimpleXMLRPCServer(("localhost", 8000))  
server.register_function(findai,"findai")  
load()  
server.serve_forever()   
