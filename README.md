# 🤖 Test Automation Assessment Suite

> **Complete Selenium Python automation solution for all 10 assessment tasks**
> Covers two target applications:
> - `https://nickolusalex.github.io/automation_interview/` (Tasks 1–2)
> - `https://opensource-demo.orangehrmlive.com` (Tasks 3–10)

---

## ✅ Final Test Results

```
================================================================================
                    TEST EXECUTION SUMMARY REPORT
================================================================================
#    | Assignment Name                            | Status  | Duration
--------------------------------------------------------------------------------
1    | Task 1: Token Generation                   |  PASS   | 5.26s
2    | Task 2: Hidden Element Toggle              |  PASS   | 4.81s
3    | Task 3: Valid Credentials Login            |  PASS   | 14.25s
4    | Task 4: Invalid Password Login             |  PASS   | 9.23s
5    | Task 5: Add New Employee (PIM)             |  PASS   | 27.14s
6    | Task 6: Create Employee Login              |  PASS   | 26.39s
7    | Task 7: Submit Weekly Timesheet            |  PASS   | 30.67s
8    | Task 8: Manager Rejects Timesheet          |  PASS   | 20.92s
9    | Task 9: Add Candidate & Schedule Interview |  PASS   | 41.07s
10   | Task 10: Candidate Hiring Stages           |  PASS   | 75.32s
--------------------------------------------------------------------------------
Total Tests : 10  |  Passed : 10  |  Failed : 0  |  Total Time : ~255s
================================================================================
```

---

## 📋 System Requirements

### 1. Operating System
- Windows 10 / 11 (tested) — also works on macOS & Linux

### 2. Python
- **Python 3.10 or higher** required
- Download from: https://www.python.org/downloads/
- Verify installation:
  ```powershell
  python --version
  ```

### 3. Web Browser
One of the following must be installed:

| Browser | Default? | Download |
|---|---|---|
| **Microsoft Edge** | ✅ Yes (default) | Pre-installed on Windows 10/11 |
| Google Chrome | Optional | https://www.google.com/chrome |

> [!NOTE]
> The tests use **Microsoft Edge** by default (headless mode). No manual ChromeDriver or EdgeDriver download is needed — **Selenium Manager** (built into Selenium 4.6+) fetches the matching driver automatically.

### 4. Internet Connection
- Required for browser to load:
  - `https://nickolusalex.github.io/automation_interview/`
  - `https://opensource-demo.orangehrmlive.com`

---

## 📁 Project Structure

```
assessment_automation/
│
├── driver_utils.py                                   # Shared WebDriver factory & helper utilities
├── run_all_assignments.py                            # Master suite runner (executes all 10 tests)
├── requirements.txt                                  # Python package dependencies
├── sample_resume.txt                                 # Resume file used in Recruitment tests (Tasks 9 & 10)
├── README.md                                         # This documentation file
│
├── assignment_01_token_generation.py                 # Task 1 – Double-click & Token Format Validation
├── assignment_02_hidden_element.py                   # Task 2 – Hidden Element Toggle
├── assignment_03_login_valid.py                      # Task 3 – Successful Login
├── assignment_04_login_invalid.py                    # Task 4 – Login with Invalid Password
├── assignment_05_add_new_employee.py                 # Task 5 – Add New Employee (PIM)
├── assignment_06_create_employee_login.py            # Task 6 – Create Employee Login Account
├── assignment_07_submit_weekly_timesheet.py          # Task 7 – Submit Weekly Timesheet
├── assignment_08_manager_reject_timesheet.py         # Task 8 – Manager Rejects Timesheet
├── assignment_09_add_candidate_schedule_interview.py # Task 9 – Add Candidate & Schedule Interview
└── assignment_10_candidate_hiring_stages.py          # Task 10 – Candidate Hiring Stages
```

---

## ⚙️ Setup — Step-by-Step Instructions

### Step 1: Verify Python is installed

Open **PowerShell** or **Command Prompt** and run:

```powershell
python --version
```

You should see something like `Python 3.12.x`. If not, download and install from https://www.python.org/downloads/

---

### Step 2: Clone the repository

```powershell
git clone https://github.com/Arihant37/assessment-automation.git
cd assessment-automation
```

---

### Step 3: Install required Python packages

```powershell
pip install -r requirements.txt
```

This installs:
| Package | Purpose |
|---|---|
| `selenium >= 4.20` | Browser automation framework |
| `webdriver-manager >= 4.0` | Optional; drivers are resolved by Selenium Manager |
| `pytest >= 8.0` | Optional test runner with detailed reports |

---

### Step 4: Verify the setup works

Run a quick check to confirm Selenium and Edge are working:

```powershell
python -c "from selenium import webdriver; from selenium.webdriver.edge.options import Options; opts = Options(); opts.add_argument('--headless=new'); d = webdriver.Edge(options=opts); d.get('https://google.com'); print('Setup OK! Title:', d.title); d.quit()"
```

Expected output: `Setup OK! Title: Google`

---

## 🚀 How to Run the Tests

