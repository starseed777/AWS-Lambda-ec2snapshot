import boto3 

def lambda_handler(event, context):
    account_id = boto3.client("sts").get_caller_identity().get("Account")
    ec2 = boto3.client("ec2")
    regions = [region["RegionName"]
                
                for region in ec2.describe_regions()["Regions"]]

    for region in regions:
        print("Region:", region)
        ec2 = boto3.client("ec2", region_name=region)
        response = ec2.describe_snapshots(OwnerIds = [account_id])
        snapshots = response["Snapshots"]

        #sort snapshots 
        snapshots.sort(key=lambda x: x["StartTime"])

        #keeps 3 most recent
        snapshots = snapshots[:-3]

        for snapshot in snapshots:
            id = snapshot["SnapshotId"]
            try:
                print("Deleting snapshot id", id)
                ec2.delete_snapshot(SnapshotId=id)
            except Exception as e:
                print("snapshot {} in use, skipping").format(id)
                continue