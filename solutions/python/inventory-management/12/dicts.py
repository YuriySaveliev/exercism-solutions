"""Functions to keep track and alter inventory."""
from collections import Counter


def create_inventory(items: list[str]) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    return dict(Counter(items))

def add_items(inventory: dict, items: list[str]) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    counter = Counter(items)
    for item, count in counter.items():
        inventory[item] = count + inventory.get(item, 0)
    return inventory

def decrement_items(inventory: dict, items: list[str]) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    decrements = Counter(items)
    for item, count in decrements.items():
        if item in inventory:
            inventory[item] = max(inventory[item] - count, 0)
    return inventory

def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, None)
    return inventory

def list_inventory(inventory: dict) -> list[str]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(item, inventory[item]) for item in inventory if inventory[item] > 0]