#!/usr/bin/env python3

from calendar import c
import shutil
import os
import socket
import psutil
from date_helper import current_date


def check_free_disk():
    """Returns true if the amount of root free disk is less than 20% and True
    otherwise"""
    # gets sizes of free, used and total of the disk
    disk_stat = shutil.disk_usage("/")
    # calculate the percentage of free disk
    free_disk_percent = 100 * (disk_stat.free / disk_stat.total)

    return free_disk_percent < 20


def check_reboot():
    """Return True if there is a pending reboot and false if otherwise"""
    return os.path.exists("/run/boot-required")


def check_cpu_load():
    """Returns True if cpu usage if over 80% and False if otherwise"""
    cpu_usage = psutil.cpu_percent(1)  # get percentage of cpu usage
    # print(cpu_usage)
    return cpu_usage > 80


def check_network():
    """check for network availability. Return true if it fails to resolve google server url and false otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True


def check_free_memory():
    """return true if available memory is less than 500MB and true otherwise"""
    memory = psutil.virtual_memory()  # memory stats
    available_memory = memory.available  # get available memory
    # convert available memory to MB
    available_memory = available_memory / 1024**2

    return available_memory < 500


def all_check(checks):
    """get a list of tuples as parameter, each tuple contains a function to be
    called and a message that will be added to a report list if the function
    return true and return the report list after all checks"""
    reports = []  # list of massages if called function returns true

    # iterate through check list and call each function in the list
    for check, msg in checks:
        if check:
            reports.append(msg)
    return reports


def output_checks(reports):
    """print the time and result of all the checks"""
    date = current_date()
    report_dir = "pc_health_report"
    report_file = "pc_health-report.txt"
    report_file_path = os.path.join(report_dir, report_file)

    date_text = "--------------- {} ---------------{}".format(date["date"], "\n\n")
    time = "Time - " + date["time"] + "\n"
    if not os.path.exists(report_file_path):
        os.mkdir(report_dir)
        with open(report_file_path, mode="w"):
            pass
    with open(report_file_path, mode="a") as file:
        if len(reports) != 0:
            report = "\n".join(reports)
            # write if script is executed for the first time or a new date
            msg_1 = "{}{}{}\n\n".format(date_text, time, report)
            # write if script executed subsequently
            msg_2 = "{}{}\n\n".format(time, report)

            if date["date"] != None:
                file.writelines(msg_1)
            else:
                file.writelines(msg_2)

        else:
            msg = "Pc in good health"
            if date["date"] != None:
                file.writelines("{}{}{}\n\n".format(date_text, time, msg))
            else:
                file.writelines("{}{}\n\n".format(time, msg))


def main():
    # a list of tuple containing checks and message
    checks = [
        (check_cpu_load(), "Error - CPU usage is over 80%"),
        (check_free_disk(), "Error - Available disk space is less than 20%"),
        (check_free_memory(), "Error - Available memory is less than 500MB"),
        (check_network(), "Error - No Network connection"),
        (check_reboot(), "Error - Pending reboot"),
    ]
    check_report = all_check(checks)
    output_checks(check_report)


if __name__ == "__main__":
    main()
