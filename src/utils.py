from PIL import Image
import shutil
import os

from src.config import (
    SOL_PROJECT_METADATA,
    SETUP,
    LAYER_ORDER,
    EXCLUDE_COMBINATIONS,
)
import json
import random
import hashlib
import time
from collections import Counter


def paste_layers(layer_order: list, chosen_items: list, id: int):
    """
    Superimposes layers to create an NFT image.

    Args:
        chosen_items (list): list of chosen items, in the same order of LAYER_ORDER
    """
    # read in items from layers folder
    pil_images = []
    for layer, item in zip(layer_order, chosen_items):
        img = Image.open(f"./layers/{layer}/{item}.png")
        pil_images.append(img)

    # create a blank image based on the background size
    nft = Image.new("RGB", (pil_images[0].width, pil_images[0].height))

    # superimpose layers
    for i, img in enumerate(pil_images):
        nft.paste(img, (0, 0), img)

    # save image
    # if folder doesn't exist, create it
    # if it does, overwrite destroy folder and create new one
    # if collection doesn't exist, create it
    # if it does, overwrite destroy folder and create new one
    if not os.path.exists("./collection"):
        os.mkdir("./collection")

    if not os.path.exists("./collection/images"):
        os.mkdir("./collection/images")
    nft.save(f"./collection/images/{id}.png")


def create_metadata(layers, chosen_items, id):
    """
    Creates metadata file for the project.
    """
    # copy project metadata
    metadata = {}
    attributes = []

    for layer, item in zip(layers, chosen_items):
        data = {"trait_type": layer, "value": item}
        attributes.append(data)

    metadata["name"] = SOL_PROJECT_METADATA["name"] + " #" + str(id + 1)
    metadata["symbol"] = SOL_PROJECT_METADATA["symbol"]
    metadata["description"] = SOL_PROJECT_METADATA["description"]
    metadata["seller_fee_basis_points"] = SOL_PROJECT_METADATA[
        "seller_fee_basis_points"
    ]
    metadata["image"] = str(id) + ".png"
    metadata["external_url"] = SOL_PROJECT_METADATA["external_url"]
    metadata["attributes"] = attributes
    metadata["properties"] = {
        "files": [
            {
                "uri": str(id) + ".png",
                "type": "image/png",
            }
        ]
    }
    metadata["creators"] = SOL_PROJECT_METADATA["creators"]

    # save metadata
    # if collection doesn't exist, create it
    # if it does, overwrite destroy folder and create new one
    if not os.path.exists("./collection"):
        os.mkdir("./collection")
        # if collection/metadata doesn't exist, create it
        # if it does, overwrite destroy folder and create new one
    if not os.path.exists("./collection/metadata"):
        os.mkdir("./collection/metadata")
    with open(f"./collection/metadata/{id}.json", "w") as f:
        json.dump(metadata, f)


def select_item(layer):
    """Selects class and items based on probability

    Args:
        layer (list): layer name specified in SETUP

    Returns:
        str: item name
    """
    classes = list(SETUP[layer]["scheme"].keys())
    classes_probabilities = [SETUP[layer]["scheme"][c]["p"] for c in classes]

    chosen_class = random.choices(classes, classes_probabilities)[0]

    # the probability of choosing a item is the same for all items in the class - create a list and store these probs
    base_item_probabilities = 1 / len(SETUP[layer]["scheme"][chosen_class]["items"])
    # append item_probabilities n times to create a list of probabilities
    item_probabilities = [base_item_probabilities] * len(
        SETUP[layer]["scheme"][chosen_class]["items"]
    )

    # if class contains a unique item, adjust probabilities
    if SETUP[layer]["scheme"][chosen_class]["unique_items"]:
        # get name of unique item
        unique_items = SETUP[layer]["scheme"][chosen_class][
            "unique_items"
        ]  # this contains item: probability
        # get the index of the unique item in the list of items
        for ui, prob in unique_items.items():
            idx = SETUP[layer]["scheme"][chosen_class]["items"].index(ui)
            item_probabilities[idx] = item_probabilities[idx] * prob

        chosen_item = random.choices(
            SETUP[layer]["scheme"][chosen_class]["items"], item_probabilities
        )[0]

    else:
        chosen_item = random.choice(SETUP[layer]["scheme"][chosen_class]["items"])

    # print(f"Seed: {rarity_seed} --> Layer: {SETUP[layer]['name']} --> Class: {classes[class_index]}, item: {chosen_item}")
    return chosen_item


