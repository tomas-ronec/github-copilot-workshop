"""NetBox Device Query Tool — Reference Solution.

A professional CLI tool for querying devices from a NetBox instance.
"""

import argparse
import logging
import os
import sys

import requests


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Query devices from a NetBox instance."
    )
    parser.add_argument(
        "search_term",
        type=str,
        help="The device name (or partial name) to search for.",
    )
    parser.add_argument(
        "--url",
        type=str,
        default="https://demo.netbox.dev/",
        help="The base URL of the NetBox instance (default: https://demo.netbox.dev/).",
    )
    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="Your NetBox API token. Falls back to NETBOX_API_TOKEN env var.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose (DEBUG) logging.",
    )
    return parser.parse_args()


def resolve_token(cli_token):
    """Resolve the API token from CLI argument or environment variable."""
    if cli_token:
        return cli_token
    env_token = os.getenv("NETBOX_API_TOKEN")
    if env_token:
        return env_token
    return None


def query_devices(url, token, search_term):
    """Query NetBox API for devices matching the search term."""
    api_url = f"{url.rstrip('/')}/api/dcim/devices/"
    params = {"name__ic": search_term}
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
    }

    logging.info("Querying %s for devices matching '%s'", api_url, search_term)

    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=30)
    except requests.exceptions.RequestException as e:
        logging.error("Network error: %s", e)
        return None

    logging.debug("Response status: %s", response.status_code)
    logging.debug("Response body: %s", response.text)

    if response.status_code in (401, 403):
        logging.error(
            "Authentication failed (HTTP %s). Check your API token.",
            response.status_code,
        )
        return None

    if response.status_code != 200:
        logging.error("API error: HTTP %s", response.status_code)
        return None

    return response.json()


def display_results(data, search_term):
    """Display query results."""
    results = data.get("results", [])

    if not results:
        logging.warning("No devices found matching '%s'.", search_term)
        return

    logging.info("Found %d device(s) matching '%s':", len(results), search_term)

    for device in results:
        name = device.get("name", "Unknown")
        primary_ip = device.get("primary_ip")
        if primary_ip and primary_ip.get("address"):
            ip_display = primary_ip["address"]
        else:
            ip_display = "No IP assigned"
        logging.info("  %s — %s", name, ip_display)


def main():
    """Main entry point."""
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if args.verbose:
        logging.debug("Verbose logging enabled.")

    token = resolve_token(args.token)
    if not token:
        logging.critical(
            "No API token provided. Use --token or set NETBOX_API_TOKEN env var."
        )
        sys.exit(1)

    data = query_devices(args.url, token, args.search_term)
    if data is None:
        sys.exit(1)

    display_results(data, args.search_term)
    logging.info("Script finished.")


if __name__ == "__main__":
    main()