### ▶ Option 1: Run ALL 10 Assignments at Once (Recommended)

This runs the complete suite and displays a formatted summary report:

```powershell
python run_all_assignments.py
```

---

### ▶ Option 2: Run a Single Assignment

Each script can be run independently:

```powershell
python assignment_01_token_generation.py
python assignment_02_hidden_element.py
python assignment_03_login_valid.py
python assignment_04_login_invalid.py
python assignment_05_add_new_employee.py
python assignment_06_create_employee_login.py
python assignment_07_submit_weekly_timesheet.py
python assignment_08_manager_reject_timesheet.py
python assignment_09_add_candidate_schedule_interview.py
python assignment_10_candidate_hiring_stages.py
```

---

### ▶ Option 3: Run with Pytest (Detailed Output)

```powershell
# Run all tests (files are named assignment_*.py, so tell pytest to collect them)
pytest -v -o python_files="assignment_*.py"

# Run a specific test file
pytest -v assignment_03_login_valid.py

# Run with output (no capture)
pytest -v -s assignment_05_add_new_employee.py
```

---

## 🔧 Configuration Options

Control browser and headless mode using environment variables:

### Run with a visible browser window (for debugging):

**PowerShell:**
```powershell
$env:HEADLESS="0"
python assignment_03_login_valid.py
```

**Command Prompt:**
```cmd
set HEADLESS=0
python assignment_03_login_valid.py
```

### Use Google Chrome instead of Edge:

**PowerShell:**
```powershell
$env:BROWSER="chrome"
python run_all_assignments.py
```

**Command Prompt:**
```cmd
set BROWSER=chrome
python run_all_assignments.py
```

| Variable | Values | Default |
|---|---|---|
| `HEADLESS` | `0` = visible browser, `1` = background | `1` |
| `BROWSER` | `edge` or `chrome` | `edge` |

---

## 📝 Assignment Details

### Task 1 — Token Generation
**URL:** `https://nickolusalex.github.io/automation_interview/`

| Step | Action |
|---|---|
| 1 | Open the automation interview page |
| 2 | Double-click the **"Double-Click Me"** button using `ActionChains` |
| 3 | Capture the generated token text |
| 4 | Verify it matches format `XXX-XXX-XXX` (alphanumeric, 3-3-3) using regex |
| 5 | Double-click again and verify the token changes |
| 6 | Print the generated token |

**Expected:** Token format validated ✅ + Token changes on each double-click ✅

---

### Task 2 — Hidden Element Toggle
**URL:** `https://nickolusalex.github.io/automation_interview/`

| Step | Action |
|---|---|
| 1 | Open the automation interview page |
| 2 | Verify the secret text is **initially hidden** (`is_displayed() = False`) |
| 3 | Click **"Show Secret"** button |
| 4 | Verify `🎯 Secret Code: 42XYZ` becomes **visible** → Print `true` |
| 5 | Click **"Show Secret"** again to toggle it back |
| 6 | Verify the element is **hidden again** → Print `false` |

**Expected:** `true` when visible, `false` when hidden ✅

---

### Task 3 — Successful Login with Valid Credentials
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`

| Step | Action |
|---|---|
| 1 | Navigate to OrangeHRM login page |
| 2 | Enter **Username:** `Admin` |
| 3 | Enter **Password:** `admin123` |
| 4 | Click **Login** button |
| 5 | Verify redirect to `/dashboard` |
| 6 | Verify user display name is visible |
| 7 | Verify profile icon is displayed |
| 8 | Verify URL contains `demo.orangehrmlive` |
| 9 | Verify no authentication error alerts |

**Expected:** All 4 post-login conditions verified ✅

---

### Task 4 — Login with Invalid Password
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`

| Step | Action |
|---|---|
| 1 | Navigate to OrangeHRM login page |
| 2 | Enter **Username:** `Admin` |
| 3 | Enter an **invalid password** (e.g. `WrongPassword_999!#`) |
| 4 | Click **Login** button |
| 5 | Verify error message `Invalid credentials` appears |
| 6 | Verify user remains on `/auth/login` URL |
| 7 | Verify login input fields are still visible |

**Expected:** Login blocked + error shown + user stays on login page ✅

---

### Task 5 — Add New Employee (Mandatory Info Only)
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`
**Module:** PIM (Employee Management)

| Step | Action |
|---|---|
| 1 | Login as `Admin / admin123` |
| 2 | Navigate to **PIM** module from top menu |
| 3 | Click **Add Employee** |
| 4 | Enter **First Name** (auto-generated unique name) |
| 5 | Enter **Last Name** |
| 6 | Note the **auto-generated Employee ID** |
| 7 | Click **Save** |
| 8 | Verify redirect to employee Personal Details page |
| 9 | Navigate to Employee List and search by Employee ID |
| 10 | Verify employee appears in results table |

**Expected:** Record created ✅ + ID generated ✅ + Appears in list ✅

---

### Task 6 — Create Employee with Login Account
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`
**Module:** PIM (Employee Management)

