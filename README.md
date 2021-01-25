# AWS-Lambda-ec2snapshot
This lambda function takes scheduled snapshots of ec2 volumes and keeps the 3 most recent snapshots.

IAM JSON policies for permissions attached + two different lambda functions - one for the periodic ec2 backups , the other for pruning the backups. 
