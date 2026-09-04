# We import our class blueprint from browser_session.py
from browser_session import BrowserSession

def test_case_1_login_flow():
    """Mimics Ranorex Test Case 1: Login"""
    # 1. Setup session object
    login_session = BrowserSession("TC001_Login")
    
    # 2. Perform actions using instance methods and setters
    login_session.delay_seconds = 3
    login_session.start_test_run()
    
    # 3. Assert (Ranorex Validate.AreEqual equivalent)
    assert login_session.delay_seconds == 3

def test_case_2_invalid_delay_guard():
    """Mimics Ranorex Test Case 2: Validation Check"""
    guard_session = BrowserSession("TC002_GuardCheck")
    
    # Try invalid negative value
    guard_session.delay_seconds = -10
    
    # Verify setter guard corrected it
    assert guard_session.delay_seconds == 0