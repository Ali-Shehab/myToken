from brownie import accounts, network , config 

DECIMALS = 8
STARTING_PRICE = 200000000000       

LOCAL_BLOCKCHAIN = ["ganache-local","development"]
FORKED_BLOCKCHAIN = ["mainnet-fork-dev"]
def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN or network.show_active() in FORKED_BLOCKCHAIN): 
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])

