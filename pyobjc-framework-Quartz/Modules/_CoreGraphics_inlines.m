#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#import <ApplicationServices/ApplicationServices.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability"

static PyObjC_function_map function_map[] = {
#if PyObjC_BUILD_RELEASE >= 1009
    {"CGVectorMake", (PyObjC_Function_Pointer)&CGVectorMake},
#endif
    {"CGPointMake", (PyObjC_Function_Pointer)&CGPointMake},
    {"CGRectMake", (PyObjC_Function_Pointer)&CGRectMake},
    {"CGSizeMake", (PyObjC_Function_Pointer)&CGSizeMake},
    {"__CGAffineTransformMake", (PyObjC_Function_Pointer)&__CGAffineTransformMake},
    {"__CGPointApplyAffineTransform",
     (PyObjC_Function_Pointer)&__CGPointApplyAffineTransform},
    {"__CGSizeApplyAffineTransform",
     (PyObjC_Function_Pointer)&__CGSizeApplyAffineTransform},
    {0, 0}};

#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

PyObjC_MODULE_INIT(_inlines)
{
    PyObject* m = PyObjC_MODULE_CREATE(_inlines);
    if (!m)
        PyObjC_INITERROR();

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) < 0)
        PyObjC_INITERROR();

    PyObjC_INITDONE();
}
