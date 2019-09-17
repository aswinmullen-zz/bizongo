#!/usr/local/bin/python3
import boto3
ec2=boto3.client('ec2', 'ap-south-1')
sg = ec2.describe_security_groups()["SecurityGroups"]
for i in sg:
        group_name = i['GroupName']
        ip = i['IpPermissions']
        for j in ip:
                for m in j['IpRanges']:
                        cidr = m['CidrIp']
                        if (cidr == '0.0.0.0/0'):
                                print(group_name)
