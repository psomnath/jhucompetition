import hashlib

def hashit(input_list):

  return_list = []
  for data in input_list:
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    return_list.append(hash_object.hexdigest())

  return return_list

input_list = ['psomnath@gmail.com','pass1234']
return_list = hashit(input_list)
for l in return_list:
    print(l)