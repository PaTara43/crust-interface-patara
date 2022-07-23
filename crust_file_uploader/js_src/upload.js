import fs from 'fs';
import path from 'path';
import { create } from 'ipfs-http-client';
import { ApiPromise, WsProvider } from '@polkadot/api';
import { typesBundleForPolkadot } from '@crustio/type-definitions';
import { Keyring } from '@polkadot/keyring';


const crustChainEndpoint = process.argv[2]
const crustSeeds = process.argv[3]
const filePath = process.argv[4]
const ipfsW3GW = process.argv[5]


const api = new ApiPromise({
    provider: new WsProvider(crustChainEndpoint),
    typesBundle: typesBundleForPolkadot,
});

main();

async function main() {
    // I. Upload file to IPFS
    const cid_size = await uploadIPFS(filePath, ipfsW3GW, crustSeeds)
    console.log(cid_size);

    // II. Place storage order
    await placeStorageOrder(cid_size.cid, cid_size.size);
}


async function uploadIPFS(filePath, ipfsW3GW, crustSeeds) {
    // 1. Read the file
    const fileContent = await fs.readFileSync(path.resolve(filePath));

    // 2. Create auth token for W3GW
    const keyring = new Keyring();
    const pair = keyring.addFromUri(crustSeeds);
    const sig = pair.sign(pair.address);
    const sigHex = '0x' + Buffer.from(sig).toString('hex');
    const authHeader = Buffer.from(`sub-${pair.address}:${sigHex}`).toString('base64');
    const ipfsRemote = create({
        url: `${ipfsW3GW}/api/v0`,
        headers: {
            authorization: `Basic ${authHeader}`
        }
    });

    // 3. Add file to IPFS via W3GW
    const cid_size = await addFile(ipfsRemote, fileContent);

    return cid_size

    };

async function addFile(ipfs, fileContent) {
    // 1. Add file to ipfs
    const cid = await ipfs.add(fileContent);

    // 2. Get file status from ipfs
    const fileStat = await ipfs.files.stat("/ipfs/" + cid.path);

    return {
        cid: cid.path,
        size: fileStat.cumulativeSize
    };
}

async function placeStorageOrder(fileCid, fileSize) {
    await api.isReadyOrError;

    // 1. Construct place-storage-order tx
    const tips = 0;
    const memo = '';
    const tx = api.tx.market.placeStorageOrder(fileCid, fileSize, tips, memo);

    // 2. Load seeds(account)
    const kr = new Keyring({ type: 'sr25519' });
    const krp = kr.addFromUri(crustSeeds);

    // 3. Send transaction

    return new Promise((resolve, reject) => {
        tx.signAndSend(krp, ({events = [], status}) => {
            if (status.isInBlock) {
                events.forEach(({event: {method, section}}) => {
                    if (method === 'ExtrinsicSuccess') {
                        console.log(`✅  Place storage order success!`);
                        resolve(true);
                    }
                });
            } else if (status.isFinalized) {
                console.log(`💸  Tx status: ${status.type}, nonce: ${tx.nonce}`);
                resolve(true);
                process.exit(0)
            } else {
                // Pass it
            }
        }).catch(e => {
            reject(e);
        })
    });
}