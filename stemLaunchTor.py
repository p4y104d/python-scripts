import stem.process
from stem.util import term

def logs_tor(log):
    if "Bootstrapped " in log:
        print term.format(log, term.Color.GREEN)

    tor_process = stem.process.launch_tor_with_config(config = {'SocksPort': '9000', 'ExitNodes': '{es}',}, init_msg_handler = logs_tor,)
