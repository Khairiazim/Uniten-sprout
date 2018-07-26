import winreg

API_URL = 'https://www.virtualmode.com.my/'
API_KEY = '9858c876d5bba2a0d928923e0218cd1b0ae7792a'
SESSION_DATA = {}
#window//
def get_machine_guid():
	try:
	    key = winreg.OpenKey(
	        winreg.HKEY_LOCAL_MACHINE,
	        "SOFTWARE\\Microsoft\\Cryptography",
	        0,
	        winreg.KEY_READ | winreg.KEY_WOW64_64KEY
	    )

	    result = winreg.QueryValueEx(key, "MachineGuid")
	    return result[0]
	except:
	    key = winreg.OpenKey(
	        winreg.HKEY_LOCAL_MACHINE,
	        "SOFTWARE\\Microsoft\\Cryptography",
	        0
	    )

	    result = winreg.QueryValueEx(key, "MachineGuid")
	    return result[0]