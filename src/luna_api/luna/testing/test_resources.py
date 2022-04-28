import unittest

from luna.api.model.resource import FilesystemResource, ResourceMeta


class TestResourceFactory(unittest.TestCase):

    def test_filesystem_resource(self):
        self.assertIn(FilesystemResource, ResourceMeta.resource_interfaces.values())
        self.assertIn(FilesystemResource.__type__, ResourceMeta.resource_interfaces)


class TestFilesystemResource(unittest.TestCase):

    def test_instantiation(self):
        resource = FilesystemResource(name='test', uri=__file__)
        self.assertTrue(resource.path.exists())
