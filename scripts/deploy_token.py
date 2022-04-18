import imp
from brownie import MyToken, accounts
from scripts.used_functions import (get_account,)
from web3 import Web3


intial_supply = Web3.toWei(1000,"ether")

def main():
    account = get_account()
    my_token = MyToken.deploy(intial_supply,{"from":account})
    print(my_token.name())