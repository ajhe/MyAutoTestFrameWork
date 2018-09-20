# coding=utf-8

from Src.BrowserEngine import browserEngine
import unittest



if __name__ == '__main__':
    suite = unittest.TestLoader().discover("TestSuite")
    try:
        browserEngine.launch_local_browser()
        runner = unittest.TextTestRunner()
        runner.run(suite)
    finally:
        browserEngine.quit_browser()
