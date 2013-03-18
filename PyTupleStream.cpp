#include <Python.h>
#include <exception>


class TupleStream {
  int count;
  int Nargs;
  PyObject *args;
  bool failbit;
public:
  
  friend TupleStream& operator>>(TupleStream &, long int &);

  class ArgsCountException: public std::exception {};
  class TypeErrorException: public std::exception {};
  class FailStateException: public std::exception {};

  TupleStream(PyObject *input_args) {
    failbit = false;
    args = input_args;
    Nargs = PyTuple_Size(args);
    count = 0;
  }

  bool fail() {
    return failbit;
  }

  void set_fail_nargs() {
    PyErr_SetString(PyExc_TypeError, "Too few arguments provided.");
    failbit = true;
  }

  void set_fail_typeerror() {
    char err_msg[1024];
    snprintf(err_msg, 1024, "Incorrect type for parameter number %d.", count + 1);
    PyErr_SetString(PyExc_TypeError, err_msg);
    failbit = true;
  }
};

// Read an integer from tuple stream.
TupleStream& operator>>(TupleStream &input, long int &x) {
  try {
    if (input.fail()) throw TupleStream::FailStateException();

    if (input.count >= input.Nargs) throw TupleStream::ArgsCountException();

    // Fetch next PyObject from stream.
    PyObject *po = PyTuple_GetItem(input.args, input.count);
    
    // type-check, then finally take the value from the PyObject, and
    // then check again! (?)
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
