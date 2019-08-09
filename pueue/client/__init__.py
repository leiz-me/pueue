import os
import pickle


def get_queue(config_dir):
    """Get the queue from the queue backup file."""
    queue_path = os.path.join(config_dir, 'queue')
    if os.path.exists(queue_path):
        queue_file = open(queue_path, 'rb')
        try:
            queue = pickle.load(queue_file)
            return queue
        except Exception:
            print('Queue log file seems to be corrupted. Aborting.')
            return None
        queue_file.close()

    print('There is no queue log file. Aborting.')
    return None
