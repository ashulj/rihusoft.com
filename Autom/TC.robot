***settings ***
Library SeleniumLibrary
Library json
Library Collection
Library JSON Library
Library Built In
Library Operating System


***Variables***
# defind path for state & joson

state_file ..//src/state.json
Json_file  ..//src/events.json

***Test Cases***
# requirements and Test Scenarios

Requirements
    Start the functiona
    File already exist ${json_file}
    Update Event Data in json_file
     File already exist ${state_file}

TESTCASE 1  state changed to Wait when READY_TO_WAIT  event right
        update Event Data in json   READY_TO_WAIT
        Check state Data in json    Wait

TESTCASE 2  state changed to Wait when IN_PROGRESS when STARTING event right
        update Event Data in json   STARTING
        Check state Data in json    IN_PROGRESS

TESTCASE 3  state changed to Done when complete event right
        update Event Data in json  COMPLETE
        Check state Data in json    DONE


***Function***
# New events Should Contain
update events Data in Json
    [Arguments]     ${New_event}
    ${binary_data}  binary File     ${json_file}
    ${json_dict} =  Evaluted Json.loads('''${binary_data}'''}
    set to the dictionary   ${json_dict}    even=${New_event}
    ${new_json} = coverted Json to string   ${json_dict}
    new Create file     ${json_file}    ${new_json}
    sleep 3s


Check State data
    [Arguments]     ${new_state}
    ${state} = file name  ${state_file}
    Should be Equal As Strings  ${state}    ${new_state}

Start with state program
    State process  python   ../src/main.py  cwd=./ shell= TrueType





