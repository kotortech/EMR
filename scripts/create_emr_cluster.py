#!/usr/bin/env python

import argparse
import sys
import boto3

def check_arg(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-CN', '--ClusterName',
                        help='Name of the EMR cluster',
                        required='True',
                        default='EMRCXX')
    results = parser.parse_args(args)
    return (results.ClusterName)

def main():
    ClusterName = check_arg(sys.argv[1:])
    client = boto3.client('emr', region_name='us-east-1')
    cluster_id = client.run_job_flow(
    Name=ClusterName,
    LogUri='s3n://aws-logs-994386103535-us-east-1/elasticmapreduce',
    ReleaseLabel='emr-5.19.0',
    Instances={
        'InstanceGroups': [
            { 
                'Name': "Master node",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'c1.medium',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'c1.medium',
                'InstanceCount': 2,
            }
        ],
        'Ec2KeyName': 'kotortech-aws',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': 'subnet-6db2c242',
        },
        Steps=[],
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
    )
    print (cluster_id['JobFlowId'])

main()
