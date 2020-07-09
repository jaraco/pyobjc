# This file is generated by objective.metadata
#
# Last update: Thu Jul  9 22:20:48 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
misc.update(
    {
        "FSEventStreamContext": objc.createStructType(
            "FSEventStreamContext", b"{FSEventStreamContext=l^v^?^?^?}", []
        )
    }
)
constants = """$$"""
enums = """$kFSEventStreamCreateFlagFileEvents@16$kFSEventStreamCreateFlagIgnoreSelf@8$kFSEventStreamCreateFlagMarkSelf@32$kFSEventStreamCreateFlagNoDefer@2$kFSEventStreamCreateFlagNone@0$kFSEventStreamCreateFlagUseCFTypes@1$kFSEventStreamCreateFlagUseExtendedData@64$kFSEventStreamCreateFlagWatchRoot@4$kFSEventStreamEventFlagEventIdsWrapped@8$kFSEventStreamEventFlagHistoryDone@16$kFSEventStreamEventFlagItemChangeOwner@16384$kFSEventStreamEventFlagItemCloned@4194304$kFSEventStreamEventFlagItemCreated@256$kFSEventStreamEventFlagItemFinderInfoMod@8192$kFSEventStreamEventFlagItemInodeMetaMod@1024$kFSEventStreamEventFlagItemIsDir@131072$kFSEventStreamEventFlagItemIsFile@65536$kFSEventStreamEventFlagItemIsHardlink@1048576$kFSEventStreamEventFlagItemIsLastHardlink@2097152$kFSEventStreamEventFlagItemIsSymlink@262144$kFSEventStreamEventFlagItemModified@4096$kFSEventStreamEventFlagItemRemoved@512$kFSEventStreamEventFlagItemRenamed@2048$kFSEventStreamEventFlagItemXattrMod@32768$kFSEventStreamEventFlagKernelDropped@4$kFSEventStreamEventFlagMount@64$kFSEventStreamEventFlagMustScanSubDirs@1$kFSEventStreamEventFlagNone@0$kFSEventStreamEventFlagOwnEvent@524288$kFSEventStreamEventFlagRootChanged@32$kFSEventStreamEventFlagUnmount@128$kFSEventStreamEventFlagUserDropped@2$kFSEventStreamEventIdSinceNow@18446744073709551615$"""
misc.update(
    {
        "kFSEventStreamEventExtendedDataPathKey": "path",
        "kFSEventStreamEventExtendedFileIDKey": "fileID",
    }
)
functions = {
    "FSEventStreamShow": (b"v^{__FSEventStream=}",),
    "FSEventStreamGetLatestEventId": (b"Q^{__FSEventStream=}",),
    "FSEventStreamRetain": (b"v^{__FSEventStream=}",),
    "FSEventStreamSetDispatchQueue": (b"v^{__FSEventStream=}@",),
    "FSEventsCopyUUIDForDevice": (
        b"^{__CFUUID=}i",
        "",
        {"retval": {"already_retained": True}},
    ),
    "FSEventStreamSetExclusionPaths": (
        b"v^{__FSEventStream=}^{__CFArray=}",
        "",
        {"retval": {"type": "Z"}},
    ),
    "FSEventStreamScheduleWithRunLoop": (
        b"v^{__FSEventStream=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "FSEventStreamInvalidate": (b"v^{__FSEventStream=}",),
    "FSEventStreamStop": (b"v^{__FSEventStream=}",),
    "FSEventsPurgeEventsForDeviceUpToEventId": (b"ZiQ",),
    "FSEventStreamGetDeviceBeingWatched": (b"i^{__FSEventStream=}",),
    "FSEventStreamCopyDescription": (
        b"^{__CFString=}^{__FSEventStream=}",
        "",
        {"retval": {"already_retained": True}},
    ),
    "FSEventStreamCopyPathsBeingWatched": (
        b"^{__CFArray=}^{__FSEventStream=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "FSEventStreamUnscheduleFromRunLoop": (
        b"v^{__FSEventStream=}^{__CFRunLoop=}^{__CFString=}",
    ),
    "FSEventStreamRelease": (b"v^{__FSEventStream=}",),
    "FSEventStreamStart": (b"Z^{__FSEventStream=}",),
    "FSEventStreamFlushSync": (b"v^{__FSEventStream=}",),
    "FSEventsGetLastEventIdForDeviceBeforeTime": (b"Qid",),
    "FSEventStreamFlushAsync": (b"Q^{__FSEventStream=}",),
    "FSEventsGetCurrentEventId": (b"Q",),
}
misc.update(
    {
        "FSEventStreamRef": objc.createOpaquePointerType(
            "FSEventStreamRef", b"^{__FSEventStream=}"
        )
    }
)
expressions = {}

# END OF FILE
