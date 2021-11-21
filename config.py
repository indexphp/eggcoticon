"""
Fill in your information in the configuration variables below
"""

traits = [
    "Background", 
    "Shape",
    "Emotion",
    "Topping",
    "Sauce"
] # The different layers and the order that they will be used - MUST be same as trait layer folders
imageCount = 15000 # Total number of images to create
nameFormat = "Eggcoticon #[NUMBER]" # The name of each NFT - '[NUMBER]' will be replaced with the NFT number
description = "15,000 unique Eggcoticons are stored as ERC-721 tokens on the Ethereum compatible Polygon network. All Eggcoticons are hosted on IPFS. For more info, visit https://eggcoticon.nft" # Description of collection
royalty = 10 # Royalty percentage
royaltyAddress = "0xDF0Bc0C493442E3d0cd45D5BD47667eadf9741aC" # Address to pay the royalties to
collectionName = "Eggcoticon" # Name of collection
collectionFamily = "Eggcoticon" # Name of family (often same as collection)
symbol = "EGG" # Symbol (often blank)
blockchain = "ETH" # ETH or SOL