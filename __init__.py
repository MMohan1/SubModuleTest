import os
from run import TestClass
tc = TestClass()
from sub_module_routes import *
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app_ini = "app.ini"
sub_module_ini = APP_ROOT + "/" + app_ini
