import os


def cleanup(config_dir):
    """Removes temporary stderr and stdout files as well as the daemon socket."""

    stdout_path = os.path.join(config_dir, 'pueue.stdout')
    stderr_path = os.path.join(config_dir, 'pueue.stderr')
    if os._exists(stdout_path):
        os.remove(stdout_path)
    if os._exists(stderr_path):
        os.remove(stderr_path)

    socketPath = os.path.join(config_dir, 'pueue.sock')
    if os.path.exists(socketPath):
        os.remove(socketPath)


def get_descriptor_output(descriptor, key, handler=None):
    """Get the descriptor output and handle incorrect UTF-8 encoding of subprocess logs.

    In case an process contains valid UTF-8 lines as well as invalid lines, we want to preserve
    the valid and remove the invalid ones.
    To do this we need to get each line and check for an UnicodeDecodeError.
    """
    line = 'stub'
    lines = ''
    while line != '':
        try:
            line = descriptor.readline()
            lines += line
        except UnicodeDecodeError:
            error_msg = "Error while decoding output of process {}".format(key)
            if handler:
                handler.logger.error("{} with command {}".format(
                    error_msg, handler.queue[key]['command']))
            lines += error_msg + '\n'
    return lines.replace('\n', '\n    ')
