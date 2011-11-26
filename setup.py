#!/usr/bin/python
from distutils.core import setup
import sys
import re

verpat = re.compile("VERSION *= *\"(.*)\"")
data = open("mgarepo").read()
m = verpat.search(data)
if not m:
    sys.exit("error: can't find VERSION")
VERSION = m.group(1)

setup(name="mgarepo",
      version = VERSION,
      description = "Tools for Mageia repository access and management",
      author = "Gustavo Niemeyer",
      author_email = "gustavo@niemeyer.net",
      url = "https://wiki.mageia.org/en/Mgarepo",
      license = "GPL",
      long_description = """Tools for Mageia repository access and management, based on repsys.""",
      packages = ["MgaRepo", "MgaRepo.cgi", "MgaRepo.commands",
          "MgaRepo.plugins"],
      scripts = ["mgarepo", "mgarepo-ssh"],
      data_files = [
	      ("/usr/share/mgarepo/",
              ["default.chlog",
              "revno.chlog",
              "create-srpm"]),
	      ("/etc/", ["mgarepo.conf"]),
          ("share/man/man8/", ["mgarepo.8"])]
      )

# vim:ts=4:sw=4:et
