import pytest
import site

@pytest.fixture(autouse=True, scope="module")
def setup_module():
      site.addsitedir('src')
