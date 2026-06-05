from user_module_v1 import Administrator

"""9-11. Імпортований Admin
Вынести классы User, Privileges, Admin в один модуль. В основном файле импортировать,
создать экземпляр Admin, вызвать show_privileges()."""

adm = Administrator("Joe", "Bone", 20, "USA")
adm.privileges.show_privileges()
