


# Note: Add number to fast track the code
# This code is for a simple attendance update message generator.




day = input("Choose: Morning, Afternoon, or Evening? ").strip().lower()
date = input("Enter a date (MM/DD/YYYY): ")


oShift1 = input("Choose Opening Shift: Refiller, Cashier, or TL/Refiller? ").strip()
nStaff1 = input("Enter number of staff for Opening Shift (eg. 2/2): ").strip()
oShift2 = input("Choose Opening Shift: Refiller, Cashier, or TL/Refiller?: ").strip()
nStaff2 = input("Enter number of staff for Opening Shift (eg. 2/2): ").strip()

cShift1 = input("Choose Closing Shift: Refiller, Cashier, or TL/Refiller? ").strip()
n1Staff1 = input("Enter number of staff for Opening Shift (eg. 2/2): ").strip()
cShift2 = input("Choose Closing Shift: Refiller, Cashier, or TL/Refiller?: ").strip()
n1Staff2 = input("Enter number of staff for Opening Shift (eg. 2/2): ").strip()


thc = input("Enter Total HC: ").strip()




frmt = F"""Best {day} and Mabuhay!

Attendance Update
{date}

EMR - ISA

OPENING SHIFT:
  • {oShift1} - {nStaff1}
  • {oShift2} - {nStaff2}

CLOSING SHIFT:
  • {cShift1} - {n1Staff1}
  • {cShift2} - {n1Staff2}


Total HC: {thc}"""




print(frmt)