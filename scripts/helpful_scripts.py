from brownie import network,accounts,config,MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-desktop"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.load("my_metamask_dev")

# get chainlink price feed address for the network I am depolying on
# or mock chainlink on development network
def get_priceFeed():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return config["networks"][network.show_active()]["eth_usd_priceFeed"]
    else:
        print("Deploying mock oracle...")
        mock_v3_aggregator = MockV3Aggregator.deploy(18,Web3.toWei(2000,"ether"),{"from": get_account()})
        print("Deployed!")
        return mock_v3_aggregator.address