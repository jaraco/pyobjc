# This file is generated by objective.metadata
#
# Last update: Thu Jun 25 17:13:37 2020
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
constants = """$SKCloudServiceCapabilitiesDidChangeNotification$SKCloudServiceSetupActionSubscribe$SKCloudServiceSetupMessageIdentifierAddMusic$SKCloudServiceSetupMessageIdentifierConnect$SKCloudServiceSetupMessageIdentifierJoin$SKCloudServiceSetupMessageIdentifierPlayMusic$SKCloudServiceSetupOptionsActionKey$SKCloudServiceSetupOptionsAffiliateTokenKey$SKCloudServiceSetupOptionsCampaignTokenKey$SKCloudServiceSetupOptionsITunesItemIdentifierKey$SKCloudServiceSetupOptionsMessageIdentifierKey$SKDownloadTimeRemainingUnknown@d$SKErrorDomain$SKReceiptPropertyIsExpired$SKReceiptPropertyIsRevoked$SKReceiptPropertyIsVolumePurchase$SKStoreProductParameterAdNetworkAttributionSignature$SKStoreProductParameterAdNetworkCampaignIdentifier$SKStoreProductParameterAdNetworkIdentifier$SKStoreProductParameterAdNetworkNonce$SKStoreProductParameterAdNetworkSourceAppStoreIdentifier$SKStoreProductParameterAdNetworkTimestamp$SKStoreProductParameterAdNetworkVersion$SKStoreProductParameterAdvertisingPartnerToken$SKStoreProductParameterAffiliateToken$SKStoreProductParameterCampaignToken$SKStoreProductParameterITunesItemIdentifier$SKStoreProductParameterProductIdentifier$SKStoreProductParameterProviderToken$SKStorefrontCountryCodeDidChangeNotification$SKStorefrontIdentifierDidChangeNotification$"""
enums = """$SKCloudServiceAuthorizationStatusAuthorized@3$SKCloudServiceAuthorizationStatusDenied@1$SKCloudServiceAuthorizationStatusNotDetermined@0$SKCloudServiceAuthorizationStatusRestricted@2$SKCloudServiceCapabilityAddToCloudMusicLibrary@256$SKCloudServiceCapabilityMusicCatalogPlayback@1$SKCloudServiceCapabilityMusicCatalogSubscriptionEligible@2$SKCloudServiceCapabilityNone@0$SKDownloadStateActive@1$SKDownloadStateCancelled@5$SKDownloadStateFailed@4$SKDownloadStateFinished@3$SKDownloadStatePaused@2$SKDownloadStateWaiting@0$SKErrorClientInvalid@1$SKErrorCloudServiceNetworkConnectionFailed@7$SKErrorCloudServicePermissionDenied@6$SKErrorCloudServiceRevoked@8$SKErrorInvalidOfferIdentifier@11$SKErrorInvalidOfferPrice@14$SKErrorInvalidSignature@12$SKErrorMissingOfferParams@13$SKErrorPaymentCancelled@2$SKErrorPaymentInvalid@3$SKErrorPaymentNotAllowed@4$SKErrorPrivacyAcknowledgementRequired@9$SKErrorStoreProductNotAvailable@5$SKErrorUnauthorizedRequestData@10$SKErrorUnknown@0$SKOverlayPositionBottom@0$SKOverlayPositionBottomRaised@1$SKPaymentTransactionStateDeferred@4$SKPaymentTransactionStateFailed@2$SKPaymentTransactionStatePurchased@1$SKPaymentTransactionStatePurchasing@0$SKPaymentTransactionStateRestored@3$SKProductDiscountPaymentModeFreeTrial@2$SKProductDiscountPaymentModePayAsYouGo@0$SKProductDiscountPaymentModePayUpFront@1$SKProductDiscountTypeIntroductory@0$SKProductDiscountTypeSubscription@1$SKProductPeriodUnitDay@0$SKProductPeriodUnitMonth@2$SKProductPeriodUnitWeek@1$SKProductPeriodUnitYear@3$SKProductStorePromotionVisibilityDefault@0$SKProductStorePromotionVisibilityHide@2$SKProductStorePromotionVisibilityShow@1$"""
misc.update({})
functions = {"SKTerminateForInvalidReceipt": (b"v",)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"cloudServiceSetupViewControllerDidDismiss:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentQueue:didRevokeEntitlementsForProductIdentifiers:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:removedTransactions:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:restoreCompletedTransactionsFailedWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:shouldAddStorePayment:forProduct:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:shouldContinueTransaction:inStorefront:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:updatedDownloads:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueue:updatedTransactions:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"paymentQueueDidChangeStorefront:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentQueueRestoreCompletedTransactionsFinished:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentQueueShouldShowPriceConsent:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"productViewControllerDidFinish:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"productsRequest:didReceiveResponse:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"request:didFailWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"requestDidFinish:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"storeOverlay:didFailToLoadWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:didFinishDismissal:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:didFinishPresentation:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:willStartDismissal:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"storeOverlay:willStartPresentation:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"SKArcadeService",
        b"arcadeSubscriptionStatusWithNonce:resultHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"I"},
                            3: {"type": b"@"},
                            4: {"type": b"I"},
                            5: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKArcadeService",
        b"registerArcadeAppWithRandomFromLib:randomFromLibLength:resultHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"I"},
                            3: {"type": b"@"},
                            4: {"type": b"I"},
                            5: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKMutablePayment",
        b"setSimulatesAskToBuyInSandbox:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKMutablePayment", b"simulatesAskToBuyInSandbox", {"retval": {"type": b"Z"}})
    r(
        b"SKOverlayAppConfiguration",
        b"setUserDismissible:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKOverlayAppConfiguration", b"userDismissible", {"retval": {"type": b"Z"}})
    r(b"SKPayment", b"simulatesAskToBuyInSandbox", {"retval": {"type": b"Z"}})
    r(b"SKPaymentQueue", b"canMakePayments", {"retval": {"type": b"Z"}})
    r(b"SKProduct", b"downloadable", {"retval": {"type": b"Z"}})
    r(b"SKProduct", b"isDownloadable", {"retval": {"type": b"Z"}})
    r(b"SKProduct", b"isFamilyShareable", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
