from .lru_cache import LRUCache
from .utils.cache_node import CacheNode
from .utils.cache_types import Address, ValueLoadCallBack, CacheKey, CacheValue, NetworkPackage
from .utils.constants import DEFAULT_MAXIMUM_CAPACITY, DEFAULT_EXPIRATION_TIME, DEFAULT_CONNECTION_TIMEOUT, \
    SET_NODE_MESSAGE, MOVE_NODE_TO_START_MESSAGE


class LRUCacheDistributed(LRUCache):
    """Distributed LRU Cache implementation

    """

    def __init__(self,
                 load_callback: ValueLoadCallBack,
                 maximum_capacity: int = DEFAULT_MAXIMUM_CAPACITY,
                 expiration_time: int = DEFAULT_EXPIRATION_TIME,
                 connection_timeout: int = DEFAULT_CONNECTION_TIMEOUT,
                 remote_address: Address = None,
                 local_address: Address = None):
        """
        :param load_callback: Method to call to load new content from the network,
            it is used if you try to get a key which does't exist yet,
            it should receive a key as argument and return the loaded value
        :param maximum_capacity: Maximum amount of nodes that the cache will store; by default it is 50000
        :param expiration_time: Maximum validity time for a node into the cache in seconds; by default it is 5184000
        :param connection_timeout: Timeout for socket connections in milliseconds; by default it is 3600
        :param remote_address: Cache server address to get connected;
            it is the local_address of this same class in a different server.
            It could be a tuple(hostname, port) or an string containing a UNIX socket path
        :param local_address:  Local address to open a socket connection as a cache server.
            It could be a tuple(hostname, port) or an string containing a UNIX socket path
        """

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
        """Add new or Update is exist a cache node

        :param key: Cache node identifier
        :param value: Associated cache value for this key
        :param expiration_time: Maximum validity time for this node into the cache in seconds;
            if None, the default will be used.
        :param from_server: Indicates if the data comes from the server cache
        :param origin_client: The client address source for this node; in case it comes from one client cache
        :return: Cache value for this node
        """

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
        """

        :param cache_node: Cache node to move
        :param from_server: Indicates if the data comes from the server cache
        :param origin_client: The client address source for this node; in case it comes from one client cache
        :return: Cache node value
        """

        data = {
            'action': MOVE_NODE_TO_START_MESSAGE,
            'node': cache_node
        }
        self._forward_data(data, from_server, origin_client)
        return LRUCache._move_node_to_start(
            self,
            cache_node
        )

    def _connect(self) -> None:
        """Create server and client sockets connections
        """

        if self.remote_address is not None:
            self._start_client()
        if self.local_address is not None:
            self._start_server()

    def _start_server(self) -> None:
        """Create the server socket
        """

        if self.local_address is not None:
            # TODO: open a socket in the address self.local_address as server cache using an independent thread
            pass

    def _start_client(self) -> None:
        """Create the client socket
        """

        if self.remote_address is not None:
            # TODO: open a socket to listen the address self.remote_address as client cache using an independent thread
            pass

    def _forward_data(self,
                      data: NetworkPackage,
                      from_server: bool = False,
                      origin_client: Address = None) -> None:
        """

        :param data: Data to forward to the server and clients
        :param from_server: Indicates if the data comes from the server cache
        :param origin_client: The client address source for this node; in case it comes from one client cache
        """

        self._send_data_to_clients(data, origin_client)
        if not from_server:
            self._send_data_to_server(data)

    def _send_data_to_clients(self, data: NetworkPackage, except_client: Address = None) -> None:
        """Send data to all connected clients cache

        :param data: Data to send to the clients
        :param except_client: Ignore this client address
        """

        # TODO: send data to all subscribed clients except the one whit address = except_client
        pass

    def _send_data_to_server(self, data: NetworkPackage) -> None:
        """Send data to the server cache

        :param data: Data to send to the server
        """
        pass

    def _listen_clients(self) -> None:
        """Listen for messages from the clients
        """

        # TODO: If receive a message call self.set(data.key, data.value, data.expiration_time, False, client_address)
        pass

    def _listen_server(self) -> None:
        """Listen for messages from the server
        """

        # TODO: If receive a message call self.set(data.key, data.value, data.expiration_time, True)
        pass
