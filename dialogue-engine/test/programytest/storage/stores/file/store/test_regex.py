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
import os
import os.path
import re

from programy.storage.stores.file.store.properties import FileRegexStore
from programy.storage.stores.file.engine import FileStorageEngine
from programy.storage.stores.file.config import FileStorageConfiguration
from programy.mappings.properties import RegexTemplatesCollection
from programy.storage.stores.file.config import FileStoreConfiguration


class FileRegexStoreTests(unittest.TestCase):

    def test_initialise(self):
        config = FileStorageConfiguration()
        engine = FileStorageEngine(config)
        engine.initialise()
        store = FileRegexStore(engine)
        self.assertEqual(store.storage_engine, engine)

    def test_load_regex(self):
        config = FileStorageConfiguration()
        config._regex_storage = FileStoreConfiguration(file=os.path.dirname(__file__) + os.sep + "data" + os.sep + "lookups" + os.sep + "text" + os.sep + "regex-templates.txt",
                                                       format="text", encoding="utf-8", delete_on_start=False)
        engine = FileStorageEngine(config)
        engine.initialise()
        store = FileRegexStore(engine)

        store.empty()

        collection = RegexTemplatesCollection()
        store.load(collection)

        self.assertTrue(collection.has_regex("anything"))
        self.assertEqual(re.compile('^.*$', re.IGNORECASE), collection.regex("anything"))
        self.assertTrue(collection.has_regex("legion"))
        self.assertFalse(collection.has_regex("XXXXX"))
