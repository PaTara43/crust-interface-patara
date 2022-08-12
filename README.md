# crust-file-uploader

https://crust.network/
https://apps.crust.network/
https://wiki.crust.network/en

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

The module is divided into `UploaderMainnet`, `UploaderShadow` and `Web3Gateway`

`Web3Gateway` allows you to upload files to IPFS via Web3-authenticate gateway.

`UploaderMainnet` provides Crust interaction functionality to check user balance, calculate file storage price, placing
file storage order, add tokens to renewal pool and checking replicas count.

`UploaderShadow` allows you to perform `xstorage` extrinsic in Crust Shadow network (Not possible yet due to wasm issue)