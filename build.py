#!/bin/env python3

import __main__
import argparse
import glob
import os
import subprocess
import sys

IMAGE_VERSION = "0.1"
IMAGE_REPO = "lewiedonckers/inplace-library-build"


def banner(message):
    print(f"\n===== {message}")


def run_command(command, *, capture=False):
    args = {"encoding": "utf-8", "capture_output": True} if capture else {"check": True}
    print(f"running command: {' '.join(command)}")
    try:
        return subprocess.run(command, **args)
    except subprocess.CalledProcessError as e:
        print(f"FATAL ERROR: {e}")
        sys.exit(1)


def get_image_name(path):
    id = path.replace("/", "")
    return f"{IMAGE_REPO}:{IMAGE_VERSION}-{id}"


def get_image_paths():
    files = glob.glob("./**/Dockerfile", recursive=True)
    return [os.path.normpath(os.path.dirname(f)) for f in files]


def docker_does_image_exist(name):
    result = run_command(["docker", "manifest", "inspect", name], capture=True)
    return result.returncode == 0


def docker_build_image(name, path):
    run_command(["docker", "build", path, "-t", name])


def docker_push_image(name):
    run_command(["docker", "push", name])


def build(*, push):
    images = {get_image_name(p): p for p in get_image_paths()}

    for n, p in images.items():
        banner(f"CHECKING IF DOCKER IMAGE {n} EXISTS")
        if docker_does_image_exist(n):
            banner(f"DOCKER IMAGE {n} EXISTS; SKIPPING")
            continue

        banner(f"DOCKER IMAGE {n} DOES NOT EXIST; BUILDING")

        docker_build_image(n, p)

        if push:
            banner(f"DOCKER IMAGE {n} PUSH REQUESTED; PUSHING")
            docker_push_image(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", action="store_true")
    args = parser.parse_args()
    build(push=args.push)
