class BrowserSession:
    # =========================================================================
    # 1. CLASS VARIABLES (C# equivalent: static fields)
    # Direct storage locations shared across ALL instances in the project.
    # =========================================================================
    default_timeout = 10         # Class Variable: Shared default timeout
    total_sessions_created = 0   # Class Variable: Shared counter across all tests

    # =========================================================================
    # 2. CONSTRUCTOR & INSTANCE VARIABLES (C# equivalent: regular fields)
    # Runs when an object is created: `BrowserSession("TC01")`
    # =========================================================================
    def __init__(self, test_name):
        # --- INSTANCE VARIABLES ---
        # Direct storage locations unique to THIS specific instance.
        self.test_name = test_name                   # Public Instance Variable
        self._target_url = "https://www.costco.com" # Internal Instance Variable (_ signals internal use)
        self._delay_seconds = 2                      # Internal Instance Variable (backing store for the property below)
        
        # Updating a shared Class Variable
        BrowserSession.total_sessions_created += 1

    # =========================================================================
    # 3. PROPERTIES: GETTER & SETTER (C# equivalent: public int DelaySeconds { get; set; })
    # NOT raw variables! These are functions disguised as variables to run guard logic.
    # =========================================================================
    @property
    def delay_seconds(self):
        """PROPERTY GETTER: Secretly runs when you READ `session.delay_seconds`"""
        return self._delay_seconds

    @delay_seconds.setter
    def delay_seconds(self, seconds):
        """PROPERTY SETTER GUARD: Secretly runs when you ASSIGN `session.delay_seconds = value`"""
        if seconds < 0:
            print(f"--> GUARD TRIGGERED [{self.test_name}]: Delay cannot be negative. Forcing to 0s.")
            self._delay_seconds = 0
        else:
            self._delay_seconds = seconds

    # =========================================================================
    # 4. INSTANCE METHOD (C# equivalent: regular public method)
    # Operates on individual object data. Always requires 'self' as the 1st parameter.
    # =========================================================================
    def start_test_run(self):
        # Combines instance variables (self.test_name), properties (self.delay_seconds),
        # and class variables (self.default_timeout).
        print(f"[{self.test_name}] Target: {self._target_url} | Delay: {self.delay_seconds}s | Timeout: {self.default_timeout}s")

    # =========================================================================
    # 5. CLASS METHOD (C# equivalent: static method operating on static fields)
    # Operates on class-level settings. Always requires 'cls' as the 1st parameter.
    # =========================================================================
    @classmethod
    def set_global_timeout(cls, new_timeout):
        cls.default_timeout = new_timeout
        print(f"--> GLOBAL UPDATE: Default timeout updated to {cls.default_timeout}s")

    # =========================================================================
    # 6. STATIC METHOD (C# equivalent: static utility helper method)
    # Pure utility function. Has NO 'self' or 'cls' parameter.
    # =========================================================================
    @staticmethod
    def sanitize_url(raw_url):
        return raw_url.strip().lower().rstrip("/")


#The core difference is that variables (or raw attributes) directly store data in memory, 
# while properties look like variables but execute custom code under the hood when you read, write, or delete them
#importance of getters
#In test automation, you might store an endpoint path internally, but when tests read it, 
# they always need the full, properly formatted URL.
#Example 1
# @property
# def target_url(self):
#     """GETTER: Converts path to a fully formatted environment URL dynamically."""
#     return f"https://{self._environment}.costco.com/{self._endpoint.strip('/')}"

#another example
# @property
# def driver(self):
#     """GETTER: Opens the browser only when the test actually needs it."""
#     if self._driver is None:
#         print("--> Launching Chrome Browser...")
#         self._driver = webdriver.Chrome()
#     return self._driver

#Keyboard Shortcut: Press Ctrl + Shift + E.