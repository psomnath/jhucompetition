import hashlib

def hashit(user_account):

  [uid, password] = user_account
  hash_object = hashlib.sha256()
    
  hash_object.update(uid.encode())
  uid_encrypt = hash_object.hexdigest()
    
  hash_object.update(password.encode())
  password_encrypt = hash_object.hexdigest()

  return [uid_encrypt,password_encrypt]

user_accounts = [['psomnath@gmail.com','pass1234'],['spurkay1@jhu.com','pass1234'], ['ayasin1@jhu.edu','pass1234']]
for user_account in user_accounts:
    user_account_encrypt = hashit(user_account)
    print(user_account_encrypt)