import requests


TOR_EXIT_LIST_URL = "https://check.torproject.org/torbulkexitlist"


def get_tor_exit_nodes():
    try:
        response = requests.get(
            TOR_EXIT_LIST_URL,
            timeout=20
        )

        response.raise_for_status()

        exit_nodes = set()

        for line in response.text.splitlines():
            line = line.strip()

            if line:
                exit_nodes.add(line)

        return {
            "success": True,
            "exit_nodes": exit_nodes
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }


def check_tor_exit(ip_address):
    result = get_tor_exit_nodes()

    if not result["success"]:
        return result

    exit_nodes = result["exit_nodes"]

    return {
        "success": True,
        "ip": ip_address,
        "is_tor_exit": ip_address in exit_nodes,
        "total_exit_nodes": len(exit_nodes)
    }
