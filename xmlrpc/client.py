import xmlrpclib  
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")  
  
candidate = proxy.findai(2)  
print "the %d-th number of a is %d" %(1, candidate)  
