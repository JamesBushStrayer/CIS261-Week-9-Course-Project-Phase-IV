# CIS261 Course Project Phase IV
# James Alan Bush (SU200619708)

def CreateUsers():
  print("Create users, passwords and roles")
  UserFile = open("Users.txt", "a+")
  while True:
    username = GetUserName()
    if username.upper() == "END":
      break
    userpwd = GetUserPassword()
    userrole = GetUserRole()

    UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
    UserFile.write(UserDetail)

  UserFile.close()
  printuserinfo()

def GetUserName():
  username = input("Enter a username or 'END' to quit: ")
  return username

def GetUserPassword():
  pwd = input("Enter password: ")
  return pwd

def GetUserRole():
  userrole = input("Enter a role (Admin or User): ")
  if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
    return userrole
  else:
    userrole = input("Enter a role (Admin or User): ")


def printuserinfo():
  UserFile = open("Users.txt", "r")
  while True:
    UserDetail = UserFile.readline()
    if not UserDetail:
      break
    UserDetail = UserDetail.replace("\n", "")
    UserList = UserDetail.split("|")
    username = UserList[0]
    userpassword = UserList[1]
    userrole = UserList[2]
    print("Username: ", username, " Password: ", userpassword, " Role: ",
          userrole)

def Login():
  UserFile = open("Users.txt", "r")
  UserList = []
  UserName = input("Enter username: ")
  UserPwd = input("Enter password: ")
  UserRole = "None"

  while True:
    UserDetail = UserFile.readline()
    if not UserDetail:
      return UserRole, UserName, UserPwd
    UserDetail = UserDetail.replace("\n", "")
    UserList = UserDetail.split("|")
    if UserName == UserList[0] and UserPwd == UserList[1]:
      UserRole = UserList[2]
      return UserRole, UserName

  return UserRole, UserName

def GetEmpName():
  empname = input("Enter employee name: ")
  return empname


def GetDatesWorked():
  fromdate = input("Enter the start date (mm/dd/yyyy): ")
  todate = input("Enter the end date (mm/dd/yyyy): ")
  return fromdate, todate


def GetHoursWorked():
  hours = float(input("Enter the number of hours worked: "))
  return hours

def GetHourlyRate():
  hourlyrate = float(input("Enter the hourly rate: "))
  return hourlyrate

def GetTaxRate():
  taxrate = float(input("Enter the tax rate: "))
  taxrate = taxrate / 100
  return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
  grosspay = hours * hourlyrate
  incometax = grosspay * taxrate
  netpay = grosspay - incometax
  return grosspay, incometax, netpay

def printinfo(EmpDetailList):
  TotEmployees = 0
  TotHours = 0
  TotGrossPay = 0
  TotTax = 0
  TotNetPay = 0

  EmpFile = open("Employees.txt", "r")
  while True:
    rundate = input(
        "Enter start date for report (mm/dd/yyyy) or 'ALL' for all data: ")
    if rundate.upper() == "ALL":
      break
    try:
      rundate = datetime.strptime(rundate, "%m/%d/%Y")
      break
    except ValueError:
      print(
          "Invalid date format. Please enter a valid date in the format mm/dd/yyyy."
      )
      print()
      continue

  while True:
    EmpDetail = EmpFile.readline()
    if not EmpDetail:
      break
    EmpDetail = EmpDetail.replace("\n", "")
    EmpList = EmpDetail.split("|")
    fromdate = EmpList[0]
    if (str(rundate).upper() != "ALL"):
      checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
      if (checkdate < rundate):
        continue
    todate = EmpList[1]
    empname = EmpList[2]
    hours = float(EmpList[3])
    hourlyrate = float(EmpList[4])
    taxrate = float(EmpList[5])
    grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)

    print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}",
          f"{taxrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.2f}",
          f"{incometax:,.2f}", f"{netpay:,.2f}")

    TotEmployees += 1
    TotHours += hours
    TotGrossPay += grosspay
    TotTax += incometax
    TotNetPay += netpay

  EmpTotals["TotEmp"] = TotEmployees
  EmpTotals["TotHours"] = TotHours
  EmpTotals["TotGrossPay"] = TotGrossPay
  EmpTotals["TotTax"] = TotTax
  EmpTotals["TotNetPay"] = TotNetPay

  DetailsPrinted = True
  if (DetailsPrinted):
    PrintTotals(EmpTotals)
  else:
    print("No details found.")

def PrintTotals(EmpTotals):
  print()
  print(f"Total number of employees: {EmpTotals['TotEmp']}")
  print(f"Total number of hours worked: {EmpTotals['TotHours']:,.2f}")
  print(f"Total gross pay: ${EmpTotals['TotGrossPay']:,.2f}")
  print(f"Total income tax: ${EmpTotals['TotTax']:,.1%}")
  print(f"Total net pay: ${EmpTotals['TotNetPay']:,.2f}")

if __name__ == "__main__":
  CreateUsers()
  print()
  print("Data Entry")
  UserRole, UserName = Login()
  DetailsPrinted = False
  EmpTotals = {}
  if (UserRole.upper() == "NONE"):
    print(UserName, " is invalid.")
  else:
    if (UserRole.upper() == "ADMIN"):
      EmpFile = open("Employees.txt", "a+")
      while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
          break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
        EmpFile.write(EmpDetail)
      Empfile.close()
    printinfo(DetailsPrinted)