def check_items(items_list):
    """Checks if combination is valid

    Args:
        items_list (list): list of items

    Returns:
        bool: True if valid, False otherwise
    """
    for entry in EXCLUDE_COMBINATIONS:
        for key, value in entry.items():
            if value["item"] in items_list:
                # if any of the items in the combination is in the "with" list, then the combination is invalid
                for blacklist in value["with"]:
                    for _, banned in blacklist.items():
                        if banned in items_list:
                            print(
                                f"Combination is invalid! Found {banned} in {value['item']}'s 'with' list!!!!"
                            )
                            return False
    return True


def assemble_nfts(layers):
    """Assembles items based on layer order

    Args:
        layers (list): list of layers

    Returns:
        list: list of items
    """
    items = []
    for layer in layers:
        items.append(select_item(layer))

    # check until combination is valid
    while not check_items(items):
        items = []
        for layer in layers:
            items.append(select_item(layer))

    return items


def create_genome(items_list):
    """Encodes the items_list into an encoded hash

    Args:
        items_list (list): items list output from assemble_nfts()

    Returns:
        str: hash of the items_list
    """
    stringified = ""
    for item in items_list:
        stringified += str(item)
    return hashlib.md5(stringified.encode()).hexdigest()


def create_nft(layer_dict: dict, id: int):
    """Basic aggregation function to create a NFT

    Args:
        layer_dict (dict): the list of ordered layers
        id (int): nft id

    Returns:
        str: dna of the nft
    """
    nft = assemble_nfts(layer_dict)
    dna = create_genome(nft)
    paste_layers(layer_order=layer_dict.values(), chosen_items=nft, id=id)
    create_metadata(layers=layer_dict.values(), chosen_items=nft, id=id)

    return dna


def create_nfts(n_samples, start_from=0):

    # THIS NEEDS MORE TESTING!!!!!!

    """Creates n_samples NFTs

    Args:
        n_samples (int): number of NFTs to create
    """
    if start_from != 0:
        remaining_samples = n_samples - start_from
        total = start_from + remaining_samples + 1
    else:
        if os.path.exists("./collection"):
            shutil.rmtree("./collection")
        total = n_samples

    if start_from > total:
        raise ValueError(
            f"n_samples must be greater than {start_from}! You specified {n_samples}"
        )

    # start timer
    start = time.time()
    dnas = set()

    for i in range(start_from, total):

        dna = create_nft(LAYER_ORDER, id=i)
        # if dna is already in set, retry
        while dna in dnas:
            previous_dna = dna
            print(f"Duplicate DNA found! {dna}")
            print("Retrying...")
            dna = create_nft(LAYER_ORDER, id=i)
            # remove the duplicate DNA from the set
            dnas.remove(previous_dna)

        dnas.add(dna)
        print(f"Created NFT #{i} with DNA {dna}")

    aggregate_metadata()
    create_rarity_report()

    # end timer
    end = time.time()
    # print out time in minutes
    print(f"Created {n_samples} NFTs in {round(((end - start) / 60), 2)} minutes")


def aggregate_metadata():
    """This function reads all metadata files in collection/metadata to create a single json file"""
    # if collection doesn't exist, create it
    # if it does, overwrite destroy folder and create new one
    if not os.path.exists("./collection"):
        os.mkdir("./collection")

    # open .json file and append data to it
    result = []
    for file in os.listdir("./collection/metadata"):
        with open(f"./collection/metadata/{file}", "r") as f:
            if file.endswith(".json"):
                data = json.load(f)
                data["id"] = int(file.split(".")[0])
                result.append(data)

    # sort result by id in ascending order
    result = sorted(result, key=lambda k: k["id"])

    # delete id
    for i in range(len(result)):
        del result[i]["id"]

    with open("./collection/all_metadata.json", "w") as f:
        json.dump(result, f)


