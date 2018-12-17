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


def remove_dashboard():
    response = client.delete_dashboards(
        DashboardNames=[ClusterName]
    )


def remove_CoreNodesRunning_alarm():
    AlarmNameString = ClusterName + ' Core Nodes Running Violation'

    response = client.delete_alarms(
        AlarmNames=[AlarmNameString]
    )


def main():
    remove_dashboard()
    remove_CoreNodesRunning_alarm()

main()
