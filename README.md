# ucloud-python-wrapper
KT ucloud storage wrapper for python

- - -

## Average
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
