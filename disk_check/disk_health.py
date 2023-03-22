#!/usr/bin/env python3

import sys
import shutil

def check_disk_space(disk, min_gb, min_parcent):
	''' Returns True if there is enough free disk space and Fale otherwise '''
	# gets sizes of free, used and total of the disk 
	disk_stat = shutil.disk_usage(disk)
	# calculate the parcentage of free disk
	parcent_free_disk = 100 * (disk_stat.free / disk_stat.total)
	# calculate the size of free disk in gigabyte
	free_disk_size = disk_stat.free / 1024**3

	if parcent_free_disk < min_parcent or free_disk_size < min_gb:
		return False

	return True

if not check_disk_space(disk='/', min_gb=2, min_parcent=10):
	print("ERROR: Not enough disk space.")
	sys.exit(1)
else:
	print("Everything is okay.")
