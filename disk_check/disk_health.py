#!/usr/bin/env python3

import sys
import shutil
import os


def check_disk_space(disk, min_gb, min_parcent):
    """Returns True if there is enough free disk space and Fale otherwise"""
    # gets sizes of free, used and total of the disk
    disk_stat = shutil.disk_usage(disk)
    # calculate the parcentage of free disk
    free_disk_parcent = 100 * (disk_stat.free / disk_stat.total)
    # calculate the size of free disk in gigabyte
    free_disk_size = disk_stat.free / 1024**3

    if free_disk_size < min_gb or free_disk_parcent < min_parcent:
        return False
    return True


if not check_disk_space(disk="/", min_gb=2, min_parcent=10):
    print("ERROR: Not enough disk space.")
    sys.exit(1)
print("Everything is ok")
