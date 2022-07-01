# python code for getting the volume id and volume size along with instance ids

#imported the required libraries
import boto3
import base64
import configparser
import sys

#method for getting volume ids and their respective sizes of each instance id
def get_ec2_volumes(ec2_resource):
    res = []
    for instance in ec2_resource.instances.all(): #iterating over all the instances one by one
        vol_list = []
        size_list = [] 
        for volume in instance.volumes.all(): #iterating over all the available volumes of each instance
            vol_list.append(volume.id)
            size_list.append(volume.size)

            # creating a list of nested dictionaries with volume id's as keys and their respective sizes as their values
            new_dict = [{u: {"size": v}} for (u, v) in zip(vol_list, size_list)]

            #creating a dictionary with instance id as a key and their respective volume id's along with their sizes as values
            out = dict({instance.id: new_dict}
                       
        res.append(out) #adding all the instance volume details in to res list
    return res


config = configparser.ConfigParser()
config.read(sys.argv[1]) #reading config file path
#retrieving the credentials from config file and storing them in different variables
resource = config.get('credentials', 'resource')
region = config.get('credentials', 'region')
access_key_id = base64.b64decode(config.get('credentials', 'access_key_id')).decode("utf-8")
secret_access_key = base64.b64decode(config.get('credentials', 'secret_access_key')).decode("utf-8")


#connecting to aws ec2 resource using boto3
ec2 = boto3.resource(resource,
                   region,
                   aws_access_key_id=access_key_id,
                   aws_secret_access_key=secret_access_key)


print(get_ec2_volumes(ec2)) #calling the method for getting required details of each instance

