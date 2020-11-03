#!/usr/bin/env python
import subprocess

def download_with_wget(link,file_name):
	program = "wget"
	arg1 = "--show-progress"
	arg2 = "--server-response"
	arg3 = "--continue"
	arg4 = "-O"
	subprocess.call([program,arg1,arg2,arg3,str(link),arg4,str(file_name)])

def download_with_curl(link,file_name):
	program = "curl"
	arg1 = "-L"
	arg2 = "--progress-bar"
	arg3 = "-Z"
	arg4 = "-o"
	subprocess.call([program,arg1,arg2,arg3,str(link),arg4,str(file_name)])