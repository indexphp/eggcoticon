import hashlib
import json
in_file_path='path.json'
with open(in_file_path,'r') as in_json_file:
  json_obj_list = json.load(in_json_file)
  for json_obj in json_obj_list:
    path = ('images'+'/'+json_obj['id']+'.jpg')
    with open(path,"rb") as f:
          bytes = f.read() # read entire file as bytes
          readable_hash = hashlib.sha256(bytes).hexdigest();
          file1 = open("sha256.txt","a")#append mode
          file1.write(readable_hash+"\n")
          file1.close()
          print('TokenID'+' '+readable_hash)
