# Introduction

Taking inspiration from Hashlips' great work, this software was born with the aim of providing an NFT generation framework for the Solana network. It allows granular control over item rarity and probability of occurring and more control over the resulting combinations.
<br>This is achieved through a user-friendly interface that only leverages Python data structures.

With it, you'll easily be able to:

- create a detailed configuration of how your NFT should be generated
- efficiently build images regardless of the numbers of layers
- create metadata for the Solana network
- create rarity reports

# Installation

Simply run in your Python 3.7+ interpreter

`git clone https://github.com/andrea-dagostino/2cool4skull_nft_generator.git`

In the project directory, run
`pip install -r requirements.txt`

You only need Pillow installed, version 9.0.1. All other libs used belong to the standard Python lib.

# How does it work?

The first step is to create a `layers` folder in root. In here, drop in your layers that contain your .png files.
Then all you need to do is fill in the `./src/config.py` file and launch `run.py`. The software will take care of the rest.

The `config.py` contains several dictionaries that can be manipulated to control:

- project settings on the Solana network
- layer number and their names
- define rarity classes within each layer and their probability of occurrence
- define exclusions among items

## Project settings

The software will build the metadata according to the Non-Fungible Token Metadata Standard (http://docs.metaplex.com/token-metadata/specification) - just fill in the following dictionary to define this information.

```python
SOL_PROJECT_METADATA = {
    "name": "2cool4skull",
    "symbol": "2c4s",
    "description": "Skullinos shine in the dark!",
    "seller_fee_basis_points": 1000,  # 10%
    "external_url": "https://2cool4skull.xyz/",  # remember to add trailing slash
    "creators": [
        {"address": "<your_wallet_address>", "share": 100}
    ],
    # "collection": {"name": "2cool4skull", "family": "2cool4skull"} # soon to be deprecated?
}
```

## Layer settings

This portion of the configuration is very similar to Hashlip's software and therefore you'll feel at home. Simply associate to the "Layer\<id>" key to the name you wish to give to your layer. Always remember to order your layers from background to foreground.

```python
# order your layers from background to foreground
LAYER_ORDER = {
    "Layer1": "Background",
    "Layer2": "<layer2_name>",
    "Layer3": "<layer3_name>",
    ...
}
```

## NFT generation logic

The most important settings are declared in the `SETUP` variable. This dictionary has the following structure:

- Layer
  - name of layer
  - item scheme
    - _rarity_class_
      - items
      - probability of rarity class
      - optional unique and special items

```python
SETUP = {
    # define layer data
    "Layer1": {
        "name": "Background",
        # define rarity classes, items belonging to classes and probabilities
        # together with special items and their probability of appearing
        "scheme": {
            "Legendary": { # define rarity class name (it can be any you want)
                "items": ["<item1>", "<item2>", "<item3>"], # create a list of legendary items
                "p": 0.1, # with 10% probability of occurring
                "unique_items": {"<item1>": 0.20}, # and define a list of unique items and their probability (read details below)
            },
            "Epic": {
                ...
            },
            "Rare": {
                ...
            },
        },
    },
    "Layer2": {
        "name": "<layer2_name>",
        ...
}
```

### How does probability for special/unique items work?

Each item in `rarity_class: items` has the same probability of occurring as defined by the `p` key. Items placed in the `unique_items` list follow this formula:

`probability_of_special_item` = `base_probability` \* `special_item_probability`

`base_probability` is the constant probability of the items in the list, and it is very simple to compute:

`base_probability` = 1 / `number_of_items`

For example, if a list of made up of 4 items, **each item will occur with a 25% chance**. Let's say that our special item is the first one in the list. <br><br>**By setting it's probability in the dedicated dict key, you will multiply the default 25% of that item by the new value set in the dict key.**
So if the probability of the special item is 10%, then 25% \* 10% = 2.5%.
Be sure to double check your math here, it can screw up the experience for your customers!

## Exclusion logic

Sometimes you might want to exclude some items to occur with others. This could be for several reasons, such as special items not being graphically compatible with other, regular items. Simply fill in the following template.

```python
EXCLUDE_COMBINATIONS = [
    {
        "<layer>": {
            "item": "<item>",
            "with": [
                {"<layer>": "<item_A>"},
                {"<layer>": "<item_B>"},
            ],
        },
    ...
    }
```

# How to create your NFTs

Once the `config.py` file is filled in, you are ready to create your NFTs.<br>
Place your layers in the `./assets/` folder and open `./src/run.py`.

```python
if __name__ == "__main__":
    from src.utils import *

    create_nfts(n_samples=1000) # edit the number here to control the number of NFTs to create.
```

In `create_nfts` you can also pass _`start_from`_ (default is 0) to control enumeration (if you want to add items to your collection with a different logic for instance). If you do so, make sure to also change the total number of NFTs to create so as to match the added values and the total.

Then in your terminal run `python run.py`. This will create a `collection` folder with images and metadata and rarity reports.

## Rarity reports

Rarirt reports give you information on how classes and items are distributed in your collection. They are useful debugging tool.

`overall_rarity.json` provides a ranking (highest --> rarest) of the rarity of your NFTs. <br>
`rarity_report.json` provides information on class and item distribution.

_these files' names will change in later releases._

# Credits

@HashLips - His work for this community is outstanding, and served as a solid base for this project.
