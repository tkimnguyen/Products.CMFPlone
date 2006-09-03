from zope.component import getSiteManager

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import ILocalPortletAssignable

from plone.app.portlets.tests.base import PortletsTestCase

class TestProductInstall(PortletsTestCase):

    def testPortletManagersRegistered(self):
        sm = getSiteManager(self.portal)
        registrations = [r.name for r in sm.registeredUtilities()
                            if IPortletManager == r.provided]
        self.assertEquals(['plone.dashboard', 'plone.leftcolumn', 'plone.rightcolumn'], sorted(registrations))
        
    def testAssignable(self):
        self.failUnless(ILocalPortletAssignable.providedBy(self.folder))
        self.failUnless(ILocalPortletAssignable.providedBy(self.portal))
        
    def testPermissions(self): 
        self.fail('Test missing')

    def testPortletTypesRegistered(self): 
        self.fail('Test missing')

    
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    return suite
