from brownie import network, accounts, exceptions
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_FundMe
import pytest

def test_fund_and_withdraw():
    my_account = get_account()
    fund_me = deploy_FundMe()
    tx = fund_me.fund({"from": my_account, "value": 10 ** 17})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(my_account) == 10**17
    tx = fund_me.withdraw({"from": my_account})
    tx.wait(1)
    assert fund_me.balance() == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local blockchain environments")
    else:
        fund_me = deploy_FundMe()
        bad_actor = accounts[1]
        with pytest.raises(exceptions.VirtualMachineError):
            fund_me.withdraw({"from": bad_actor})
