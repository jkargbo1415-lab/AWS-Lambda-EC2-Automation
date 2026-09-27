import os

import boto3


ec2 = boto3.client("ec2")


def lambda_handler(event, context):
    """Start or stop the EC2 instances listed in the INSTANCE_IDS variable."""
    instance_ids = os.environ["INSTANCE_IDS"].split(",")
    action = event.get("action", os.environ.get("ACTION", "stop")).lower()

    if action == "start":
        ec2.start_instances(InstanceIds=instance_ids)
    elif action == "stop":
        ec2.stop_instances(InstanceIds=instance_ids)
    else:
        raise ValueError("ACTION must be 'start' or 'stop'")

    return {
        "statusCode": 200,
        "message": f"Successfully requested EC2 instances to {action}",
        "instance_ids": instance_ids,
    }
