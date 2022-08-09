#crust-file-uploader

This is a simple tool to upload your files to a Crust network.

## Setup

#### For Rocky Testnet
- create an account on [Crust Rocky Testnet](https://apps.crust.network/?rpc=wss%3A%2F%2Frpc-rocky.crust.network#/explorer)
- ask for tokens in [faucet](https://discord.gg/d6XuBXCqxU)

### Installation:
```bash
git clone https://github.com/PaTara43/crust-file-uploader/
cd crust-file-uploader
pip3 istall .
```

## Features

- Check account balance with `get_balance`
- Calculate file storage cost with `get_appx_store_price`
- Upload files to IPFS through web3 gateway with `upload_file_w3gw`
- Store file with `store_file`
- Add renewal balance with `add_renewal_pool_balance`
- Check replicas with `get_replicas` !! # Not supported yet due to decoder issues
- Check docstrings for additional info!