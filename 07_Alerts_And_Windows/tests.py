from pages import AlertsPage, WindowsPage


def test_javascript_alerts(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.load()

    # 1. Standard JS Alert
    alert_text = alerts_page.trigger_js_alert_and_accept()
    assert alert_text == "I am a JS Alert"
    assert alerts_page.get_result_text() == "You successfully clicked an alert"

    # 2. JS Confirm (Dismiss)
    confirm_text = alerts_page.trigger_js_confirm_and_dismiss()
    assert confirm_text == "I am a JS Confirm"
    assert alerts_page.get_result_text() == "You clicked: Cancel"

    # 3. JS Prompt (Input text)
    input_str = "Automated Test"
    prompt_text = alerts_page.trigger_js_prompt_and_send_keys(input_str)
    assert prompt_text == "I am a JS prompt"
    assert alerts_page.get_result_text() == f"You entered: {input_str}"


def test_multiple_windows(driver):
    windows_page = WindowsPage(driver)
    windows_page.load()

    # Verify Parent Heading
    assert windows_page.get_heading_text() == "Opening a new window"

    # Open child tab and switch context
    parent_handle, child_handle = windows_page.open_new_window_and_switch()

    # Assert Child Window Heading
    assert windows_page.get_heading_text() == "New Window"

    # Close child tab and switch back
    windows_page.close_current_tab_and_switch_to(parent_handle)

    # Confirm back on Parent Window
    assert windows_page.get_heading_text() == "Opening a new window"