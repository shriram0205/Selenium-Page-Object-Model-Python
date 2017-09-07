import unittest
from tests.home import LoginTest
import os
import HTMLTestRunner

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):
    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromModule(LoginTest)
        ])

        outfile = open(direct + "\LoginReport.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

        runner1.run(smoke_test)


if __name__ == '__main__':
    unittest.main()