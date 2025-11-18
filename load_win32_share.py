# load_win32_share.py
# Low-level Windows CreateFile + ReadFile approach to open a file with sharing flags
# This uses ctypes to call CreateFileW with FILE_SHARE_READ|FILE_SHARE_WRITE|FILE_SHARE_DELETE.
# It then reads the file bytes and passes them to pandas.

import ctypes
from ctypes import wintypes
import io
import pandas as pd
from pathlib import Path
import sys

path = r"C:\Temp\healthcare_dataset.csv"
p = Path(path)
print("Path exists:", p.exists())

# Constants
GENERIC_READ  = 0x80000000
OPEN_EXISTING = 3
FILE_SHARE_READ  = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE= 0x00000004
FILE_ATTRIBUTE_NORMAL = 0x80

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

CreateFileW = kernel32.CreateFileW
CreateFileW.argtypes = [
    wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
    wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE
]
CreateFileW.restype = wintypes.HANDLE

ReadFile = kernel32.ReadFile
ReadFile.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.DWORD,
                     ctypes.POINTER(wintypes.DWORD), wintypes.LPVOID]
ReadFile.restype = wintypes.BOOL

CloseHandle = kernel32.CloseHandle
CloseHandle.argtypes = [wintypes.HANDLE]
CloseHandle.restype = wintypes.BOOL

INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value

def read_file_bytes_win(path):
    h = CreateFileW(path,
                    GENERIC_READ,
                    FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
                    None,
                    OPEN_EXISTING,
                    FILE_ATTRIBUTE_NORMAL,
                    None)
    if h == INVALID_HANDLE_VALUE or h == 0:
        err = ctypes.get_last_error()
        raise OSError(f"CreateFileW failed. GetLastError: {err}")
    try:
        # get file size
        # use GetFileSizeEx
        filesize = ctypes.c_longlong(0)
        ok = kernel32.GetFileSizeEx(h, ctypes.byref(filesize))
        if not ok:
            raise OSError("GetFileSizeEx failed")
        size = int(filesize.value)
        buf = (ctypes.c_ubyte * size)()
        read = wintypes.DWORD(0)
        ok = ReadFile(h, ctypes.byref(buf), size, ctypes.byref(read), None)
        if not ok:
            err = ctypes.get_last_error()
            raise OSError(f"ReadFile failed. GetLastError: {err}")
        data = bytes(buf[:read.value])
        return data
    finally:
        CloseHandle(h)

try:
    b = read_file_bytes_win(path)
    print("Read bytes:", len(b))
    df = pd.read_csv(io.BytesIO(b))
    print("Loaded rows,cols:", df.shape)
    print(df.head(5).to_string())
except Exception as e:
    print("ERROR:", repr(e))
    print("If this still fails, please try these quick checks:")
    print("  * Temporarily disable Controlled Folder Access in Windows Security (Ransomware protection).")
    print("  * Try opening the CSV in Notepad and re-saving as a new file in C:\\Temp (File → Save As).")
    print("  * If corporate device, IT policy may block programmatic read; try the Notepad Save-As workaround.")
    sys.exit(1)
