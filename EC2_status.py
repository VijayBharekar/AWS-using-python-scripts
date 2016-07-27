#checking EC2 instance status
import boto3

region='xx-xxxx-x'
instances=['InstanceID']

ec2=boto3.client('ec2',region_name=region)
#ec2.stop_instances(InstanceIds=instances)
output = ec2.describe_instance_status(InstanceIds=instances)
#print 'your instance status is  : %s' %instances[0]
if output["InstanceStatuses"][0]["InstanceId"] == instances[0]:
   print ' instance  %s' %instances[0] + ' is in '+ output["InstanceStatuses"][0]["InstanceState"]["Name"] + ' mode'
else:
    print "Try again..please!!!"
