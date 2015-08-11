from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTabViewController (TestCase):
    @min_os_level('10.10')
    def testConstants(self):
        self.assertEqual(NSTabViewControllerTabStyleSegmentedControlOnTop, 0)
        self.assertEqual(NSTabViewControllerTabStyleSegmentedControlOnBottom, 1)
        self.assertEqual(NSTabViewControllerTabStyleToolbar, 2)
        self.assertEqual(NSTabViewControllerTabStyleUnspecified, -1)

    def testMethods(self):
        self.assertResultIsBOOL(NSTabViewController.canPropagateSelectedChildViewControllerTitle)
        self.assertArgIsBOOL(NSTabViewController.setCanPropagateSelectedChildViewControllerTitle_, 0)

        self.assertResultIsBOOL(NSTabViewController.tabView_shouldSelectTabViewItem_)

if __name__ == "__main__":
    main()