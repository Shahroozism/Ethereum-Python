from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/9549dc6e7edb45469d57d8d8d5c78ef8"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected)

print(web3.eth.blockNumber)

#insert MetaMask account info in the quotes

balance = web3.eth.getBalance("")
print(web3.fromWei(balance, "ether"))
