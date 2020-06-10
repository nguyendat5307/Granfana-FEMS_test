import json
import paho.mqtt.subscribe as subscribe
topics = ["SAVINA/SPMS10kW/27HOANGHOATHAM/DANANG/07052020/GateWay02"]
auth = {"username":"mind", "password":"123"}
hostname = "202.158.245.111"
m = subscribe.simple(topics, transport="tcp", hostname=hostname, port=16766, auth=auth)
print(m.payload)
print(json.loads(m.payload))