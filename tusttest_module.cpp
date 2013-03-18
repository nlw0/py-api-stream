#include <Python.h>
#include "PyTupleStream.cpp"

static PyObject * test_function1(PyObject *self, PyObject *args) {
  TupleStream qq(args);

  long int a;
  long int b;

  qq >> a >> b;

  if (qq.fail()) return NULL;

  long int z = a + b;

  return PyInt_FromLong(z);
}

static PyObject * test_function2(PyObject *self, PyObject *args) {
  TupleStream qq(args);

  long int a;
  double b;

  qq >> a >> b;

  if (qq.fail()) return NULL;

  double z = a * b;

  return PyFloat_FromDouble(z);
}

static PyMethodDef TuStTestMethods[] =
  {
    {"tfun1", test_function1, METH_VARARGS,
     "test function 1.\n"},
    {"tfun2", test_function2, METH_VARARGS,
     "test function 1.\n"},
    {NULL, NULL, 0, NULL}
  };

PyMODINIT_FUNC

inittusttest(void) {
  (void) Py_InitModule("tusttest", TuStTestMethods);
}
