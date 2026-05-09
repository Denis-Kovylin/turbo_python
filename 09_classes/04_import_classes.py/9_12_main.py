from only_user import User
from only_privileges import Privileges
from  user_module_v1 import Administrator
'''9-12. Декілька модулів
User в одном модуле, Privileges и Admin в другом (импортируют User из первого). 
В основном файле создать Admin, вызвать show_privileges().'''

adm = Administrator('Bob', 'Joy', 22, 'USA')
adm.privileges.show_privileges()