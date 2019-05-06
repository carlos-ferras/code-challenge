## Ormuco Code Challenge

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/72856449ef6b4bfa8b5075054186268b)](https://app.codacy.com/app/carlos-ferras/code-challenge?utm_source=github.com&utm_medium=referral&utm_content=carlos-ferras/code-challenge&utm_campaign=Badge_Grade_Dashboard)
[![codecov](https://codecov.io/gh/carlos-ferras/code-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/carlos-ferras/code-challenge)

This project has been created only for demonstration purpose.
>
> ### The challenge
>
> ##### Question A:
> Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
>
> ##### Question B:
> The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
>
> ##### Question C:
> At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
> 1. Simplicity. Integration needs to be dead simple.
> 2. Resilient to network failures or crashes.
> 3. Near real time replication of data across Geolocation. Writes need to be in real time.
> 4. Data consistency across regions
> 5. Locality of reference, data should almost always be available from the closest region
> 6. Flexible Schema
> 7. Cache can expire 
>

### The Answers

#### Question A:

source directory: `./overlap`

usage: 
```
from overlap import overlap

result = overlap((1,5), (4,25))

# It will return True if the lines overlap, False otherwise
```

#### Question B:

source directory: `./compare_versions`

usage: 
```
from compare_versions import compare_versions

result = compare_versions('1.0.0.2.9', '1.0.0.3.4')

# It will return:
#     A positive number: If the first version is greater than the second  
#     A negative number: If the first version is smaller than the second
#     Zero: If the versions are equals
```

#### Question C:

source directory: `./cache`

>
> This feature is not finished yet, but the idea to implement is:
> 1. In each remote server create a local cache
> 2. Each independent cache will have other 2 optional roles at the same time; as server cache and as client cache
> 3. As server cache it will have the responsibility to synchronize all its client caches
> 4. As client cache it will have the responsibility to notify its server cache each time a change occurs
> 5. All this communication will be through sockets in independent threads each one
> 6. If the connection gets broken in any point the caches networks remaining will continue working as independent networks
> 7. If a server gets disconnected from the caches network, its cache will work locally without any problem
> 8. The developer in charge to deploy the system will have the responsibility to decide which server is a cache server or client or both
>

usage for a local cache only: 
```
from lru_cache import LRUCache

def load_callback(key):
    """This function has the responsibility to load the content 
       to store into the cache
    """
    return key

local_cache = LRUCache(
    load_callback=load_callback,
    maximum_capacity=5555,
    expiration_time=5555
)

# get data from the cache; it will call `load_callback` if the 
# value is not available
data_from_cache = local_cache.get('test_key')

# set data manually into the cache
data_from_cache = local_cache.set('test_key', 'test_value')

# More options are only documented into the source code
```

usage for a distributed cache: 
```
from lru_cache_distributed import LRUCacheDistributed

def load_callback(key):
    """This function has the responsibility to load the content 
       to store into the cache
    """
    return key

local_cache = LRUCacheDistributed(
    load_callback=load_callback,
    maximum_capacity=5555,
    expiration_time=5555,
    connection_timeout=5555,
    remote_address=('192.168.1.1', '5555'),  # to be a client
    local_address=('', '5555')  # to be a server
)

# get data from the cache; it will call `load_callback` if the 
# value is not available
data_from_cache = local_cache.get('test_key')

# set data manually into the cache
data_from_cache = local_cache.set('test_key', 'test_value')

# More options are only documented into the source code
```
