import urllib3
import json

in_file_path='cek.json' # Change me!

with open(in_file_path,'r') as in_json_file:

    # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)

    for json_obj in json_obj_list:
        http = urllib3.PoolManager()
        url='https://api.opensea.io/asset/matic/0xa8997ce074bc73fe9ec40406734fe5528ead84b1/'
        resp = http.request("GET", url + json_obj['id']+ '/validate/')
        status = str(resp.status)
        filename = json_obj['id']
        file1 = open("status.txt","a")#append mode
        file1.write(filename+' '+status+"\n")
        file1.close()
        print('TokenID'+' '+filename+' '+status)
