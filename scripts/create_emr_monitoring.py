#!/usr/bin/env python

import argparse
import sys
import boto3
import time

def check_arg(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-CID', '--ClusterID',
                        help='ID of the EMR cluster',
                        required='True',
                        default='j-XXXXXXXX')
    parser.add_argument('-CN', '--ClusterName',
                        help='Name of the EMR cluster',
                        required='True',
                        default='EMRCXX')
    results = parser.parse_args(args)
    return (results.ClusterID,results.ClusterName)
 
#globals
ClusterID, ClusterName = check_arg(sys.argv[1:])
client = boto3.client('cloudwatch')

def create_dashboard():
    dashboardTemplate='{"widgets":[{"type":"metric","x":0,"y":0,"width":24,"height":3,"properties":{"view":"singleValue","metrics":[["AWS/ElasticMapReduce","TotalLoad","JobFlowId","j-2V3IPUFKMUUIR"],[".","MRActiveNodes",".","."],[".","MemoryTotalMB",".","."],[".","CoreNodesRunning",".","."],[".","CoreNodesPending",".","."]],"region":"us-east-1"}}]}'

    response = client.put_dashboard(
        DashboardName = ClusterName,
        DashboardBody = dashboardTemplate
    )

def create_CoreNodesRunning_alarm():
    AlarmNameString = ClusterName + ' Core Nodes Running Violation'
    client.put_metric_alarm(
        AlarmName=AlarmNameString,
        ComparisonOperator='LessThanThreshold',
        EvaluationPeriods=1,
        MetricName='CoreNodesRunning',
        Namespace='AWS/ElasticMapReduce',
        Period=60,
        Statistic='Minimum',
        Threshold=2,
        ActionsEnabled=True,
        AlarmDescription='Insufficient number of Core Nodes Running',
        AlarmActions=['arn:aws:sns:us-east-1:994386103535:oncall'],
	TreatMissingData='breaching',
        Dimensions=[
            {
                'Name': 'JobFlowId',
                'Value': ClusterID 
            },
        ],
    )

def main():
    create_dashboard()
    create_CoreNodesRunning_alarm()

main()
