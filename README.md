# crust-file-uploader

https://crust.network/
https://apps.crust.network/
https://wiki.crust.network/en
https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Frpc-shadow.crust.network%2F#/explorer

This is a simple tool to upload your files to a Crust network.

## Setup
### Installation:
```bash
git clone https://github.com/PaTara43/crust-file-uploader/
cd crust-file-uploader
pip3 install .
```

## Features

The module is divided into `Mainnet` and `Shadow`

`Mainnet` provides Crust interaction functionality to check user balance, calculate file storage price, placing
file storage order, add tokens to renewal pool and checking replicas count.

`Shadow` allows you to perform `Xstorage` extrinsic in Crust Shadow network.