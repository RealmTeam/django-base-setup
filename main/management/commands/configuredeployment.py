# -*- coding: utf-8 -*-

"""This command is used to deploy this django setup with ease"""

from __future__ import unicode_literals

import os
import sys

from django.core.management.base import BaseCommand
from django.template import engines
from django.utils.encoding import force_str
from six.moves import input



class NotRunningInTTYException(Exception):
    pass


class Command(BaseCommand):

    help = 'This command configures the files used in deployment'

    FILES_TO_CONFIGURE = ("README.rst", "main/settings.py",
                          "front/public/index.html", "front/public/manifest.json",
                          "nginx/sites-enabled/main", ".env")

    def _ask_param(self, input_msg, error_msg):
        param = None
        while param is None:
            if not param:
                param = input(force_str('%s: ' % input_msg))

            if not param:
                sys.stderr.write(error_msg)
                param = None
                continue
        return param

    def _get_params(self):
        try:
            if hasattr(sys.stdin, 'isatty') and not sys.stdin.isatty():
                raise NotRunningInTTYException("Not running in a TTY")

            project = self._ask_param("Project name", "You need to specify a project name\n")
            domainname = self._ask_param("Fully qualified domain name for the api",
                                         "You need to specify a domain name for the project to run on\n")
            staticdomainname = self._ask_param("Fully qualified domain name for the assets",
                                               "You need to specify a domain name for the project to run on\n")
            return project, domainname, staticdomainname

        except KeyboardInterrupt:
            sys.stderr.write("\nOperation cancelled.")
            sys.exit(1)

        except NotRunningInTTYException:
            sys.stdout.write("Deployment skipped due to not running in a TTY.")
            sys.exit(1)

    def handle(self, *args, **options):
        sys.stdout.write("The configuration of deployment files will begin.\n")
        project, domainname, staticdomainname = self._get_params()
        context = {'name': project, 'domainname': domainname, 'staticdomainname': staticdomainname}

        for path in self.FILES_TO_CONFIGURE:
            with open(path, "r+") as f:
                old_contents = f.read()
                directory, filename = os.path.split(path)
                with open(os.path.join(directory, ("." if not filename.startswith(".") else "") + filename + ".old"), "w+") as o:
                    o.write(old_contents)
                template = engines['django'].from_string(old_contents)
                f.seek(0)
                f.write(template.render(context))

        sys.stdout.write(
            "Files have been configured.\n"
            "You can now apply instructions from the README file.\n"
        )
