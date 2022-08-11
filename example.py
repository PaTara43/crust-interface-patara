from crust_file_uploader import UploaderMainnet, Endpoints

tester_tokens_seed = "<seed>"

file_uploader = UploaderMainnet(seed=tester_tokens_seed, remote_ws=Endpoints.Testnet)
file_path = "../file.extension"

cid, size = file_uploader.upload_file_w3gw(file_path, pin=True)
print(cid, size)

balance = file_uploader.get_balance()
print(balance)
price = file_uploader.get_appx_store_price(size)
print(price)
file_stored = file_uploader.store_file(cid, size)
print(file_stored)
file_prepaid = file_uploader.add_renewal_pool_balance(cid, price*2)
print(file_prepaid)
# replicas = file_uploader.get_replicas(cid)
# print(replicas)
# Not possible yet due to type_registry issue.
