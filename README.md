#crust-file-uploader

This is a simple tool to upload your files to a Crust network.

## Setup

### Prerequisites
- nvm [installation](https://github.com/nvm-sh/nvm#installing-and-updating)
- `node` >= 15 (update with `nvm install node`)
- `yarn` (install with `sudo npm install --global yarn`)
#### For Rocky Testnet
- create an account on [Crust Rocky Testnet](https://apps.crust.network/?rpc=wss%3A%2F%2Frpc-rocky.crust.network#/explorer)
- ask for tokens in [faucet](https://discord.gg/d6XuBXCqxU)

### Installation:
```bash
git clone https://github.com/PaTara43/crust-file-uploader/
cd crust-file-uploader
# rn you have to manually go and install Node dependencies via
cd crust_file_uploader/js_src
yarn
cd ../..
# I promise to add automation in setup.py in future:) 
pip3 istall .
```

## Run

```python
from crust_file_uploader import upload_file

upload_file(
    "sample_file.txt",
    "<seed>",
    test_network=True,
) ## -> IPFS hash of the uploaded file
```