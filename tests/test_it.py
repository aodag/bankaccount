from datetime import datetime
from OFS.Folder import Folder
from Acquisition import Explicit
from Products.MyBlog import blog


def test_catalog():
    folder = Folder()
    catalog = blog._create_catalog(folder)

    class Dummy(Explicit):
        def __init__(self, title, date):
            self.title = title
            self.date = date

    dummy = Dummy("dummy title", datetime(2018, 1, 1))
    dummy = dummy.__of__(folder)
    catalog.catalog_object(dummy, "/this/is/dummy")
    result = catalog({"title": "dummy title"})
    assert len(catalog) == 1
    assert len(result) == 1
    assert result[0].title == "dummy title"
    assert list(catalog) == []
