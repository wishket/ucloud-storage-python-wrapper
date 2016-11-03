# ucloud-python-wrapper
KT ucloud storage wrapper for python

- - -

**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [ucloud-python-wrapper](#)
	- [How to use.](#)
	- [Available Range](#)
    - [API Detail Description](#)
- - -
## How to use.
1. install package.
`pip install ucloud-storage-python-wrapper`
2. create manager object by authentication.
```
from uspw.manager import UcloudManager

manager = UcloudManager(key='{user_key}', email='{ucloud_user_email}')
```
3. use wrapper api.
```
result = manager.put_object_to_container('my_container', file_stream)
```

## Available Range
1. Account authentication : Serve specific part.
    + Token Authenticate : serve
    + IP Authenticate : not serve
2. Storage Accounts : Serve
    + get storage of account : serve
    + head storage of account (get metadata): serve
    + post sotrage of account (set metadata) : serve    
3. Storage Containers : Serve specific part.
    + HEAD container (get metadata) : serve
    + GET container's object : serve
    + PUT container (create container) : serve
    + DELETE container : serve
    + POST container (set metadata) : serve
    + POST container (ACL) : not serve
    + POST container as static website : not serve
    + POST container logging : not serve
    + POST container access IP controll : not serve 
4. Storage Objects : Serve
    + HEAD object (get metadata) : serve
    + GET object : serve
    + PUT object : serve
    + PUT large object : not serve
    + Chunked Transfer Encoding : not serve
    + copy object : serve
    + POST object (set metadata) : not serve
    + DELETE object
5. Reseller Service API : Not serve. No Plan.

## API Detail Desciption
+ Api Management Object Create
```
from uspw.manager import UcloudManager

# use options file
manager = UcloudManager()

# use specific key, email
manager = UcloudManager(key=user_key, email=user_email)

```