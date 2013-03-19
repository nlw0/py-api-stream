#include <Python.h>
#include "PyTupleStream.h"
#include "ArrayManager.h"

#include "PyTupleStream.cpp"
#include "ArrayManager.cpp"

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

static PyObject * test_function3(PyObject *self, PyObject *args) {
  TupleStream qq(args);

  double a;
  ArrayManager m;

  qq >> a >> m;

  if (qq.fail()) return NULL;

  double z = a * (m(0,0) * m(1,1) - m(1,0) * m(0,1));

  return PyFloat_FromDouble(z);
}

static PyMethodDef TuStTestMethods[] =
  {
    {"tfun1", test_function1, METH_VARARGS,
     "test function 1.\n"},
    {"tfun2", test_function2, METH_VARARGS,
     "test function 2.\n"},
    {"tfun3", test_function3, METH_VARARGS,
     "test function 3.\n"},
    {NULL, NULL, 0, NULL}
  };

PyMODINIT_FUNC

inittusttest(void) {
  (void) Py_InitModule("tusttest", TuStTestMethods);
  import_array();
}
