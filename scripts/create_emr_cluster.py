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

def main()
    client = boto3.client('emr', region_name='us-east-1')

    response = client.run_job_flow(
        Name = ClusterName,
        ReleaseLabel='emr-5.19.0',
        Instances={
            'MasterInstanceType': 'm1.small',
            'SlaveInstanceType': 'm1.small',
            'InstanceCount': 3,
            'KeepJobFlowAliveWhenNoSteps': True,
            'TerminationProtected': False,
            'Ec2SubnetId': 'subnet-6db2c242',
            'Ec2KeyName': 'kotortech-aws',
        },
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole'
    )
    print (response['JobFlowId'])
connection = boto3.client(
    'emr',
    region_name='us-west-1',
    aws_access_key_id='<Your AWS Access Key>',
    aws_secret_access_key='<You AWS Secred Key>',
)

cluster_id = connection.run_job_flow(
    Name='test_emr_job_with_boto3',
    LogUri='',
    ReleaseLabel='emr-4.2.0',
    Instances={
        'InstanceGroups': [
            {
                'Name': "Master node",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm1.small',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm1.small',
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
