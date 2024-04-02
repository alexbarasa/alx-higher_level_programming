#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints basic information about a Python list.
 * @p: Pointer to the PyObject representing the list
 *
 * Description: This function prints the
 * size and allocation of the Python list,
 * along with the types of its elements.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyListObject\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - Prints basic information about Python bytes.
 * @p: Pointer to the PyObject representing the bytes object
 *
 * Description: This function prints
 * the size of the bytes object,
 * whether it can be represented as a string,
 * and the first 10 bytes of its content.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p) ? "yes" : "no");
	if (size > 10)
		size = 10;
	str = PyBytes_AsString(p);
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
		printf("%02hhx%c", str[i], i < size - 1 ? ' ' : '\n');
}
/**
 * print_python_float - Prints basic information about Python float.
 * @p: Pointer to the PyObject representing the float object
 *
 * Description: This function prints the value of the float object.
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid PyFloatObject\n");
		return;
	}
	printf("  value: %s\n", PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
