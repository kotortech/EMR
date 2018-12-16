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
    print(ClusterID,ClusterName)
    client = boto3.client('cloudwatch', region_name='us-east-1')

    response = client.put_dashboard(
        DashboardName=ClusterName,
        DashboardBody='string'
    )

main()
