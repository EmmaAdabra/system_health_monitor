#!/usr/bin/env python3

import sys
import shutil

def check_disk_usage(disk, min_abs, min_parcent):
	''' Returns True if there is enough free disk space and Fale otherwise '''
	# gets sizes of free, used and total of the disk 
	disk_stat = shutil.disk_usage(disk)
	# calculate the parcentage of free disk
	parcent_free_disk = 100 * (disk_stat.free / disk_stat.total)
	# calculate the size of free disk in gigabyte
	free_disk_size = disk_stat.free / 1024**3

	if parcent_free_disk < min_parcent or free_disk_size < min_abs:
		return False

	return True

if not check_disk_usage('/', 2, 10):
	print("ERROR: Not enough disk space.")
	sys.exit(1)
else:
	print("Everything is okay.")
