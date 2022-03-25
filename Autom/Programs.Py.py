import json
import time
import os

def _modify_events(event):
    with open('../src/events.json','w') as a:
        json.dumps("event", a, indent=4)

def _get_state_value():
    with open('../src/state.json','r') as a:
        return a.read()

def _setup():

# Initialize state.txt

  with open('../src/state.txt','w') as a:
      a.write("IDLE")

def _tear_down():
    # clean state.txt

    if os.path.exists('../src/state.txt'):
        os.unlink('../src/state.txt')

def run_tests():
    # Run test cases.

    --_setup()

# Case - 1 `IDLE - STARTING -> IDLE`
    _modify_events("STARTING")
    time.sleep(5)
    print("changing starting -> IDLE ")
    try:
        assert _get_state_value()
    except AssertionError as msg:
        print(msg)

    -_setup()

# testCase 2 `IDLE - READY_TO_WAIT -> WAIT`
    _modify_events("READY_TO_WAIT")
    time.sleep(5)
    print("changing READY_TO_WAIT -> WAIT")

    assert _get_state_value()

# testCase 3 IDLE - STARTING -> IDLE`

    _modify_events("STARTING")
    time.sleep(5)
    print("changing STARTING -> IDLE")
    assert  _get_state_value()

# testCase 4  - STARTING -> In Progress

    _modify_events("STARTING")
    time.sleep(5)
    print("changing STARTING -> In Progress")
    assert  _get_state_value()

# testCase 5  - completed -> Done

    _modify_events("COMPLETE")
    time.sleep(5)
    print("changing COMPLETE -> DONE")
    assert  _get_state_value()

    -_tear_down()


if __name__ == '__main__':
    run_tests()
