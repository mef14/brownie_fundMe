from brownie import FundMe, network, accounts, config
from scripts.helpful_scripts import get_account,get_priceFeed

def deploy_FundMe():
    # choose account to operate from
    my_account = get_account()
    # deploy contract
    fund_me = FundMe.deploy(get_priceFeed(),{"from": my_account},
    publish_source=config["networks"][network.show_active()]["verify"])
    return fund_me

def main():
    deploy_FundMe()