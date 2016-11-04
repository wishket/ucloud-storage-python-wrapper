# ucloud-storage-python-wrapper
KT ucloud storage wrapper with python

- - -

   * [ucloud-storage-python-wrapper](#ucloud-storage-python-wrapper)
      * [How to use.](#how-to-use)
      * [Available Range](#available-range)
      * [API Detail Desciption](#api-detail-desciption)
         * [Api Management Object Create (init())](#api-management-object-create-init)
         * [get container list of account (get_container_of_account())](#get-container-list-of-account-get_container_of_account)
            * [params](#params)
         * [get account's metadata (head_account_metadata())](#get-accounts-metadata-head_account_metadata)
         * [add metadata to account (post_account_metadata())](#add-metadata-to-account-post_account_metadata)
            * [params](#params-1)
         * [get container's metadata (head_container_metadata())](#get-containers-metadata-head_container_metadata)
            * [params](#params-2)
         * [get container's object list (get_container_objects())](#get-containers-object-list-get_container_objects)
            * [params](#params-3)
         * [create container (put_container())](#create-container-put_container)
            * [params](#params-4)
         * [delete container (delete_container())](#delete-container-delete_container)
            * [params](#params-5)
         * [add metadata to container (post_container_metadata())](#add-metadata-to-container-post_container_metadata)
            * [params](#params-6)
         * [store object to target container (put_object_to_container())](#store-object-to-target-container-put_object_to_container)
            * [params](#params-7)
         * [delete object from target container (delete_object())](#delete-object-from-target-container-delete_object)
            * [params](#params-8)
         * [get object from target container like download. (get_object())](#get-object-from-target-container-like-download-get_object)

- - -
## How to use.
1. install package.
`pip install ucloud-storage-python-wrapper`
2. create manager object by authentication. then use wrapper api.
```
from uspw.manager import UcloudManager
manager = UcloudManager(key='{user_key}', email='{ucloud_user_email}')

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
1. __limit__ (integer - None) is maximum container length to get
2. __marker__ (string - None) is start point for container list
3. __response_format__ (string - 'json') is type of container list data. default is __json__.
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

#### get container's metadata (`head_container_metadata()`)
return specific container's metadata

###### params
1. __container_name__ (string) is target container's name.

```
result = manager.get_container_metadata('test')

result['object_count'] = container's object count
result['used_bytes'] = container used bytes as human readable string
```

#### get container's object list (`get_container_objects()`)
return container's object list.

###### params
1. __container_name__ (string) is target container's name.
2. __limit__ (integer - None) is maximum object length to get.
3. __marker__ (string - None) is start point for object list.
4. __response_format__ (string - 'json') is type of object list data. default is __json__.
you can use xml format.
5. __prefix__ (string - None) is filter for object name (django's objects filter like start_with).
6. __path__ is not served this api yet.

```
result = manager.get_container_objects

result['object_list'] = object's data as xml or json(python dict)
result['object_count'] = account's all object count
result['used_bytes'] = all used bytes as human readable string
```

#### create container (`put_container()`)
it will create container as served name.

###### params
1. __container_name__ (string) is target container's name.

```
result = manager.put_container('test')

result = status code (201)

```


#### delete container (`delete_container()`)
it will delete container which name is served params.
__you cannot delete container which has child object.__

###### params
1. __container_name__ (string) is target container's name.

```
result = manager.delete_container('test')

result = status code (204)

```


#### add metadata to container (`post_container_metadata()`)
add user custom metadata to container.

###### params
1. __container_name__ (string) is target container's name.
2. __params__ (dict - iterable) is key & value data set for metadata.
like {'username': 'wishket'}
3. __action__ (string) is add or delete action. you can use 'add' or 'delete'.

```
result = manager.post_container_metadata(params, action)

result = status code (201)
```

#### store object to target container (`put_object_to_container()`)
store object data to target container.
you can use specific file path for upload or use data stream (like django's request.FILE['target']).

###### params
1. __container_name__ (string) is target container's name.
2. __file_path__ (string - None) is target object local path. (not url)
3. __file_name__ (string - None) is saved name on container. if you not passed, 
file_path name will be splited for file_name. 
4. __file_stream__ (string - None) is stream data of file's. if you not passed, 
script will open and read of target file_path's file.

```
# use only file_path
result = manager.put_object_to_container('test', file_path='./test.png')

# use with file_name, file_path
result = manager.put_object_to_container('test', file_path='./test.png', file_name='te.png')

# use with file_name, file_stream
result = manager.put_object_to_container('test', file_name='te.png', file_stream=request.FILES['image'])

result = status code (201)
```

#### delete object from target container (`delete_object()`)
delete object from target container's by file_name

###### params
1. __container_name__ (string) is target container's name.
3. __file_name__ (string) is target object's stored name.

```
result = manager.delete_object('test', 'test.png')

result = status code (204)

```

#### get object from target container like download. (`get_object()`)
will be add.