# -*- coding: utf-8 -*-

"""This command is used to build the react front with ease"""

from __future__ import unicode_literals

import os
import sys
from subprocess import call

from django.core.management.base import BaseCommand, CommandError


def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


class NotRunningInTTYException(Exception):
    pass


class Command(BaseCommand):
    help = 'This command builds the react frontend files'

    def handle(self, *args, **options):
        sys.stdout.write("The build will begin.\n")
        try:
            os.chdir("front")
        except OSError:
            raise CommandError("Couldn't cd into front.")
        command = which("yarn") or which("npm")
        if not command:
            raise CommandError("Please install yarn or npm.")
        if call([command, "install"]):
            raise CommandError("Error while installing front dependencies.")
        if call([command, "run", "build"]):
            raise CommandError("Error while building front.")
        sys.stdout.write(
            "The frontend has been built.\n"
            "You can now collectstatic.\n"
        )

