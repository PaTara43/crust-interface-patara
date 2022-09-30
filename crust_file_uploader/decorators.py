"""
Decorators to open interface instances when necessary only.

"""

import substrateinterface as substrate

from functools import wraps
from websocket._exceptions import WebSocketConnectionClosedException

from .constants import (
    CRUST_SS_58_FORMAT,
    CRUST_TYPE_REGISTRY_PRESET,
    CRUST_MAINNET_ENDPOINT,
    CRUST_ROCKY_TESTNET_ENDPOINT,
)


def check_interface_opened(func):
    """
    Open substrate node connection each time needed.

    :param func: wrapped function.

    :return: wrapped function after augmentations.

    """

    @wraps(func)
    def wrapper(crust_interface, *args, **kwargs):
        """
        Wrap decorated function with interface opening if it was closed.

        :param crust_interface: Crust interface instance in a decorated function.
        :param args: Wrapped function args.
        :param kwargs: Wrapped function kwargs.

        """

        if not crust_interface.interface:
            open_interface(crust_interface)

        try:
            res = func(crust_interface, *args, **kwargs)
        except (BrokenPipeError, WebSocketConnectionClosedException):
            open_interface(crust_interface)
            res = func(crust_interface, *args, **kwargs)

        return res

    return wrapper


def open_interface(interface_instance):
    """
    (Re-)open a new node interface instance.

    :param interface_instance: Interface to (re-)open.

    """

    interface_instance.interface = substrate.SubstrateInterface(
        url=interface_instance.remote_ws,
        ss58_format=CRUST_SS_58_FORMAT,
        type_registry_preset=CRUST_TYPE_REGISTRY_PRESET
        if interface_instance.remote_ws in [CRUST_MAINNET_ENDPOINT, CRUST_ROCKY_TESTNET_ENDPOINT]
        else None
    )
