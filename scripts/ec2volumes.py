
# python code for getting the volume id and volume size along with instance ids
import boto3
ec2 = boto3.resource('ec2',
                   'us-east-1',
                   aws_access_key_id='AKIAQHKJUW5SSADWMHWX',
                   aws_secret_access_key='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')
res=[]
for instance in ec2.instances.all():
    vol_list = []
    size_list = []
    for volume in instance.volumes.all():
        vol_list.append(volume.id)
        size_list.append(volume.size)
        new_dict = [{u : {"size" : v}} for (u,v) in zip(vol_list,size_list)]
        out = dict({instance.id:new_dict})
    res.append(out)
print(res)
#print(*res,sep=',\n')
