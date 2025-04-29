from llm.plugins import pm, load_plugins


def test_plugin_is_installed():
    load_plugins()
    names = [mod.__name__ for mod in pm.get_plugins()]
    assert "llm_documentcloud" in names
