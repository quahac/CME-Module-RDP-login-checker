import subprocess, os, re


class NXCModule:

    name = 'rdplogin'
    description = 'Module checks if a valid user has also Remote Desktop access on the server...(needs Hydra to work!)'
    supported_protocols = ['smb']
    opsec_safe= True 
    multiple_hosts = True 

    def options(self, context, module_options):
        pass

    def on_login(self, context, connection):
        try:       
            if (len(connection.password) == 0):
              exit(1)  
            rdp_arg = 'rdp://' + connection.host + '/' + connection.domain
            p = subprocess.run(['hydra', '-I', '-q', '-l', connection.username, '-p', connection.password, rdp_arg], capture_output=True, text=True, timeout=10).stdout
            result = re.search("successfully", p)
            if result:
                context.log.success("RDP Access Granted")      
            else:
                context.log.fail("RDP Access NOT Granted")
        except:
            pass
        pass

class CMEModule:

    name = 'rdplogin'
    description = 'Module checks if a valid user has also Remote Desktop access on the server...(needs Hydra to work!)'
    supported_protocols = ['smb']
    opsec_safe= True 
    multiple_hosts = True 

    def options(self, context, module_options):
        pass

    def on_login(self, context, connection):
        try:       
            if (len(connection.password) == 0):
              exit(1)  
            rdp_arg = 'rdp://' + connection.host + '/' + connection.domain
            p = subprocess.run(['hydra', '-I', '-q', '-l', connection.username, '-p', connection.password, rdp_arg], capture_output=True, text=True, timeout=10).stdout
            result = re.search("successfully", p)
            if result:
                context.log.success("RDP Access Granted")      
            else:
                context.log.fail("RDP Access NOT Granted")
        except:
            pass
        pass
