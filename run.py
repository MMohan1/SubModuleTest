from routes import hm
@hm.hook_function('hook_test_resistration_new')
def Test():
    return "from custom module from Function"


class TestClass:
    def __init__(self):
        pass

    @hm.hook('hook_test_resistration')
    def test(self):
        return "from custom module"