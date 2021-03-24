import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545" # Node Address
web3 = Web3(Web3.HTTPProvider(ganache_url)) 

wallet_1 = '0xdf9C0dA60D2d35bf8546b5D678A94387383507a4' # Wallet Account 1 Sender 
wallet_2 = '0x48C8e7f6bfB9C34302030121709dbBa6Af536A7C' # Wallet Account 2 Recipient 

private_key = 'b178fb9281515157e5fc0c1bd18a1b2fd15e673cbc14d03a838effb71c42e8b2' # Ganache key for transaction signing i.e confirming 

nonce = web3.eth.getTransactionCount(wallet_1) # nonce or not a nonsense number, prevents double-spend 

tx = {
    'nonce': nonce,
    'to': wallet_2,
    'value': web3.toWei(1, 'ether'), # Value of ether transferred in the transaction
    'gas': 2000000, # gas price or amount of wei burned per transaction
    'gasPrice': web3.toWei('50', 'gwei'), 
}

signed_tx = web3.eth.account.signTransaction(tx, private_key) # Sign transaction with private key to confirm transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction) # Sends raw transaction to network and returns a transaction hash
print(web3.toHex(tx_hash)) # Hash to hex conversion to display to console