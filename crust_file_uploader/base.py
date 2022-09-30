import typing as tp

from substrateinterface import SubstrateInterface, Keypair, KeypairType

from .constants import CRUST_SS_58_FORMAT, CRUST_MAINNET_ENDPOINT, CRUST_SHADOW_ENDPOINT, CRUST_ROCKY_TESTNET_ENDPOINT
from .decorators import check_interface_opened


class Base:
    """
    Base class with basic functionality for Crust interfaces
    """

    def __init__(self, chain: str = "shadow", seed: tp.Optional[str] = None, crypto_type: int = KeypairType.SR25519):
        """
        Accept basic information for interacting with Crust interfaces.

        :param chain: Chain to work with: shadow, mainnet or rocky.
        :param seed: User seed (needed to sign storage transactions).
        :param crypto_type: Account KeypairType.

        """

        if seed:
            self.keypair: Keypair = self.create_keypair(seed, crypto_type)
        else:
            self.keypair = None

        if chain == "shadow":
            self.remote_ws = CRUST_SHADOW_ENDPOINT
        elif chain == "mainnet":
            self.remote_ws = CRUST_MAINNET_ENDPOINT
        elif chain == "rocky":
            self.remote_ws = CRUST_ROCKY_TESTNET_ENDPOINT
        else:
            raise ValueError("Invalid chain name. Choose from [shadow, mainnet, rocky].")

        self.interface: tp.Optional[SubstrateInterface] = None

    @staticmethod
    def create_keypair(seed: str, crypto_type: int = KeypairType.SR25519) -> Keypair:
        """
        Create a keypair for further use.

        :param seed: Account seed (mnemonic or raw) as a key to sign transactions.
        :param crypto_type: Account crypto_type.

        :return: A Keypair instance used by substrate to sign transactions.

        """

        if seed.startswith("0x"):
            return Keypair.create_from_seed(
                seed_hex=hex(int(seed, 16)), ss58_format=CRUST_SS_58_FORMAT, crypto_type=crypto_type
            )
        else:
            return Keypair.create_from_mnemonic(seed, ss58_format=CRUST_SS_58_FORMAT, crypto_type=crypto_type)

    @check_interface_opened
    def extrinsic(self, call_module: str, call_function: str, params: tp.Optional[dict] = None) -> tp.Tuple[str, str]:
        """
        Submit an extrinsic in Crust Network.

        :param call_module: Call module.
        :param call_function: Call function.
        :param params: Call params.

        :return: transaction hash, block_num-event_idx.

        """

        call = self.interface.compose_call(call_module=call_module, call_function=call_function, call_params=params)
        signed_extrinsic = self.interface.create_signed_extrinsic(call=call, keypair=self.keypair)
        receipt = self.interface.submit_extrinsic(signed_extrinsic, wait_for_finalization=True)
        block_num: int = self.interface.get_block_number(receipt.block_hash)

        return receipt.extrinsic_hash, f"{block_num}-{receipt.extrinsic_idx}"

    @check_interface_opened
    def query(
        self, storage_module: str, storage_function: str, params: tp.Union[list, str, int, None] = None
    ) -> tp.Any:
        """
        Perform a query to a Crust Network.

        :param storage_module: Storage module.
        :param storage_function: Storage function.
        :param params: Query params.

        :return: Query result.

        """

        return self.interface.query(storage_module, storage_function, [params] if params else None)
