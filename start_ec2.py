#Start instance using Python
import boto3

region='xx-xxxx-x'

instances=['InstanceId']

def lambda_handler(event, context):
	
	ec2=boto3.client('ec2',region_name=region)
	
	ec2.start_instances(InstanceIds=instances)
	
	print 'started your instances :'+ str(instances)
