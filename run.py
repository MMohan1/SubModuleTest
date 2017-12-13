from hook_manager import hm
@hm.hook('hook_test_resistration')
def Test():
    return "Good To Know"
