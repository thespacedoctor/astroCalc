from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import unittest
import yaml
from astrocalc.utKit import utKit
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
settingsFile = packageDirectory + "/test_settings.yaml"
su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
moduleDirectory = os.path.dirname(__file__)
pathToInputDir = moduleDirectory + "/input/"
pathToOutputDir = moduleDirectory + "/output/"

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)


class test_unit_conversion(unittest.TestCase):

    def test_unit_conversion_sexe_to_deg_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        # xt-kwarg_key_and_value

        # DEC FIRST
        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        dec = converter.dec_sexegesimal_to_decimal(
            dec="-23:45:21.23232"
        )
        print(dec)

        dec = converter.dec_sexegesimal_to_decimal(
            dec="+1:58:05.45341"
        )
        print(dec)

        dec = converter.dec_sexegesimal_to_decimal(
            dec="+01:58:5.45341"
        )
        print(dec)

        dec = converter.dec_sexegesimal_to_decimal(
            dec="01:58:05"
        )
        print(dec)

        dec = converter.dec_sexegesimal_to_decimal(
            dec="12.3234234234"
        )
        print(dec)

        dec = converter.dec_sexegesimal_to_decimal(
            dec="-34.3234234234"
        )
        print(dec)

        # TEST RA NOW
        ra = converter.ra_sexegesimal_to_decimal(
            ra="23:45:21.23232"
        )
        print(ra)

        # TEST RA NOW
        ra = converter.ra_sexegesimal_to_decimal(
            ra="23h45m21.23232s"
        )
        print(ra)

        # TEST RA NOW
        ra = converter.ra_sexegesimal_to_decimal(
            ra="23 45 21.23232"
        )
        print(ra)

        # TEST RA NOW
        ra = converter.ra_sexegesimal_to_decimal(
            ra="2 04 21.23232"
        )
        print(ra)

        # TEST RA NOW
        ra = converter.ra_sexegesimal_to_decimal(
            ra="04:45  21"
        )
        print(ra)

        ra = converter.ra_sexegesimal_to_decimal(
            ra="12.3234234234"
        )
        print(ra)

        ra = converter.ra_sexegesimal_to_decimal(
            ra="334.3234234234"
        )
        print(ra)

    def test_unit_conversion_deg_to_sex_functions(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        # xt-kwarg_key_and_value

        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        ra = converter.ra_decimal_to_sexegesimal(
            ra="-23.454676456",
            delimiter="/"
        )
        print(ra)

        ra = converter.ra_decimal_to_sexegesimal(
            ra="63.454676456"
        )
        print(ra)

        ra = converter.ra_decimal_to_sexegesimal(
            ra="0.454676456"
        )
        print(ra)

        ra = converter.ra_decimal_to_sexegesimal(
            ra="345.454"
        )
        print(ra)

        ra = converter.ra_decimal_to_sexegesimal(
            ra="345"
        )
        print(ra)

        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        dec = converter.dec_decimal_to_sexegesimal(
            dec="-23.454676456",
            delimiter="/"
        )
        print(dec)

        dec = converter.dec_decimal_to_sexegesimal(
            dec="-83.454676456",
            delimiter=":"
        )
        print(dec)

        dec = converter.dec_decimal_to_sexegesimal(
            dec="-3.454676456",
            delimiter=":"
        )
        print(dec)

        dec = converter.dec_decimal_to_sexegesimal(
            dec="50",
            delimiter=":"
        )
        print(dec)

    def test_unit_conversion_ra_dec_to_cartesian_functions(self):

        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        x, y, z = converter.ra_dec_to_cartesian(
            ra=23.454676456,
            dec=-3.454676456
        )
        print(x, y, z)

        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        x, y, z = converter.ra_dec_to_cartesian(
            ra="23 45 21.23232",
            dec=-3.454676456
        )
        print(x, y, z)

        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        cartesians = converter.ra_dec_to_cartesian(
            ra="23 45 21.23232",
            dec="+01:58:5.45341"
        )
        print(cartesians)
