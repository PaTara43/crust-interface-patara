import requests
import typing as tp

from ast import literal_eval
from substrateinterface import Keypair

from .constants import W3GW, W3PS
from .exceptions import NoPrivateKeyException, FailedToUploadFile, FailedToPinFile, InvaliIdPFSCIDFormat
from .utils import create_keypair


class Web3Gateway:
    """
    Use Web3 gateway with pubkey authorization to upload files to IPFS network.

    """

    def __init__(self, seed: str):

        self._keypair: Keypair = create_keypair(seed)

    def upload_file(self, file_path: str, file_name: tp.Optional[str] = None, pin: bool = False) -> tp.Tuple[str, int]:
        """
        Upload a file to IPFS via IPFS Web3 Gateway with private key-signed message. The signed message is user's
            pubkey. https://wiki.crust.network/docs/en/buildIPFSWeb3AuthGW#usage.

        :param file_path: Path to a file to be uploaded.
        :param file_name: A name you want to give to the file.
        :param pin: Whether pin the file via Web3 pinning service or not.

        :return: (IPFS cid, file size in bytes)

        """

        with open(file_path, "rb") as f:
            content = f.read()
        file_name_ = file_name or file_path[file_path.rfind("/") + 1 : len(file_path)]

        response = requests.post(
            W3GW,
            auth=(f"sub-{self._keypair.ss58_address}", f"0x{self._keypair.sign(self._keypair.ss58_address).hex()}"),
            files={"file@": (None, content)},
            json={"name": file_name_},
        )

        if response.status_code == 200:
            resp = literal_eval(response.content.decode("utf-8"))
            cid = resp["Hash"]
            size = int(resp["Size"])
        else:
            raise FailedToUploadFile(response.status_code)

        if pin:
            self._pin_file(cid, file_name_)

        return cid, size

    def _pin_file(self, ipfs_cid: str, filename: str) -> bool:
        """
        Pin file for some time via Web3 IPFS pinning service. This may help to spread the file wider across IPFS.

        :param ipfs_cid: Uploaded file cid.
        :param filename: A name you want to give to the file.

        :return: Server response flag.
        """

        if not self._keypair:
            raise NoPrivateKeyException("No seed was provided, unable to authenticate in Web3 Gateway service .")

        if len(ipfs_cid) != 46 or not ipfs_cid.startswith("Qm"):
            raise InvaliIdPFSCIDFormat("Invalid IPFS cid format!")

        body = {"cid": ipfs_cid, "name": filename}

        response = requests.post(
            W3PS,
            auth=(f"sub-{self._keypair.ss58_address}", f"0x{self._keypair.sign(self._keypair.ss58_address).hex()}"),
            json=body,
        )

        if response.status_code == 200:
            return True
        else:
            raise FailedToPinFile(response.status_code)
