## Ormuco Code Challenge

This project has been created only for demonstration purpose.
>
> ### The challenge
>
> At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
> 1. Simplicity. Integration needs to be dead simple.
> 2. Resilient to network failures or crashes.
> 3. Near real time replication of data across Geolocation. Writes need to be in real time.
> 4. Data consistency across regions
> 5. Locality of reference, data should almost always be available from the closest region
> 6. Flexible Schema
> 7. Cache can expire 
>

### The Answer

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

usage:

- Run `pip3 install cf_LRU_cache`

usage for a local cache only: 
```
from lru_cache.lru_cache import LRUCache

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
from lru_cache.lru_cache_distributed import LRUCacheDistributed

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