| Step | Action |
|---|---|
| 1 | Login as `Admin / admin123` |
| 2 | Go to **PIM → Add Employee** |
| 3 | Enter employee **First Name** and **Last Name** |
| 4 | Enable the **"Create Login Details"** toggle switch |
| 5 | Enter a unique **Username** |
| 6 | Enter and confirm a strong **Password** |
| 7 | Click **Save** |
| 8 | Verify redirect to Personal Details page |
| 9 | **Logout** the Admin session |
| 10 | Login with the **newly created employee credentials** |
| 11 | Verify login is successful and user profile is shown |

**Expected:** Profile created ✅ + Login account created ✅ + Employee can login ✅

---

### Task 7 — Submit Weekly Timesheet
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`
**Module:** Time

| Step | Action |
|---|---|
| 1 | Login as `Admin / admin123` |
| 2 | Check Attendance Punch In/Out status |
| 3 | Navigate to **Time → Timesheets → My Timesheets** |
| 4 | Click **Edit** to open the current week's timesheet |
| 5 | Enter `8.00` hours for each weekday (Mon–Fri) in the table |
| 6 | Click **Save** to save the timesheet |
| 7 | Navigate back to **My Timesheets** |
| 8 | Click **Submit** for approval |
| 9 | Verify page shows **"Status: Submitted"** text |

**Expected:** Timesheet submitted ✅ + Status = Submitted ✅

---

### Task 8 — Manager Rejects Submitted Timesheet
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`
**Module:** Time

| Step | Action |
|---|---|
| 1 | Login as Manager/Admin (`Admin / admin123`) |
| 2 | Navigate to **Time → Timesheets → Employee Timesheets** |
| 3 | Review the list of submitted timesheets pending action |
| 4 | Click **View** on a submitted employee timesheet |
| 5 | Check for **Reject** button and click it |
| 6 | Enter rejection comments in the text area |
| 7 | Confirm rejection |
| 8 | Verify status changes to **Rejected** |

**Expected:** Rejection workflow executed ✅ + Status = Rejected ✅ + Employee can resubmit ✅

---

### Task 9 — Add Candidate and Schedule Interview
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`
**Module:** Recruitment

| Step | Action |
|---|---|
| 1 | Login as `Admin / admin123` |
| 2 | Navigate to **Recruitment → Add Candidate** |
| 3 | Enter **First Name** and **Last Name** |
| 4 | Enter **Email** address |
| 5 | Enter **Contact Number** |
| 6 | Select a **Vacancy** from the dropdown |
| 7 | Upload **Resume** file (`sample_resume.txt`) |
| 8 | Click **Save** |
| 9 | Verify candidate profile is created (`/recruitment/addCandidate/{id}`) |
| 10 | Click **Shortlist** to advance the candidate |
| 11 | Confirm shortlisting |
| 12 | Verify candidate appears in recruitment workflow |

**Expected:** Profile created ✅ + Resume stored ✅ + Interview in workflow ✅

---

### Task 10 — Move Candidate Through Hiring Stages
**URL:** `https://opensource-demo.orangehrmlive.com/web/index.php`
**Module:** Recruitment

| Step | Stage | Action |
|---|---|---|
| 1 | **Application Initiated** | Create a fresh candidate and verify application is initiated |
| 2 | **Interview Scheduled** | Click **Shortlist**, confirm; then verify workflow stage |
| 3 | **Interview Passed** | Click **Mark Interview Passed**, confirm |
| 4 | **Job Offer** | Click **Offer Job**, confirm |
| 5 | **Verify History** | Confirm recruitment status/history is recorded on the page |

**Expected:** Status updates at each stage ✅ + Recruitment history recorded ✅

---

## 🛡️ Framework Design Decisions

| Feature | Implementation |
|---|---|
| **Explicit Waits** | `WebDriverWait` + `expected_conditions` ; only short `time.sleep()` pauses for UI animations |
| **Loader Handling** | `safe_click()` waits for `oxd-form-loader` spinner to disappear before clicking |
| **Random Popup Handling** | `handle_possible_alert()` accepts or dismisses unexpected browser alerts |
| **Unique Test Data** | `uuid.uuid4()` generates unique names/emails/usernames per run to avoid collisions |
| **UTF-8 Support** | `sys.stdout.reconfigure(encoding="utf-8")` prevents emoji print errors on Windows |
| **Network Retry** | `orangehrm_login()` retries page load once on transient DNS/network failures |
| **Clean Teardown** | `try...finally: driver.quit()` always closes browser, even on test failure |
| **Cross-Browser** | Supports **Microsoft Edge** (default) and **Google Chrome** via env variable |

---

## 🔑 OrangeHRM Demo Credentials

| Field | Value |
|---|---|
| **URL** | `https://opensource-demo.orangehrmlive.com/web/index.php` |
| **Username** | `Admin` |
| **Password** | `admin123` |

> [!WARNING]
> This is a **shared public demo environment**. Other users may be modifying data simultaneously, which can occasionally cause tests (especially Timesheets and Recruitment) to behave differently across runs.
