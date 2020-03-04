# -*- coding: utf-8 -*-
# catalog (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from unittest import TestCase as BaseCase
import pandas as pd
from . import Cata, get_checksum

df = pd.DataFrame(data={
    "id": [1, 2, 3],
    "value": [1, 4, 9] 
})
params = {"lr": 0.01, "momentum": 0.9}
checksum_good = "6a493bd94026b8ff60fcc1601fdd4ec144a2e82eb46d4b4a973263d89130beb7"

class BasicTestCase(BaseCase):
    def setUp(self):
        self.cata = Cata("/tmp/test.cata", overwrite=True)

    def tearDown(self):
        pass

    def test_create(self):
        "ensure an entry can be created"
        checksum = self.cata.create(df, params=params)
        self.assertEqual(checksum, checksum_good)

    def test_read(self):
        "ensure an entry can be read"
        checksum = self.cata.create(df, params=params)
        df_test = self.cata.read(checksum=checksum)
        self.assertIsNotNone(df_test)

        params_test = self.cata.get_params(checksum=checksum)
        #print(params)
        self.assertIsNotNone(params_test)

        self.assertEqual(get_checksum(df_test, params_test), checksum_good)

    def test_checksum(self):
        "ensure a table checksum works"
        # result = self.cata.create(df, params={"lr": 0.01, "momentum": 0.9})
        checksum = get_checksum(df, params)
        self.assertEqual(checksum, checksum_good)
        #assert(False)
