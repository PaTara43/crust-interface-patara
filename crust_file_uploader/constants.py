W3GW = "https://crustwebsites.net/api/v0/add"
W3PS = "https://pin.crustcode.com/psa/pins"
CRUST_ROCKY_TESTNET_ENDPOINT = "wss://rpc-rocky.crust.network"
CRUST_MAINNET_ENDPOINT = "wss://rpc.crust.network"
CRUST_SHADOW_ENDPOINT = "wss://rpc-shadow.crust.network/"
CRUST_TYPE_REGISTRY_PRESET = "crust"
CRUST_TYPE_REGISTRY = {
    "types": {
        "FileInfoV2": {
            "type": "struct",
            "type_mapping": [
                ["file_size", "u64"],
                ["spower", "u64"],
                ["expired_at", "BlockNumber"],
                ["calculated_at", "BlockNumber"],
                ["amount", "Balance"],
                ["prepaid", "Balance"],
                ["reported_replica_count", "u32"],
                ["remaining_paid_count", "u32"],
                ["replicas", "BTreeMap<AccountId, Replica<AccountId>>"]
            ]
        },
        "Replica": {
            "type": "struct",
            "type_mapping": [
                ["who", "AccountId"],
                ["valid_at", "BlockNumber"],
                ["anchor", "SworkerAnchor"],
                ["is_reported", "Bool"],
                ["created_at", "Option<BlockNumber>"]
            ]
        },
    }
}

CRUST_SS_58_FORMAT = 66
