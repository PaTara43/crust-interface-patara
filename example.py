from crust_file_uploader import upload_file

ipfs_hash: str = upload_file(
    "sample_file.txt",
    "<seed>",
    test_network=True,
)

print(ipfs_hash)
