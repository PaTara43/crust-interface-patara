import typing as tp

from substrateinterface import SubstrateInterface, Keypair

from .constants import CRUST_SS_58_FORMAT, CRUST_TYPE_REGISTRY_PRESET


def create_keypair(seed: str) -> Keypair:
    """
    Create a keypair for further use.

    :param seed: Account seed (mnemonic or raw) as a key to sign transactions.

    :return: A Keypair instance used by substrate to sign transactions.

    """

    if seed.startswith("0x"):
        return Keypair.create_from_seed(seed_hex=hex(int(seed, 16)), ss58_format=CRUST_SS_58_FORMAT)
    else:
        return Keypair.create_from_mnemonic(seed, ss58_format=CRUST_SS_58_FORMAT)


def extrinsic(
    remote_ws: str, keypair: Keypair, call_module: str, call_function: str, params: tp.Optional[dict] = None
) -> tp.Tuple[str, str]:
    """
    Submit an extrinsic in Crust Network.

    :param remote_ws: Crust Mainnet|Testnet|Shadow.
    :param keypair: Account keypair created with seed.
    :param call_module: Call module.
    :param call_function: Call function.
    :param params: Call params.

    :return: transaction hash, block_num-event_idx.

    """

    interface: SubstrateInterface = SubstrateInterface(
        url=remote_ws,
        ss58_format=CRUST_SS_58_FORMAT,
        type_registry_preset=CRUST_TYPE_REGISTRY_PRESET
    )

    call = interface.compose_call(call_module=call_module, call_function=call_function, call_params=params)
    signed_extrinsic = interface.create_signed_extrinsic(call=call, keypair=keypair)
    receipt = interface.submit_extrinsic(signed_extrinsic, wait_for_finalization=True)
    block_num: int = interface.get_block_number(receipt.block_hash)

    return receipt.extrinsic_hash, f"{block_num}-{receipt.extrinsic_idx}"


def query(
    remote_ws: str, storage_module: str, storage_function: str, params: tp.Union[list, str, int, None] = None
) -> tp.Any:
    """
    Perform a query to a Crust Network.

    :param remote_ws: Crust Mainnet|Testnet|Shadow.
    :param storage_module: Storage module.
    :param storage_function: Storage function.
    :param params: Query params.

    :return: Query result.

    """

    interface: SubstrateInterface = SubstrateInterface(
        url=remote_ws,
        ss58_format=CRUST_SS_58_FORMAT,
        type_registry_preset=CRUST_TYPE_REGISTRY_PRESET,
    )

    return interface.query(storage_module, storage_function, [params] if params else None)
