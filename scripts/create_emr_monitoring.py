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
 
def main():
    ClusterID, ClusterName = check_arg(sys.argv[1:])
    client = boto3.client('cloudwatch')
    dashboardTemplate='{"widgets":[{"type":"metric","x":0,"y":0,"width":24,"height":3,"properties":{"view":"singleValue","metrics":[["AWS/ElasticMapReduce","TotalLoad","JobFlowId","j-2V3IPUFKMUUIR"],[".","MRActiveNodes",".","."],[".","MemoryTotalMB",".","."],[".","CoreNodesRunning",".","."],[".","CoreNodesPending",".","."]],"region":"us-east-1"}}]}'

    response = client.put_dashboard(
        DashboardName = ClusterName,
        DashboardBody = dashboardTemplate
    )

main()
