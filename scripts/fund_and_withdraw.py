from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    my_account = get_account()
    fund_me.fund({"from": my_account,"value": 10**18})

def withdraw():
    fund_me = FundMe[-1]
    my_account = get_account()
    fund_me.withdraw({"from": my_account})

def main():
    fund()
    withdraw()
    