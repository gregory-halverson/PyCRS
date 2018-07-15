import unittest

import pycrs


class TestParserMethods(unittest.TestCase):
    def test_from_proj4_usfeet_tometer(self):
        # test proj4 using tometer alternative
        crs_obj = pycrs.parser.from_proj4("""+proj=tmerc +lat_0=30 +lon_0=-87.5 +k=0.9999333333333333
                                            +x_0=600000.0000000001 +y_0=0 +ellps=GRS80 +datum=NAD83
                                            +to_meter=0.3048006096012192 +no_defs""")
        # Test correct output
        proj4 = crs_obj.to_proj4()
        self.assertIn('+to_meter=0.3048006096012192', proj4)
        self.assertNotIn('+units=', proj4)

    def test_from_proj4_usfeet_units(self):
        # test proj4 using units altnerative
        crs_obj = pycrs.parser.from_proj4("""+proj=tmerc +lat_0=30 +lon_0=-87.5 +k=0.9999333333333333
                                            +x_0=600000.0000000001 +y_0=0 +ellps=GRS80 +datum=NAD83
                                            +units=us-ft +no_defs""")
        # Test correct output
        proj4 = crs_obj.to_proj4()
        self.assertIn('+units=us-ft', proj4)
        self.assertNotIn('+to_meter=', proj4)