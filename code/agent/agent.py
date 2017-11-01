#!/usr/bin/env python
import time
import urllib, urllib2
import json
import hashlib
import os
import subprocess

class Method:
    def __init__(self):
        self.task_url="http://localhost:8080/task"
        self.script_url="http://localhost:8080/script"
        self.upload_url="http://localhost:8080/upload"
        self.id="{'nodeid':'172.31.56.44-00:16:3e:00:30:b3'}"

    def getTask(self):
        #task_req = urllib2.Request(self.task_url, self.id, {'Content-Type': 'application/json'})
        #task_f = urllib2.urlopen(task_req)
        #task_response = task_f.read()
        #task_f.close()
        test_str = '{"nodeid":"172.31.56.44-00:16:3e:00:30:b3", "task":[{"taskID":"4096","execTime":"192321343", "taskName":"get cpu usage info", "scriptID":"f5e07fafe072303ddebac6a5d8d7e366", "scriptName":"get_cpu_usage.py"}, {"taskID":"5639","execTime":"12345667", "taskName":"get memory usage info", "scriptID":"f94da6f2ff7024893a34edf785e89b54", "scriptName":"get_mem_usage.py"}]}'
        task_response = json.loads(test_str)
        return task_response 

    def getMD5(self, filename):
        return hashlib.md5(filename).hexdigest()

    def getLocalScript(self, script_name, script_md5sum):
        if os.path.exists(script_name):
            if script_md5sum == self.getMD5(script_name):
                #print script_md5sum 
                return True
            else:
               # print script_md5sum 
               # print self.getMD5(script_name) 
                print "local script %s md5 error, please update script" % script_name
                return False
        else:
            print "file %s not exist, please download script" % script_name
            return False

    def getRemoteScript(self,scriptName):
        #script_req = urllib2.Request(self.script_url, self.id, {'Content-Type': 'application/json'})
        #script_f = urllib2.urlopen(script_req)
        #with open(scriptName, "wb") as code:
        #    code.write(script_f.read())
        #script_f.close()
        command='echo "#!/usr/bin/python" > ' + scriptName + """; echo 'print "xxx" ' >>  """ + scriptName
        subprocess.call(command, shell=True)
        #return script_response 

    def uploadData(self,data):
        #upload_req = urllib2.Request(self.upload_url, self.id, {'Content-Type': 'application/json'})
        #upload_f = urllib2.urlopen(upload_req)
        #upload_response = upload_f.read()
        #upload_f.close()
        print "data upload ok" 

    def execScript(self,scriptPath):
        #https://blog.linuxeye.cn/375.html
        cmd="python %s" % scriptPath
        return subprocess.check_output(cmd, shell=True)
        
if __name__ == "__main__":
  while True:
    method = Method()
    task = method.getTask()
    if len(task["task"]) > 0 :
        for t in task["task"]:
            if method.getLocalScript(t["scriptName"], t["scriptID"]):
                d = method.execScript(t["scriptName"])
                method.uploadData(d) 
            else:
                method.getRemoteScript(t["scriptName"])
                dd = method.execScript(t["scriptName"])
                method.uploadData(dd)
    time.sleep(10)
