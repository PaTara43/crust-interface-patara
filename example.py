from crust_file_uploader import UploaderMainnet, UploaderShadow, Web3Gateway

tester_tokens_seed = "<seed>"

shadow = UploaderShadow(seed=tester_tokens_seed)
mainnet = UploaderMainnet()
w3gw = Web3Gateway(tester_tokens_seed)

file_path = "<path/to/file>"

# Upload file to IPFS
cid, size = w3gw.upload_file(file_path, pin=True)
print(cid, size)

# Check balance
balance = shadow.get_balance()
print(balance)

# Check price in Main net. Price in pCRUs
price = mainnet.get_appx_store_price(size)
print(price)

# Store file in Shadow for CSMs
file_stored = shadow.store_file(cid, size)
print(file_stored)

# Check balance again
balance = shadow.get_balance()
print(balance)

# This is for CRUs
file_prepaid = mainnet.add_renewal_pool_balance(cid, price*2)
print(file_prepaid)

# This is in Crust Main net
replicas = mainnet.get_replicas(cid)
print(replicas)
