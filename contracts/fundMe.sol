// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    
    AggregatorV3Interface public priceFeed;
    mapping(address => uint256) public addressToAmountFunded;
    address owner;

    constructor(address _priceFeed) {
        // connect with Chainlink on the right network
        priceFeed = AggregatorV3Interface(_priceFeed);
        // set contract's owner
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function fund() public payable {
        // require at least 100 USD of funding
        require(msg.value * getConversionRate(msg.value) >= 100 * 10 ** 18, "You need to send at least 100 USD worth of ETH");
        // map the sender of funds to the value funded
        addressToAmountFunded[msg.sender] += msg.value;
    }

    function withdraw() public onlyOwner payable {
        // transfer all funds in the contract to the contact's owner
        address payable payableOwner = payable(owner);
        payableOwner.transfer(address(this).balance);
    }

    function getEthPrice() public view returns(uint256) {
        // get the ETH price in USD from Chainlink (with 18 decimals)
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10 ** 10);
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256) {
        // get the USD value of any amount of ETH (wei) sent (with 18 decimals)
        uint256 ethPrice = getEthPrice();
        uint256 usdValue = (ethAmount * ethPrice) / (10 ** 18);
        return usdValue;
    }

}