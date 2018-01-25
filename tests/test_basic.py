import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import robolearnr

def test_connect():
    robolearnr.Robolearn()

def test_connect_url():
    robolearnr.Robolearn(url='http://127.0.0.1:9000')

def test_forward():
    rl = robolearnr.Robolearn()
    rl.forward()

def test_rotate():
    rl = robolearnr.Robolearn()
    rl.rotate()
