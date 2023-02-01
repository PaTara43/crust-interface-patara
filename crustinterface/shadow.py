"""
Tool for interacting with Crust Shadow Parachain.

"""

import typing as tp

from substrateinterface import KeypairType

from .base import Base


class Shadow(Base):
    """
    Class made for interacting with Crust Shadow Kusama Parachain to store files via Web3 services. Most of the queries
        and extrinsics should be performed in Crust Main net with Mainnet, since files via Shadow are actually
        stored in Crust Mainnet.
    """

    def __init__(self, seed: tp.Optional[str] = None, crypto_type: int = KeypairType.SR25519):

        super().__init__(chain="shadow", seed=seed, crypto_type=crypto_type)

    def get_balance(self) -> int:
        """
        Get your account balance.

        :return: Account balance, pCSMs.

        """

        return self.query("System", "Account", self.keypair.ss58_address).value["data"]["free"]

    def store_file(self, ipfs_cid: str, file_size: int) -> tp.Tuple[str, str]:
        """
        Store a file `already uploaded` to IPFS providing its cid and size.

        :param ipfs_cid: Uploaded file cid.
        :param file_size: Uploaded file size, bytes.

        :return: transaction hash, block_num-event_idx.

        """

        return self.extrinsic("Xstorage", "place_storage_order_through_parachain", dict(cid=ipfs_cid, size=file_size))
