from logging import getLogger
from Naked.toolshed.shell import muterun_js
from pathlib import Path

from .constants import W3GW, CRUST_MAINNET_ENDPOINT, CRUST_ROCKY_TESTNET_ENDPOINT
from .exceptions import FailedToUploadFile

logger = getLogger(__name__)


def upload_file(file_path: str, crust_seeds: str, test_network: bool = False, ipfs_w3gw: str = W3GW) -> str:
    """
    Upload a file to a Crust Network.

    :param file_path: Path to a file to be stored in Crust Network.
    :param crust_seeds: Crust account seed.
    :param test_network: Whether to use Rocky testnet or not.
    :param ipfs_w3gw: Web# IPFS gateway address.

    :return: IPFS hash of the uploaded file.

    """

    response = muterun_js(
        f"{Path(__file__).parent.resolve()}/js_src/upload.js",
        f"{CRUST_ROCKY_TESTNET_ENDPOINT if test_network else CRUST_MAINNET_ENDPOINT} "
        f"'{crust_seeds}' "
        f"{Path(file_path).resolve()} "
        f"{ipfs_w3gw}",
    )
    if response.exitcode == 0:
        resp: str = response.stdout.decode("utf-8")
        logger.info(resp)
        qm_pos: int = resp.find("Qm")
        return resp[qm_pos:qm_pos+46]

    else:
        logger.error(response.stderr.decode("utf-8"))
        raise FailedToUploadFile("Failed to upload a file to Crust Network.")
