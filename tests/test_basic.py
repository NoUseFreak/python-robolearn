import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import robolearn

def test_connect():
    robolearn.Robolearn()

def test_connect_url():
    robolearn.Robolearn(url='http://127.0.0.1:9000')

def test_forward():
    rl = robolearn.Robolearn()
    rl.forward()

def test_rotate():
    rl = robolearn.Robolearn()
    rl.rotate()
