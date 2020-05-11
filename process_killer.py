import commands
import getpass
import os
import sys
import time

def start():
  processPath = '/Applications/Spotify.app/Contents/MacOS/Spotify' # sys.argv[1]
  
  try:
    killInSec = int(sys.argv[1])  # int(sys.argv[2))
  except:
    print "Must has time in seconds as 1. argument "
    return 0

  if not processPath.startswith('/Applications/'):
    print "Processes must run from '/Applications/*'"
    return 0

  # Get PID
  process = commands.getstatusoutput('ps -ax | grep "%s" | grep -v grep' % processPath)

  try:
    processSplit = process[1].split(" ")
    pid = processSplit[0] if processSplit[0] else processSplit[1]
  except:
    print "No process running with with path '%s'" % processPath
    return 0

  # Prepare
  pw = getpass.getpass(prompt='Password: ', stream=None)

  if 'incorrect' in commands.getstatusoutput('echo %s|sudo -S ls -l %s' % (pw, processPath))[1]:
    print "Password invalid"
    return 0

  # Sleep
  print "Process with PID %s will be killed in %s minute/s" % (pid, int(killInSec))
  time.sleep(60 * killInSec)

  # Kill
  os.system('echo %s|sudo -S %s' % (pw, 'sudo kill ' + pid))


if __name__ == "__main__":
  start()