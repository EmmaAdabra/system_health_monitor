#!/usr/bin/env python3

import sys
import shutil
import os


def check_disk_space(disk, min_gb, min_percent):
    """Returns True if amount of free disk space is less than min_gb or
    min_percent and False otherwise"""
    # gets sizes of free, used and total of the disk
    disk_stat = shutil.disk_usage(disk)
    # calculate the percentage of free disk
    free_disk_percent = 100 * (disk_stat.free / disk_stat.total)
    # calculate the size of free disk in gigabyte
    free_disk_size = disk_stat.free / 1024**3

    if free_disk_size < min_gb or free_disk_percent < min_percent:
        return True
    return False


def check_roof_full():
    """Return True if the root partition is full and False otherwise"""
    return check_disk_space(disk="/", min_gb=2, min_percent=10)


def main():
    if check_disk_space(disk="/", min_gb=2, min_percent=10):
        print("ERROR: Not enough disk space.")
        sys.exit(1)
    print("Everything is ok")


if __name__ == "__main__":
    main()
