/* Copyright 2013-2018 Nicolau Leal Werneck
 *
 *    Licensed under the Apache License, Version 2.0 (the "License");
 *    you may not use this file except in compliance with the License.
 *    You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing, software
 *    distributed under the License is distributed on an "AS IS" BASIS,
 *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *    See the License for the specific language governing permissions and
 *    limitations under the License.
 */

#include <Python.h>
#include <iostream>
#include "PyTupleStream.h"
#include "ArrayManager.h"

#include "PyTupleStream.cpp"
#include "ArrayManager.cpp"

static PyObject * test_function1(PyObject *self, PyObject *args) {
  TupleStream ts(args);

  long int a;
  long int b;

  ts >> a >> b;

  if (ts.fail()) return NULL;

  long int z = a + b;

  return PyLong_FromLong(z);
}

static PyObject * test_function2(PyObject *self, PyObject *args) {
  TupleStream ts(args);

  long int a;
  double b;

  ts >> a >> b;

  if (ts.fail()) return NULL;

  double z = a * b;

  return PyFloat_FromDouble(z);
}

static PyObject * test_function3(PyObject *self, PyObject *args) {
  TupleStream ts(args);

  double a;
  ArrayManager<double> m;
  m.set_dimensions(2);

  ts >> a >> m;

  if (ts.fail()) return NULL;

  double z = a * (m(0,0) * m(1,1) - m(1,0) * m(0,1));
    std::cout << z<<std::endl;
  return PyFloat_FromDouble(z);
}

static PyObject * test_function4(PyObject *self, PyObject *args) {
  TupleStream ts(args);

  double a;
  ArrayManager<int> m;
  m.set_dimensions(2);

  ts >> a >> m;

  if (ts.fail()) return NULL;

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
    {"tfun4", test_function4, METH_VARARGS,
     "test function 4.\n"},
    {NULL, NULL, 0, NULL}
  };


static struct PyModuleDef tustmodule = {
    PyModuleDef_HEAD_INIT,
    "tusttest",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    TuStTestMethods
};

PyMODINIT_FUNC
PyInit_tusttest(void) {
  PyObject*module = PyModule_Create(&tustmodule);
  import_array();
  return module;
}
