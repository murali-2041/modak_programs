import boto3
def list_object_with_latest_timestamp(s3_files_path):
   s3 = boto3.resource('s3')
   bucket_path_list = s3_files_path.split('/')
   bucket = bucket_path_list[2]
   print(bucket)
   folder_path = bucket_path_list[3:]
   print(folder_path)
   prefix = ""
   if(folder_path==[]):
     result = s3.meta.client.list_objects(Bucket=bucket, Prefix=prefix)
   else:
     for path in folder_path:
        prefix = prefix + path + '/'
        result = s3.meta.client.list_objects(Bucket=bucket, Prefix=prefix)
   print(result)
   if 'Contents' in result.keys():
       last_modified_timestamp = result['Contents'][0]["LastModified"]
       for obj in result['Contents']:
         if str(obj["LastModified"]) >= str(last_modified_timestamp):
           last_modified_timestamp = obj["LastModified"]
       for obj in result['Contents']:
         if str(obj["LastModified"]) == str(last_modified_timestamp):
           full_s3_file = "s3://" + bucket + "/" + obj["Key"]
           break
   else:
       prefix = prefix[0:len(prefix)-1]
       print(prefix)
       result1 = s3.meta.client.list_objects(Bucket=bucket, Prefix=prefix)
       print(result1)
       full_s3_file = "s3://" + bucket + "/" + result1['Contents'][0]["Key"]
       last_modified_timestamp = result1['Contents'][0]['LastModified']
   return full_s3_file,last_modified_timestamp
print(list_object_with_latest_timestamp("s3://arch-dev-datalake/abbvie-hadoop-arch/zeppelin/notebook/2EC4CK5FD/note.json"))
