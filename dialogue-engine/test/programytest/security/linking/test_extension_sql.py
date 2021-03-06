"""
Copyright (c) 2020 COTOBA DESIGN, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import unittest
from programy.storage.stores.sql.engine import SQLStorageEngine
from programy.storage.stores.sql.config import SQLStorageConfiguration
from programy.security.linking.accountlinker import BasicAccountLinkerService

from programytest.client import TestClient
from programytest.security.linking.extension_asserts import AccountLinkerExtensionAsserts
import programytest.storage.engines as Engines


class SQLAccountLinkerExtensionTests(AccountLinkerExtensionAsserts):

    def setUp(self):
        config = SQLStorageConfiguration()
        storage_engine = SQLStorageEngine(config)
        storage_engine.initialise()

        client = TestClient()
        self.context = client.create_client_context("TESTUSER")
        self.context.brain._security._account_linker = BasicAccountLinkerService(storage_engine)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_unknown_command(self):
        self.assert_unknown_command(self.context)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_primary_account_link_success(self):
        self.assert_primary_account_link_success(self.context)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_primary_account_link_failures(self):
        self.assert_primary_account_link_failures(self.context)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_secondary_account_link_success(self):
        self.assert_secondary_account_link_success(self.context)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_secondary_account_link_failures(self):
        self.assert_secondary_account_link_failures(self.context)