def create_rarity_report():
    """Creates a rarity report"""

    # read all_metadata.json
    with open("./collection/all_metadata.json", "r") as f:
        metadata = json.load(f)

    rarities = []

    for d in metadata:

        for i, attribute in enumerate(d["attributes"]):
            layer = attribute["trait_type"]
            item = attribute["value"]

            if layer == SETUP[f"Layer{i + 1}"]["name"]:
                scheme = SETUP[f"Layer{i + 1}"]["scheme"]
                for rarity, items_list in scheme.items():
                    if item in items_list["items"]:
                        rarities.append(
                            {"layer": layer, "rarity": rarity, "item": item}
                        )
                        break
    compute_nft_rarity()
    # group data in this way:
    # layer -> rarity -> item
    # layer : { rarity : { percentage_in_layer, items: { item: count } } }

    grouped = {}
    for rarity in rarities:
        if rarity["layer"] not in grouped:
            grouped[rarity["layer"]] = {"rarity": {}, "items": {}}
            grouped[rarity["layer"]]["rarity"][rarity["rarity"]] = 1
            grouped[rarity["layer"]]["items"][rarity["item"]] = 1
        else:
            if rarity["rarity"] not in grouped[rarity["layer"]]["rarity"]:
                grouped[rarity["layer"]]["rarity"][rarity["rarity"]] = 1
            else:
                grouped[rarity["layer"]]["rarity"][rarity["rarity"]] += 1
            if rarity["item"] not in grouped[rarity["layer"]]["items"]:
                grouped[rarity["layer"]]["items"][rarity["item"]] = 1
            else:
                grouped[rarity["layer"]]["items"][rarity["item"]] += 1

    # compute percentage of rarity and items
    sums_of_rarity = []
    for layer in grouped:
        for rarity in grouped[layer]["rarity"]:
            sum_of_rarity = sum(grouped[layer]["rarity"].values())
            sums_of_rarity.append(sum_of_rarity)

    for layer in grouped:
        for i, rarity in enumerate(grouped[layer]["rarity"]):
            grouped[layer]["rarity"][
                rarity
            ] = f"{round((grouped[layer]['rarity'][rarity] / sums_of_rarity[i])* 100,2)}%"

    # create rarity report
    with open("./collection/rarity_report.json", "w") as f:
        json.dump(grouped, f)


def compute_nft_rarity():
    """
    Computes the overall rarity of a list of rarities.

    1. Read all_metadata.json
    2. Get count of each type of item in each NFT (legendary: 2, epic: 1, ...)
    3. rarity_score = (1 / (attribute count / total nfts))
    """

    # read all_metadata.json
    with open("./collection/all_metadata.json", "r") as f:
        metadata = json.load(f)

    # define a counter for the attributes['value']
    # (legendary: 2, epic: 1, ...)
    items = []
    for d in metadata:
        for attribute in d["attributes"]:
            items.append(attribute["value"])

    # count each type of item in each NFT (legendary: 2, epic: 1, ...)
    counts = {}
    for item in items:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1

    rarities = {}
    for item in items:
        rarities[item] = 1 / (counts[item] / len(metadata))

    report_data = []
    for i, nft in enumerate(metadata):
        data = {}
        rarity_score = 0
        for attribute in nft["attributes"]:
            item = attribute["value"]
            rarity_score += rarities[item]

        data["id"] = i
        data["attributes"] = nft["attributes"]
        data["rarity_score"] = round(rarity_score, 2)

        report_data.append(data)
    # sort metadata by rarity_score
    report_data = sorted(report_data, key=lambda k: k["rarity_score"], reverse=True)

    # create overall_rarity.json
    with open("./collection/overall_rarity.json", "w") as f:
        json.dump(report_data, f)
