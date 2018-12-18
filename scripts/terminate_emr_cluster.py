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

    client = boto3.client('emr', region_name='us-east-1')

    response = client.terminate_job_flows(
    JobFlowIds=[
        ClusterID,
    ]
    )
    print(response)


main()
