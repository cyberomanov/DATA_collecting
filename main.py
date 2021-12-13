from web3.auto import Web3
import time

# dictionary "public_key": "private_key"
donar_list = {
    "0x6F62xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxBD0668": "0x43xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd5f",
    "0x1aA7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx751dF8": "0x83xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx0e9",
    "0x58E6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxbe1F4b": "0x0axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx85a",
}

# recipient address
recipient = "0xfg36xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxbesfb"

# session generation
web = Web3(Web3.HTTPProvider("https://polygon-mainnet.infura.io/v3/<API>"))
ABI = [{"inputs":[{"internalType":"address","name":"initialBridgeAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"address","name":"owner","type":"address"},{"indexed":"true","internalType":"address","name":"spender","type":"address"},{"indexed":"false","internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":"true","internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":"true","internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":"true","internalType":"address","name":"account","type":"address"},{"indexed":"true","internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":"true","internalType":"address","name":"account","type":"address"},{"indexed":"true","internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"address","name":"from","type":"address"},{"indexed":"true","internalType":"address","name":"to","type":"address"},{"indexed":"false","internalType":"uint256","name":"value","type":"uint256"},{"indexed":"false","internalType":"bytes","name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"address","name":"from","type":"address"},{"indexed":"true","internalType":"address","name":"to","type":"address"},{"indexed":"false","internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":"false","inputs":[{"indexed":"false","internalType":"string","name":"newName","type":"string"},{"indexed":"false","internalType":"string","name":"newSymbol","type":"string"}],"name":"UpdatedTokenInformation","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bridgeAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"bytes","name":"depositData","type":"bytes"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"isMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newBridgeAddress","type":"address"}],"name":"setBridgeAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newName","type":"string"},{"internalType":"string","name":"newSymbol","type":"string"}],"name":"setTokenInformation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"transferAndCall","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]
contract = web.eth.contract(address="0x3a9A81d576d83FF21f26f325066054540720fC34", abi=ABI)

# loop
for public_key in donar_list:
    sender = public_key
    priv_key = donar_list[public_key]

    # getting DATA balance
    balanceDATA = contract.functions.balanceOf(sender).call()

    if balanceDATA > 0:

        # getting nonce
        nonce = web.eth.getTransactionCount(sender)

        # generating tx
        tx = contract.functions.transfer(
             recipient,
             balanceDATA,
         ).buildTransaction({
             'chainId': 137,
             'gas': 45000,
             'gasPrice': web.toWei('35', 'gwei'),
             'nonce': nonce,
         })

        # signing tx
        signed_tx = web.eth.account.signTransaction(tx, priv_key)

        # sending tx
        web.eth.sendRawTransaction(signed_tx.rawTransaction)
        transactionRaw = Web3.toHex(Web3.sha3(signed_tx.rawTransaction))
        print(f"{public_key}: sending DATA. tx: {transactionRaw}.")

        # waiting for transaction
        time.sleep(10)
    else:
        print(f"{public_key}: no DATA.")

    # getting free balance
    feePrice = 21000 * web.toWei(35, 'gwei')
    balanceMATIC = web.eth.getBalance(sender)
    freeToSend = balanceMATIC - feePrice

    if freeToSend > 0:

        # getting nonce
        nonce = web.eth.getTransactionCount(sender)

        # generating tx
        tx = {
            'nonce': nonce,
            'to': recipient,
            'value': freeToSend,
            'gas': 21000,
            'chainId': 137,
            'gasPrice': web.toWei(35, 'gwei')
        }

        # signing tx
        signed_tx = web.eth.account.signTransaction(tx, priv_key)

        # sending tx
        web.eth.sendRawTransaction(signed_tx.rawTransaction)
        transactionRaw = Web3.toHex(Web3.sha3(signed_tx.rawTransaction))
        print(f"{public_key}: sending MATIC. tx: {transactionRaw}.")

    else:
        print(f"{public_key}: no MATIC.")
   
    print("with love by @cyberomanov.")
