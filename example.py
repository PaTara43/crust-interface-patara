from crust_file_uploader import CrustUploader, Endpoints

tester_seed = "<seed>"

file_uploader = CrustUploader(seed=tester_seed, remote_ws=Endpoints.Testnet)

print(file_uploader.get_balance())
price = file_uploader.get_appx_store_price(35*1024)
print(price)
print(file_uploader.store_file("QmanD3QhdJMwxgqRFAeHX4nTTKh2dgD6ZExeJkca7GkGZB", 35*1024))
# One more 6 months
print(file_uploader.add_renewal_pool_balance("QmanD3QhdJMwxgqRFAeHX4nTTKh2dgD6ZExeJkca7GkGZB", price))
# Not supported yet due to decoder issues
print(file_uploader.get_replicas("QmanD3QhdJMwxgqRFAeHX4nTTKh2dgD6ZExeJkca7GkGZB"))
