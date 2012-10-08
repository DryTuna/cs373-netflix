#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Duy & Ulan
# -------------------------------

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.py.out
"""


# -------
# imports
# -------

import StringIO
import unittest


from Netflix import Init, c_avg, m_avg, sqre_diff, RMSE
# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    
	# ----
	# Init
	# ----

	def test_Init_1(self):
		Init()
		self.assert_(len(c_avg) == 480189)
		self.assert_(c_avg[1048577] == 4.57692307692)

	def test_Init_2(self):
		Init()
		self.assert_(len(m_avg) == 17770)
		self.assert_(m_avg[1] == 3.74954296161)

	def test_Init_3(self):
		Init()
		self.assert_(len(c_avg) == 480189)
		self.assert_(len(m_avg) == 17770)
		self.assert_(c_avg[2097148] == 3.08)
		self.assert_(m_avg[17770] == 2.81650380022)

	# -------
	# predict
	# -------

	def test_predict_1(self):
		self.assert_(False)
    

	# ---------
	# sqrt_diff
	# ---------

	def test_sqrt_diff_1(self):
		a = 10
		b = 1
		self.assert_(sqre_diff(a, b) == 81)

	def test_sqrt_diff_2(self):
		a = 1.1
		b = 1
		c = sqre_diff(b, a)
		self.assert_(sqre_diff(a, b) == c)

	def test_sqrt_diff_3(self):
		a = 3.0
		b = 9.0
		self.assert_(sqre_diff(a, b) == 36.0)

	# ----
	# RMSE
	# ----

	def test_RMSE_1(self):
		a = [2, 3, 4, 5]
		b = [2, 3, 4, 5]
		self.assert_(RMSE(a, b) == 0.0)

	def test_RMSE_2(self):
		a = [2, 3, 4, 5]
		b = [3, 4, 5, 6]
		self.assert_(RMSE(a, b) == 1.0)

	def test_RMSE_3(self):
		a = [2]
		b = [5]
		self.assert_(RMSE(a, b) == 3.0)
    
    
    
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
