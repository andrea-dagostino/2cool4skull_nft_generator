SOL_PROJECT_METADATA = {
    "name": "2cool4skull",
    "symbol": "2c4s",
    "description": "Little skullinos shine in the dark!",
    "seller_fee_basis_points": 1000,  # 10%
    "external_url": "https://2cool4skull.com/",  # remember to add trailing slash
    "creators": [
        {"address": "<your_wallet_address>", "share": 100}
    ],
    # "collection": {"name": "2cool4skull", "family": "2cool4skull"}
}

# order your layers from background to foreground
LAYER_ORDER = {
    "Layer1": "Background",
    "Layer2": "Head",
    "Layer3": "Clothing",
    "Layer4": "Wings",
    "Layer5": "Mouth",
    "Layer6": "Eyes",
    "Layer7": "Head accessory",
}

# define here the configuration of our project
SETUP = {
    # define layer data
    "Layer1": {
        "name": "Background",
        # define rarity classes, items belonging to classes and probabilities
        # together with unique items and their probability of appearing
        "scheme": {
            "Legendary": {
                "items": ["Hypno", "Hypno BW", "Rainbow melted"],
                "p": 0.1,
                "unique_items": {},
            },
            "Epic": {
                "items": [
                    "Day sky",
                    "Flames",
                    "Night sky",
                    "Rainbow circles",
                    "Rainbow wave",
                    "Space",
                ],
                "p": 0.25,
                "unique_items": {},
            },
            "Rare": {
                "items": ["Pink green", "Purple Pink", "Yellow blue"],
                "p": 0.30,
                "unique_items": {},
            },
            "Common": {
                "items": ["Blue", "Red", "Green", "Purple", "Pink", "Yellow"],
                "p": 0.35,
                "unique_items": {},
            },
        },
    },
    "Layer2": {
        "name": "Head",
        "scheme": {
            "Legendary": {
                "items": ["Triangled G", "Squared G", "Rounded G"],
                "p": 0.1,
                "unique_items": {},
            },
            "Epic": {
                "items": ["Triangled Y", "Squared Y", "Rounded Y"],
                "p": 0.25,
                "unique_items": {},
            },
            "Rare": {
                "items": ["Triangled B", "Squared B", "Rounded B"],
                "p": 0.30,
                "unique_items": {},
            },
            "Common": {
                "items": ["Triangled W", "Squared W", "Rounded W"],
                "p": 0.35,
                "unique_items": {},
            },
        },
    },
    "Layer3": {
        "name": "Clothing",
        "scheme": {
            "Legendary": {
                "items": ["DBZ", "HP", "Armor"],
                "p": 0.1,
                "unique_items": {},
            },
            "Epic": {
                "items": [
                    "Rainbow hoodie",
                    "Rainbow shirt",
                    "Bomber rainbow",
                    "Vking",
                    "Sweater G",
                ],
                "p": 0.25,
                "unique_items": {},
            },
            "Rare": {
                "items": [
                    "Multi color shirt",
                    "Bomber P B",
                    "Bomber V Y",
                    "Leather jacket",
                    "Kimono",
                    "Smoking",
                    "Sweater R",
                ],
                "p": 0.30,
                "unique_items": {},
            },
            "Common": {
                "items": [
                    "Black hoodie",
                    "Hoodie V",
                    "Tank top",
                    "Office shirt",
                    "Santa",
                ],
                "p": 0.35,
                "unique_items": {},
            },
        },
    },
    "Layer4": {
        "name": "Wings",
        "scheme": {
            "Legendary": {
                "items": ["Angel", "Demon", "Dark angel", "Devil tail", "Fairy"],
                "p": 0.05,
                "unique_items": {},
            },
            "Epic": {"items": [], "p": 0, "unique_items": {}},
            "Rare": {"items": [], "p": 0, "unique_items": {}},
            "Common": {"items": ["None"], "p": 0.95, "unique_items": {}},
        },
    },
    "Layer5": {
        "name": "Mouth",
        "scheme": {
            "Legendary": {
                "items": [
                    "Big golden smile",
                    "Big rainbow smile",
                    "Default rainbow",
                    "Rainbow",
                ],
                "p": 0.1,
                "unique_items": {},
            },
            "Epic": {
                "items": ["Clouds bandana", "Monster", "Rainbow bandana", "Vampire"],
                "p": 0.25,
                "unique_items": {},
            },
            "Rare": {
                "items": [
                    "Teeth",
                    "Tongue",
                    "Bubblegum",
                    "Cigarette",
                    "Lipstick",
                    "Big smile",
                ],
                "p": 0.30,
                "unique_items": {},
            },
            "Common": {
                "items": [
                    "Scared",
                    "Open",
                    "Grr",
                    "Dumb",
                    "Shocked",
                    "Smile",
                    "Default",
                    "Big smile v2",
                ],
                "p": 0.35,
                "unique_items": {},
            },
        },
    },
    "Layer6": {
        "name": "Eyes",
        "scheme": {
            "Legendary": {
                "items": ["Triclop", "Third eye", "Laser rainbow"],
                "p": 0.1,
                "unique_items": {},
            },
            "Epic": {
                "items": [
                    "Cyclop",
                    "Laser red",
                    "Cyborg",
                    "3d",
                    "Post it happy",
                    "Post it sad",
                ],
                "p": 0.25,
                "unique_items": {},
            },
            "Rare": {
                "items": [
                    "Sunglasses",
                    "Flames",
                    "Stars",
                    "Hearts",
                    "Oval glasses",
                    "Spirals",
                    "Shine",
                ],
                "p": 0.30,
                "unique_items": {},
            },
            "Common": {
                "items": [
                    "Angry",
                    "Bored",
                    "Default",
                    "Sad",
                    "UU",
                    "HP",
                    "Eyelids",
                    "50s",
                ],
                "p": 0.35,
                "unique_items": {},
            },
        },
    },
    "Layer7": {
        "name": "Head accessory",
        "scheme": {
            "Legendary": {
                "items": [
                    "DBZ",
                    "HP",
                    "Tengu mask",
                    "Unicorn",
                    "Vader mask",
                    "Gas mask",
                ],
                "p": 0.1,
                "unique_items": {
                    "Tengu mask": 0.20,
                    "Vader mask": 0.20,
                    "Gas mask": 0.20,
                },
            },
            "Epic": {
                "items": [
                    "Punk",
                    "Rainbow hat",
                    "Horns",
                    "Brain",
                    "Angel",
                    "Arrow",
                    "Afro",
                ],
                "p": 0.25,
                "unique_items": {},
            },
            "Rare": {
                "items": [
                    "Karate band",
                    "Spacebuns",
                    "Vking",
                    "Blue hat",
                    "Party hat V Y",
                    "Violet beanie",
                ],
                "p": 0.30,
                "unique_items": {},
            },
            "Common": {
                "items": [
                    "Santa",
                    "Blue hat",
                    "Spikes",
                    "Party hat P G",
                    "Pink ponytail",
                    "Cowboy",
                    "Blonde",
                ],
                "p": 0.35,
                "unique_items": {},
            },
        },
    },
}


