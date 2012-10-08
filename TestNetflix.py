import unittest


from Netflix import Init, c_avg
# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    
    def testInit(self):
        Init()
        self.assert_(len(c_avg) == 480189)
        self.assert_(c_avg[2097092] == 3.28260869565)
        
    
    def testPredict(self):
        self.assert_(False);
    
    def testCalcRMSE(self):
        self.assert_(False);
    
    
    
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."