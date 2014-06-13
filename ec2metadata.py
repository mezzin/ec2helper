import ec2InstanceData
import sys
import argparse

parser = argparse.ArgumentParser(description='This script will get the value of the userdata')
parser.add_argument('-t', '--type', help='type of value needed e.g. userdata, metadata, instance_identity', required=True)
parser.add_argument('-n', '--name', help='name of the userdata value', required=True)

args = vars(parser.parse_args())

if(args["type"] == "userdata"):
    print ec2InstanceData.getUserData(args["name"]);
if(args["type"] == "metadata"):
    print "nothing"
if(args["type"] == "instance_identity"):
    print ec2InstanceData.getInstanceIdentity(args["name"]);