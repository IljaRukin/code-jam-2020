cd C:\Users\User\Downloads\challenges\ESAb_ATAd
REM  python -m compileall ./ESAb_ATAd.py
python interactive_runner.py python local_testing_tool.py 2 -- python ESAb_ATAd.py
REM python interactive_runner.py python local_testing_tool.py 0 -- python test.py
set /p DUMMY=Hit ENTER to continue...