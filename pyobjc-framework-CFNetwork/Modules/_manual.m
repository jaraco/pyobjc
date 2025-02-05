#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreServices/CoreServices.h>
#if PyObjC_BUILD_RELEASE > 1008
#import <CFNetwork/CFNetwork.h>
#endif

static const void*
mod_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFStreamClientContext mod_CFStreamClientContext = {
    0, NULL, (void* (*)(void*))mod_retain, (void (*)(void*))mod_release, NULL};

static CFHostClientContext mod_CFHostClientContext = {0, NULL, mod_retain, mod_release,
                                                      0};

#if PyObjC_BUILD_RELEASE >= 1005
static void
m_CFProxyAutoConfigurationResultCallback(void* _context, CFArrayRef proxyList,
                                         CFErrorRef error)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_list = PyObjC_IdToPython((NSObject*)(NSArray*)proxyList);
    if (py_list == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    PyObject* py_error = PyObjC_IdToPython((NSObject*)(NSError*)error);
    if (py_error == NULL) {
        Py_DECREF(py_list);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }

    PyObject* rv = PyObject_CallFunction(py_func, "ONN", py_ctx, py_list, py_error);

    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}
#endif

static void
m_CFHostClientCallBack(CFHostRef host, CFHostInfoType typeInfo,
                       const CFStreamError* error, void* _context)
{
    PyObject* context = (PyObject*)_context;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_func = PyTuple_GetItem(context, 0);
    PyObject* py_ctx  = PyTuple_GetItem(context, 1);

    PyObject* py_host = PyObjC_IdToPython((NSObject*)host);
    if (py_host == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    PyObject* py_info = PyObjC_ObjCToPython(@encode(CFHostInfoType), &typeInfo);
    if (py_info == NULL) {
        Py_DECREF(py_host);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }

    PyObject* py_error = PyObjC_ObjCToPython("{_CFStreamError=qi}", (void*)error);
    if (py_error == NULL) {
        Py_DECREF(py_host);
        Py_DECREF(py_info);
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }

    PyObject* rv =
        PyObject_CallFunction(py_func, "NNNO", py_host, py_info, py_error, py_ctx);

    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
        return;
    }
    Py_DECREF(rv);

    PyGILState_Release(state);
}

static PyObject*
m_CFNetworkExecuteProxyAutoConfigurationScript(PyObject* mod __attribute__((__unused__)),
                                               PyObject* args)
{
    CFStringRef script;
    CFURLRef    url;
    PyObject*   callback;
    PyObject*   ctx;
    PyObject*   py_script;
    PyObject*   py_url;

    if (!PyArg_ParseTuple(args, "OOOO", &py_script, &py_url, &callback, &ctx)) {
        return NULL;
    }

    if (depythonify_python_object(py_script, (id*)&script) == -1) {
        return NULL;
    }

    if (depythonify_python_object(py_url, (id*)&url) == -1) {
        return NULL;
    }

    PyObject* py_context = Py_BuildValue("OO", callback, ctx);
    if (py_context == NULL) {
        return NULL;
    }

    CFStreamClientContext context = mod_CFStreamClientContext;
    context.info                  = py_context;

    CFRunLoopSourceRef ref = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CFNetworkExecuteProxyAutoConfigurationScript(
                script, url, m_CFProxyAutoConfigurationResultCallback, &context);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            ref = NULL;
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

    return rv;
}

static PyObject*
m_CFNetworkExecuteProxyAutoConfigurationURL(PyObject* mod __attribute__((__unused__)),
                                            PyObject* args)
{
    CFURLRef  script;
    CFURLRef  url;
    PyObject* callback;
    PyObject* ctx;
    PyObject* py_script;
    PyObject* py_url;

    if (!PyArg_ParseTuple(args, "OOOO", &py_script, &py_url, &callback, &ctx)) {
        return NULL;
    }

    if (depythonify_python_object(py_script, (id*)&script) == -1) {
        return NULL;
    }

    if (depythonify_python_object(py_url, (id*)&url) == -1) {
        return NULL;
    }

    PyObject* py_context = Py_BuildValue("OO", callback, ctx);
    if (py_context == NULL) {
        return NULL;
    }

    CFStreamClientContext context = mod_CFStreamClientContext;
    context.info                  = py_context;

    CFRunLoopSourceRef ref = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CFNetworkExecuteProxyAutoConfigurationURL(
                script, url, m_CFProxyAutoConfigurationResultCallback, &context);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            ref = NULL;
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* rv = PyObjC_IdToPython((NSObject*)ref);

    return rv;
}

static PyObject*
m_CFHostSetClient(PyObject* mod __attribute__((__unused__)), PyObject* args)
{
    CFHostRef host;
    PyObject* callback;
    PyObject* ctx;
    PyObject* py_host;
    Boolean   ok = 0;

    if (!PyArg_ParseTuple(args, "OOO", &py_host, &callback, &ctx)) {
        return NULL;
    }

    if (depythonify_python_object(py_host, (id*)&host) == -1) {
        return NULL;
    }
    if (callback == Py_None) {
        Py_BEGIN_ALLOW_THREADS
            @try {
                ok = CFHostSetClient(host, NULL, NULL);
            } @catch (NSException* localException) {
                PyObjCErr_FromObjC(localException);
            }
        Py_END_ALLOW_THREADS

        if (PyErr_Occurred()) {
            return NULL;
        }

        return PyBool_FromLong(!!ok);
    }

    PyObject* py_context = Py_BuildValue("OO", callback, ctx);
    if (py_context == NULL) {
        return NULL;
    }

    CFHostClientContext context = mod_CFHostClientContext;
    context.info                = py_context;

    Py_BEGIN_ALLOW_THREADS
        @try {
            ok = CFHostSetClient(host, m_CFHostClientCallBack, &context);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(py_context);

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyBool_FromLong(!!ok);
}

static PyMethodDef mod_methods[] = {
#if PyObjC_BUILD_RELEASE >= 1005
    {"CFNetworkExecuteProxyAutoConfigurationScript",
     (PyCFunction)m_CFNetworkExecuteProxyAutoConfigurationScript, METH_VARARGS,
     "CFNetworkExecuteProxyAutoConfigurationScript(arg0, arg1, arg2, arg3)"},
#endif /* OSX >= 10.5 */
#if PyObjC_BUILD_RELEASE >= 1005
    {"CFNetworkExecuteProxyAutoConfigurationURL",
     (PyCFunction)m_CFNetworkExecuteProxyAutoConfigurationURL, METH_VARARGS,
     "CFNetworkExecuteProxyAutoConfigurationURL(arg0, arg1, arg2, arg3)"},
#endif /* OSX >= 10.5 */

    {"CFHostSetClient", (PyCFunction)m_CFHostSetClient, METH_VARARGS,
     "CFHostSetClient(arg0, arg1, arg2)"},

    {
        0,
        0,
        0,
    }};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_manual", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__manual(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__manual(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    return m;
}
