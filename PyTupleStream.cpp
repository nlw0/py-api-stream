#include <Python.h>
#include <exception>

#include "PyTupleStream.h"

TupleStream::TupleStream(PyObject *input_args) {
  failbit = false;
  args = input_args;
  Nargs = PyTuple_Size(args);
  count = 0;
}

bool TupleStream::fail() {
  return failbit;
}

void TupleStream::set_fail_nargs() {
  PyErr_SetString(PyExc_TypeError, "Too few arguments provided.");
  failbit = true;
}

void TupleStream::set_fail_typeerror() {
  char err_msg[1024];
  snprintf(err_msg, 1024, "Incorrect type for parameter number %d.", count + 1);
  PyErr_SetString(PyExc_TypeError, err_msg);
  failbit = true;
}

bool TupleStream::eof() { return count >= Nargs; }

// Read an integer from tuple stream.
TupleStream& operator>>(TupleStream &input, long int &x) {
  try {
    if (input.fail()) throw TupleStream::FailStateException();

    if (input.count >= input.Nargs) throw TupleStream::ArgsCountException();

    // Fetch next PyObject from stream.
    PyObject *po = PyTuple_GetItem(input.args, input.count);

    // Type-check, then finally take the value from the PyObject, and
    // then check again. First check is necessary to prevent automatic
    // conversion from float to int.
    if (!PyInt_CheckExact(po)) throw TupleStream::TypeErrorException();
    x = PyInt_AsLong(po);    
    if ((x == -1) && PyErr_Occurred()) throw TupleStream::TypeErrorException();
  }
  catch (TupleStream::ArgsCountException) { input.set_fail_nargs(); }
  catch (TupleStream::TypeErrorException) { input.set_fail_typeerror(); }
  catch (TupleStream::FailStateException) { }
  
  input.count++;
  return input;
}

// Read an integer from tuple stream.
TupleStream& operator>>(TupleStream &input, double &x) {
  try {
    if (input.fail()) throw TupleStream::FailStateException();

    if (input.count >= input.Nargs) throw TupleStream::ArgsCountException();

    // Fetch next PyObject from stream.
    PyObject *po = PyTuple_GetItem(input.args, input.count);
    
    // Take the value from the PyObject, and then check if
    // reading/conversion was successful.
    x = PyFloat_AsDouble(po);
    if ((x == -1.0) && PyErr_Occurred()) throw TupleStream::TypeErrorException();
  }
  catch (TupleStream::ArgsCountException) { input.set_fail_nargs(); }
  catch (TupleStream::TypeErrorException) { input.set_fail_typeerror(); }
  catch (TupleStream::FailStateException) { }
  
  input.count++;
  return input;
}

// Read an integer from tuple stream.
TupleStream& operator>>(TupleStream &input, TupleStreamExtractable &x) {
  try {
    if (input.fail()) throw TupleStream::FailStateException();

    if (input.eof()) throw TupleStream::ArgsCountException();

    // Fetch next PyObject from stream.
    PyObject *po = PyTuple_GetItem(input.args, input.count);
    
    // Take the value from the PyObject, and then check if
    // reading/conversion was successful.
    try {
      x = po;
    }
    catch (std::exception) {
      throw TupleStream::TypeErrorException();
    }
  }
  catch (TupleStream::ArgsCountException) { input.set_fail_nargs(); }
  catch (TupleStream::TypeErrorException) { input.set_fail_typeerror(); }
  catch (TupleStream::FailStateException) { }
  
  input.count++;
  return input;
}

