/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */
static void __attribute__((__used__)) use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1012
    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(PHLivePhotoFrame)); Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(PHPhotoLibraryChangeObserver)); Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(PHPhotoLibraryAvailabilityObserver)); Py_XDECREF(p);
#endif
}
