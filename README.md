# ucloud-storage-python-wrapper
KT ucloud storage wrapper with python

- - -

it will be TOC

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

#### Api Management Object Create (`init()`)
you can use two type of authorization.

1. use specific django settings file as key file.
    + if you want to use django.settings add two value.
        - `UCLOUD_EMAIL = 'your email'`
        - `UCLOUD_KEY = 'your key'`
2. insert directly to init()

```
from uspw.manager import UcloudManager

# type a. use django settings file
manager = UcloudManager()

# type b. use specific key, email
manager = UcloudManager(key=user_key, email=user_email)

```

#### get container list of account (`get_container_of_account()`)
return container list and account's usage data.

###### params
1. __limit__ (integer) is maximum container length to get
2. __marker__ (string) is start point for container list
3. __response_format__ (string) is type of container list data. default is __json__.
you can use xml format.

```
# get all container data as json (max=1000)
result = manager.get_container_of_account()

# get 200 container after container which name is 'banana' as xml
result = manager.get_container_of_account(
    limit=200,
    marker='banana',
    response_format='xml'
)

result['container_list'] = object's data as xml or json(python dict)
result['object_count'] = account's all object count
result['used_bytes'] = all used bytes as human readable string

```

#### get account's metadata (`head_account_metadata()`)
return account's metadata

```
result = manager.head_account_metadata()

result['container_count'] = account's container count
result['object_count'] = account's all object count
result['used_bytes'] = all used bytes as human readable string
```


#### add metadata to account (`post_account_metadata()`)
add user custom metadata to account

###### params
1. __params__ (dict - iterable) is key & value data set for metadata.
like {'username': 'wishket'}

2. __action__ (string) is add or delete action. you can use 'add' or 'delete'.

```
result = manager.post_account_metadata(params, action)

result = status code (201)
```

