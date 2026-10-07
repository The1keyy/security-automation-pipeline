import json
import os
import time


CACHE_FILE = "enrichment/cache.json"
CACHE_TTL = 3600


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r") as file:
        return json.load(file)


def save_cache(cache):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file, indent=4)


def get_cached_result(key):
    cache = load_cache()

    if key not in cache:
        return None

    entry = cache[key]

    age = time.time() - entry["timestamp"]

    if age > CACHE_TTL:
        return None

    return entry["data"]


def save_cached_result(key, data):
    cache = load_cache()

    cache[key] = {
        "timestamp": time.time(),
        "data": data
    }

    save_cache(cache)