# define here the items that cannot occur together
EXCLUDE_COMBINATIONS = [
    {
        "Head accessory": {
            "item": "Tengu mask",
            "with": [
                {"Mouth": "Rainbow bandana"},
                {"Mouth": "Rainbow"},
                {"Mouth": "Clouds bandana"},
                {"Mouth": "Cigarette"},
                {"Eyes": "HP"},
                {"Eyes": "Laser rainbow"},
                {"Eyes": "Laser red"},
                {"Eyes": "Flames"},
                {"Eyes": "Stars"},
                {"Eyes": "3d"},
                {"Eyes": "Sunglasses"},
            ],
        },
        "Head accessory": {
            "item": "Vader mask",
            "with": [
                {"Mouth": "Rainbow bandana"},
                {"Mouth": "Rainbow"},
                {"Mouth": "Clouds bandana"},
                {"Mouth": "Cigarette"},
                {"Eyes": "HP"},
                {"Eyes": "Laser rainbow"},
                {"Eyes": "Laser red"},
                {"Eyes": "Flames"},
                {"Eyes": "Stars"},
                {"Eyes": "3d"},
                {"Eyes": "Sunglasses"},
            ],
        },
        "Head accessory": {
            "item": "Gas mask",
            "with": [
                {"Mouth": "Rainbow bandana"},
                {"Mouth": "Rainbow"},
                {"Mouth": "Clouds bandana"},
                {"Mouth": "Cigarette"},
                {"Eyes": "HP"},
                {"Eyes": "Laser rainbow"},
                {"Eyes": "Laser red"},
                {"Eyes": "Flames"},
                {"Eyes": "Stars"},
                {"Eyes": "3d"},
                {"Eyes": "Sunglasses"},
            ],
        },
        "Eyes": {
            "item": "Ciclop",
            "with": [{"Head accessory": "Karate band"}, {"Head accessory": "DBZ"}],
        },
        "Eyes": {
            "item": "Triclop",
            "with": [{"Head accessory": "Karate band"}, {"Head accessory": "DBZ"}],
        },
        "Eyes": {
            "item": "Flames",
            "with": [{"Head accessory": "HP"}, {"Head accessory": "DBZ"}],
        },
    }
]