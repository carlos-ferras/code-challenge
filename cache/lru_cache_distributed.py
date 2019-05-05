from .lru_cache import LRUCache
from .utils.cache_node import CacheNode
from .utils.cache_types import Address, ValueLoadCallBack, CacheKey, CacheValue, NetworkPackage
from .utils.constants import DEFAULT_MAXIMUM_CAPACITY, DEFAULT_EXPIRATION_TIME, DEFAULT_CONNECTION_TIMEOUT, \
    SET_NODE_MESSAGE


class LRUCacheDistributed(LRUCache):
    def __init__(self,
                 load_callback: ValueLoadCallBack,
                 maximum_capacity: int = DEFAULT_MAXIMUM_CAPACITY,
                 expiration_time: int = DEFAULT_EXPIRATION_TIME,
                 connection_timeout: int = DEFAULT_CONNECTION_TIMEOUT,
                 remote_address: Address = None,
                 local_address: Address = None):
        LRUCache.__init__(
            self,
            load_callback,
            maximum_capacity,
            expiration_time
        )

        self.remote_address = remote_address
        self.local_address = local_address
        self.connection_timeout = connection_timeout
        self.server_socket = None
        self.client_socket = None

        self._connect()

    def set(self,
            key: CacheKey,
            value: CacheValue = None,
            expiration_time: int = None,
            from_server: bool = False,
            origin_client: Address = None) -> CacheValue:
        data = {
            'action': SET_NODE_MESSAGE,
            'key': key,
            'value': value,
            'expiration_time': expiration_time
        }
        self._forward_data(data, from_server, origin_client)
        return LRUCache.set(
            self,
            key,
            value,
            expiration_time
        )

    def _move_node_to_start(self,
                            cache_node: CacheNode,
                            from_server: bool = False,
                            origin_client: Address = None) -> CacheValue:
        pass

    def _connect(self) -> None:
        pass

    def _start_server(self) -> None:
        pass

    def _start_client(self) -> None:
        pass

    def _forward_data(self,
                      data: NetworkPackage,
                      from_server: bool = False,
                      origin_client: Address = None) -> None:
        pass

    def _send_data_to_clients(self, data: NetworkPackage, except_client: Address = None) -> None:
        pass

    def _send_data_to_server(self, data: NetworkPackage) -> None:
        pass

    def _listen_clients(self) -> None:
        pass

    def _listen_server(self) -> None:
        pass
