import os
from subprocess import call
import sys
import re
import multiprocessing as mp
import string
import urllib
import shutil
import errno


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def call_with_err_code(cmd):
    err_code = call(cmd, shell=True)
    if err_code != 0:
        print("")
        print("")
        sys.stderr.write('call \'' + cmd + '\' exited with error code ' + str(err_code) + ' \n')
        print("")
        exit(err_code)


def install_packages_debian(packages_to_install):
    call_with_err_code('sudo apt-get update')
    call_with_err_code('sudo apt-get -y install ' + " ".join(packages_to_install))