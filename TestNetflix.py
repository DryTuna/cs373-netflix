# !/usr/bin/env python

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

import unittest
import StringIO

from Netflix import Init, c_avg, m_avg, sqre_diff, RMSE, predict, solve
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
		self.assert_(c_avg[1048577][0] == 4.57692307692)

	def test_Init_2(self):
		Init()
		self.assert_(len(m_avg) == 17770)
		self.assert_(m_avg[1][0] == 3.74954296161)

	def test_Init_3(self):
		Init()
		self.assert_(len(c_avg) == 480189)
		self.assert_(len(m_avg) == 17770)
		self.assert_(c_avg[2097148][0] == 3.08)
		self.assert_(m_avg[17770][0] == 2.81650380022)

	# -------
	# predict
	# -------

	def test_predict_1(self):
		a = predict(2097148, 10)
		self.assert_(a >= 0 and a <= 5)

	def test_predict_2(self):
		a = predict(1442411, 1774)
		self.assert_(a >= 0 and a <= 5)

	def test_predict_3(self):
		a = predict(22601, 9999)
		self.assert_(a >= 0 and a <= 5)

	# ---------
	# sqre_diff
	# ---------

	def test_sqre_diff_1(self):
		a = 5
		b = 4
		self.assert_(sqre_diff(a, b) == 1)

	def test_sqre_diff_2(self):
		a = 1.1
		b = 1
		self.assert_(str(sqre_diff(a, b)) == "0.01")

	def test_sqre_diff_3(self):
		a = 2.0
		b = 4.0
		self.assert_(sqre_diff(a, b) == 4.0)

	# ----
	# RMSE
	# ----

	def test_RMSE_1(self):
		a = [2, 3, 4, 5]
		b = [2, 3, 4, 5]
		self.assert_(RMSE(a, b) == 0.0)

	def test_RMSE_2(self):
		a = [1, 2, 3, 4]
		b = [2, 3, 4, 5]
		self.assert_(RMSE(a, b) == 1.0)

	def test_RMSE_3(self):
		a = [2]
		b = [5]
		self.assert_(RMSE(a, b) == 3.0)
		
	def test_RMSE_4(self):
		a = [2, 3, 4, 5]
		b = [1, 2, 3, 4]
		self.assert_(RMSE(a, b) == 1.0)

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("1001:\n1050889\n67976\n")
		w = StringIO.StringIO()
		solve(r, w)
		self.assert_(w.getvalue() == "RMSE = 0.983460336694\n1001:\n4.5\n3.5\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("10010:\n1462925\n52050\n")
		w = StringIO.StringIO()
		solve(r, w)
		self.assert_(w.getvalue() == "RMSE = 0.983460336694\n10010:\n2.4\n2.2\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("10045:\n2314434\n")
		w = StringIO.StringIO()
		solve(r, w)
		self.assert_(w.getvalue() == "RMSE = 0.983460336694\n10045:\n3.7\n")

# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
