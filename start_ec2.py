import boto3

region='us-east-1'

instances=['i-a1c18027']

def lambda_handler(event, context):
	
	ec2=boto3.client('ec2',region_name=region)
	
	ec2.start_instances(InstanceIds=instances)
	
	print 'started your instances :'+ str(instances)