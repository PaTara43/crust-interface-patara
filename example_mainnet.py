import time

from crust_file_uploader import Mainnet
from robonomicsinterface.utils import ipfs_upload_content

seed = "seed"
mainnet = Mainnet(seed=seed)

# Read file
file_path = "file_path"
with open(file_path, "rb") as f:
    content = f.read()

# Upload file to IPFS
cid, size = ipfs_upload_content(seed=seed, content=content)
print(cid, size)

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
