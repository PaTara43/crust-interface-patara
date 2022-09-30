from crust_file_uploader import Shadow
from robonomicsinterface.utils import ipfs_upload_content

seed = "seed"
shadow = Shadow(seed=seed)

# Read file
file_path = "file_path"
with open(file_path, "rb") as f:
    content = f.read()

# Upload file to IPFS
cid, size = ipfs_upload_content(seed=seed, content=content)
print(cid, size)

# Check balance
balance = shadow.get_balance()
print(balance)

# Store file in Shadow for CSMs
file_stored = shadow.store_file(cid, size)
print(file_stored)