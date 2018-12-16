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
    results = parser.parse_args(args)
    return (results.ClusterID)
 
def main():
    ClusterID = check_arg(sys.argv[1:])
    maxAttempts = 60 
    sleepTimeInSeconds = 30
    waitTime = (maxAttempts * sleepTimeInSeconds) / 60

    client = boto3.client('emr', region_name='us-east-1')
    print("Waiting upto", int(waitTime)," seconds for the cluster to start up...")
    for i in range(maxAttempts):
        response = client.describe_cluster(
            ClusterId = ClusterID
        )
        status = response['Cluster']['Status']['State']
        print("current cluster status:", status)
        if status == 'STARTING':
            time.sleep(sleepTimeInSeconds)
        elif status == 'WAITING':
            sys.exit(0)
        elif status == 'TERMINATED_WITH_ERRORS':
            print("ERROR!!! Cluster TERMINATED WITH ERRORS")
            sys.exit(1)
        elif status == 'TERMINATING':
            print("ERROR!!! Cluster is TERMINATING")
            sys.exit(1)
        elif status == 'TERMINATED':
            print("ERROR!!! Cluster is TERMINATED")
            sys.exit(1)
    print("ERROR!!! Timed out on determening cluster status")
    sys.exit(1)
        
main()
