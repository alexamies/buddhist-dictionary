"""Unit tests for the bdict.configmanager module.

Tests the methods for loading the configuration file.
"""

import unittest

from bdict import configmanager


class ConfigManagerTest(unittest.TestCase):

    def testLoadConfig(self):
        manager = configmanager.ConfigurationManager()
        config = manager.LoadConfig()
        self.assertTrue(config)
