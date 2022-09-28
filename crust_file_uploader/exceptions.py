class NoPrivateKeyException(Exception):
    """
    No private key was provided so unable to perform any operations requiring message signing.

    """

    pass


class FailedToUploadFile(Exception):
    """
    Failed to upload a file to Crust Network.
    """

    pass


class FailedToPinFile(Exception):
    """
    Failed to upload a file to Crust Network.
    """

    pass


class InvaliIdPFSCIDFormat(Exception):
    """
    Invalid IPFS cid format. The right example: QmZ4tDuvesekSs4qM5ZBKpXiZGun7S2CYtEZRB3DYXkjGx.
    """

    pass
