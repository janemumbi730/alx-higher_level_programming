#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list
 * @p: object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int b, a;
	PyListObject *list;
	PyObject *item;

	b = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", b);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (a = 0; a < b; a++)
	{
		item = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(item)->tp_name);
	}
}
