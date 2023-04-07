def show():
	subprocess.run("docker ps -a", shell=True)
    #Bug: If docker daemon is not running we got 'error during connect' error (needs to be deleted)