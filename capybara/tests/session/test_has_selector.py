import pytest


class TestHasSelector:
    @pytest.fixture(autouse=True)
    def setup_session(self, session):
        session.visit("/with_html")

    def test_is_true_if_the_given_selector_is_on_the_page(self, session):
        assert session.has_selector("xpath", "//p")

    def test_is_false_if_the_given_selector_is_not_on_the_page(self, session):
        assert not session.has_selector("xpath", "//abbr")