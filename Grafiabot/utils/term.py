import subprocess

from Bestie_Robot.utils.logger import log


def term(cmd):
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    if p.stderr:
        log.error(p.stderr.readlines())
    return p.stdout.readlines()
