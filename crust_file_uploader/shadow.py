import typing as tp

from substrateinterface import Keypair

from .constants import CRUST_SHADOW_ENDPOINT
from .exceptions import NoPrivateKeyException
from .utils import create_keypair, extrinsic, query


class UploaderShadow:
    """
    Class made for interacting with Crust Shadow Kusama Parachain to store files via Web3 services. Most of the queries
        and extrinsics should be performed in Crust Main net with UploaderCrust, since files via Shadow are actually
        stored in Crust Mainnet.
    """

    def __init__(self, seed: str = None) -> None:
        """
        Initialize Crust Shadow uploader class. Set websocket and keypair.

        :param seed: Account seed.

        """

        self._shadow: str = CRUST_SHADOW_ENDPOINT

        if seed:
            self._keypair: Keypair = create_keypair(seed)
        else:
            self._keypair = None

    def get_balance(self) -> int:
        """
        Get your account balance.

        :return: Account balance, pCSMs.

        """

        if not self._keypair:
            raise NoPrivateKeyException("No seed was provided, unable to get self balance.")

        return query(self._shadow, "System", "Account", self._keypair.ss58_address).value["data"]["free"]

    def store_file(self, ipfs_cid: str, file_size: int) -> tp.Tuple[str, str]:
        """
        Store a file `already uploaded` to IPFS providing its cid and size.

        :param ipfs_cid: Uploaded file cid.
        :param file_size: Uploaded file size, bytes.

        :return: transaction hash, block_num-event_idx.

        """

        if not self._keypair:
            raise NoPrivateKeyException("No seed was provided, unable to use extrinsics.")

        return extrinsic(
            self._shadow,
            self._keypair,
            "xstorage",
            "place_storage_order_through_parachain",
            dict(cid=ipfs_cid, size=file_size),
        )
