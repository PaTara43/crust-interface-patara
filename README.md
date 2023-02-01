# crust-file-uploader

https://crust.network/
https://apps.crust.network/
https://wiki.crust.network/en
https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Frpc-shadow.crust.network%2F#/explorer

This is a simple tool to pin your files sing Crust Network or Crust Shadow.

## Setup
### Installation:
```bash
pip3 install crust-interface-patara
```

## Features

The module is divided into `Mainnet` and `Shadow`

`Mainnet` provides Crust interaction functionality to check user balance, calculate file storage price, placing
file storage order, add tokens to renewal pool and checking replicas count.

```python
import time
from crustinterface import Mainnet

seed = "seed"
mainnet = Mainnet(seed=seed)

# get any IPFS CID and size
cid, size =  "QmbJtyu82TQSHU52AzRMXBENZGQKYqPsmao9dPuTeorPui", 18  # <any way to get an IPFS CID and size. One may use ipfshttpclient2 from IPFS-Toolkit>

# Check balance
balance = mainnet.get_balance()
print(balance)

# Check price in Main net. Price in pCRUs
price = mainnet.get_appx_store_price(int(size))
print(price)

# Store file in Mainnet for CRUs
file_stored = mainnet.store_file(cid, size)
print(file_stored)

# Add renewal pool
file_prepaid = mainnet.add_renewal_pool_balance(cid, price*2)
print(file_prepaid)


# Get replicas
time.sleep(10)
replicas = mainnet.get_replicas(cid)
print(replicas)

```

`Shadow` allows you to perform `Xstorage` extrinsic in Crust Shadow network.
```python
from crustinterface import Shadow
seed = "seed"
shadow = Shadow(seed=seed)

# get any IPFS CID and size
cid, size =  "QmbJtyu82TQSHU52AzRMXBENZGQKYqPsmao9dPuTeorPui", 18  # <any way to get an IPFS CID and size. One may use ipfshttpclient2 from IPFS-Toolkit>

print(cid, size)

# Check balance
balance = shadow.get_balance()
print(balance)

# Store file in Shadow for CSMs
file_stored = shadow.store_file(cid, size)
print(file_stored)
```
