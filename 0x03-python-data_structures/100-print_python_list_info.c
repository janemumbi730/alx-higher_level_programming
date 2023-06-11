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
	PyListObject *i;
	PyObject *j;

	b = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", b);

	i = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", i->allocated);

	for (a = 0; a < b; a++)
	{
		j = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(j)->tp_name);
	}
}
