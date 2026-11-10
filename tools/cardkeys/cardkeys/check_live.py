#!/usr/bin/env python3
"""Live check for drifterpixel/yaml-keys-in-3-dataset-cards.

UNTESTED against the network: written in a step that had no network access.
Standard library only. No arguments needed beyond the optional --offline.

Usage, from the folder that holds this file and the two package files:

    python3 check_live.py            # one GET per link, print the ARTIFACTS block
    python3 check_live.py --offline  # no request at all, live values NOT_READ

Exit codes:
    0  online: page answered 2xx and both files answered 2xx with live size
       equal to local size. Offline: nothing checked, printed as such.
    1  online: at least one link did not answer 2xx or a size did not match.
    2  bad argument.

It fetches three URLs once each and writes nothing: pasting the printed lines
into ARTIFACTS.md is a separate, human step.
"""

import os
import sys
import urllib.error
import urllib.request

DATASET = "drifterpixel/yaml-keys-in-3-dataset-cards"
PAGE_URL = "https://huggingface.co/datasets/" + DATASET
RESOLVE_BASE = PAGE_URL + "/resolve/main/"
FILES = ("data.csv", "README.md")
TIMEOUT_SECONDS = 30
USER_AGENT = "cardkeys-live-check/1 (stdlib urllib; one request per link)"


def folder():
    """The folder this script sits in, so sibling files are found."""
    return os.path.dirname(os.path.abspath(__file__))


def local_size(name):
    """Byte size of the sibling file, or None if it is not there."""
    try:
        return os.path.getsize(os.path.join(folder(), name))
    except OSError:
        return None


def fetch(url):
    """Return (status, nbytes, error_name). Exactly one request, no retry."""
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT}, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read()
            status = int(getattr(response, "status", 0) or 0)
            return status, len(body), None
    except urllib.error.HTTPError as error:
        return int(error.code), None, "HTTPError"
    except Exception as error:  # URLError, timeout, DNS, TLS: all NOT_READ
        return None, None, type(error).__name__


def size_word(value):
    return "NOT_READ" if value is None else "{} B".format(value)


def main(argv):
    if len(argv) > 2 or (len(argv) == 2 and argv[1] != "--offline"):
        print("usage: python3 check_live.py [--offline]")
        return 2
    offline = len(argv) == 2

    problems = []
    print("# cardkeys live check")
    print("# dataset: {}".format(DATASET))
    if offline:
        print("# offline: no request made; every live value below is NOT_READ")
    else:
        print("# one GET per link, no retry, timeout {} s".format(TIMEOUT_SECONDS))

    # 1. The dataset page itself.
    if offline:
        print("page      {}  NOT_READ  (no fetch)".format(PAGE_URL))
    else:
        status, nbytes, error = fetch(PAGE_URL)
        if error is None and status is not None and 200 <= status < 300:
            print("page      {}  HTTP {}  {} delivered".format(
                PAGE_URL, status, size_word(nbytes)))
        else:
            reason = error if error else "HTTP {}".format(status)
            print("page      {}  NOT_READ  {}  (no 2xx answer)".format(
                PAGE_URL, reason))
            problems.append("page")

    # 2. Each file link, once, compared with the local sibling.
    for name in FILES:
        url = RESOLVE_BASE + name
        local = local_size(name)
        if offline:
            print("{:<9} {}  NOT_READ  local {}  verdict NOT_READ  (no fetch)".format(
                name, url, size_word(local)))
            continue
        status, nbytes, error = fetch(url)
        if error is not None or status is None or not (200 <= status < 300):
            reason = error if error else "HTTP {}".format(status)
            print("{:<9} {}  NOT_READ  local {}  verdict NOT_READ  ({})".format(
                name, url, size_word(local), reason))
            problems.append(name)
            continue
        if local is None:
            verdict = "NO_LOCAL_FILE"
        elif nbytes == local:
            verdict = "match"
        else:
            verdict = "MISMATCH"
        print("{:<9} {}  HTTP {}  live {}  local {}  verdict {}".format(
            name, url, status, size_word(nbytes), size_word(local), verdict))
        if verdict != "match":
            problems.append(name)

    if offline:
        print("# nothing verified: run again without --offline where network exists")
        return 0
    if problems:
        print("# FAIL: {}. Do not record a live size for these.".format(
            ", ".join(problems)))
        return 1
    print("# OK: page answered 2xx; both files answered 2xx; "
          "both live sizes equal the local files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
