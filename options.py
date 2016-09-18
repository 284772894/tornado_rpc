__author__ = 'Administrator'
processnum = 1
maxclientnum = 10
clientnum = 10
testtime = 1
flag = 1

stat_rpc_server = "localhost"
stat_rpc_port= "4321"


datafile_json = {}
datafile_json["protocol_type"] = "get"
datafile_json["data_type"] = "json"
datafile_json["url_string"] = "dgm.boweixin.com/GetPersonalHomePage?lookerId=2&userId=30"
datafile_json["headers"] = {"Content-type":"application/json"}
datafile_json["body"] = [{}]
datafile_json["connection_tmout"] = 3000
datafile_json["request_tmout"] = 3000
