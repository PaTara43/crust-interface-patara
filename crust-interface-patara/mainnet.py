import typing as tp

from substrateinterface import KeypairType

from .base import Base


class Mainnet(Base):
    """
    Class made for interacting with Crust Network to store files via Web3 services.
    """

    def __init__(self, seed: tp.Optional[str] = None, crypto_type: int = KeypairType.SR25519):

        super().__init__(chain="mainnet", seed=seed, crypto_type=crypto_type)

    def get_balance(self) -> int:
        """
        Get your account balance.

        :return: Account balance, pCRUs.

        """

        return self.query("System", "Account", self.keypair.ss58_address).value["data"]["free"]

    def get_appx_store_price(self, file_size: int) -> int:
        """
        Calculate an approximate price of the file.

        :param file_size: File size, bytes.

        :return: Approximate 6 months store cost, pCRUs.
        """

        # Returns base size-independent fee, pCRUs
        base_fee = self.query("Market", "FileBaseFee").value
        # Returns pCRUs fee per MB
        size_fee = self.query("Market", "FileByteFee").value

        return round(base_fee + size_fee * file_size / (1024 ** 2))

    def get_replicas(self, ipfs_cid: str) -> int:
        """
        Get number of file replicas in Crust network.

        :param ipfs_cid: Stored file cid.

        :return: Number of replicas.

        """

        return self.query("Market", "FilesV2", ipfs_cid).value["reported_replica_count"]

    def add_renewal_pool_balance(self, ipfs_cid: str, amount: int) -> tp.Tuple[str, str]:
        """
        Add funds to a renewal pool balance.
            https://wiki.crust.network/docs/en/storageUserGuide#124-renew-the-file-pool-balance. DOESN'T WORK ON SHADOW,
            will be executed in Mainnet.

        :param ipfs_cid: Stored file cid.
        :param amount: Amount of funds to be added, pCRUs. Make sure to add at balance which is enough for at least 6
            months. Use `calculate_appx_store_price` to check.

        :return: transaction hash, block_num-event_idx.

        """

        return self.extrinsic("Market", "add_prepaid", dict(cid=ipfs_cid, amount=amount))

    def store_file(self, ipfs_cid: str, file_size: int, tips: int = 0) -> tp.Tuple[str, str]:
        """
        Store a file `already uploaded` to IPFS providing its cid and size.

        :param ipfs_cid: Uploaded file cid.
        :param file_size: Uploaded file size, bytes.
        :param tips: Tips for the file host, pCRUs.

        :return: transaction hash, block_num-event_idx
        """

        return self.extrinsic(
            "Market", "place_storage_order", dict(cid=ipfs_cid, reported_file_size=file_size, tips=tips, _memo="")
        )
