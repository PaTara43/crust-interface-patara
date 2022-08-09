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