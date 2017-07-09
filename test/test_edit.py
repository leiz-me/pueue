from test.helper import command_factory, execute_add


def test_edit(daemon_setup):
    """It's possible to edit the command of a queue entry."""
    # Pause, add command and check that it has been added correctly
    command_factory('pause')()
    execute_add('ls')
    status = command_factory('status')()
    assert status['data'][0]['command'] == 'ls'
    assert status['data'][0]['path'] == '/tmp'

    # Edit the command
    command_factory('edit')({'key': 0, 'command': 'ls -al'})

    # Check for changed command
    status = command_factory('status')()
    assert status['data'][0]['command'] == 'ls -al'
    assert status['data'][0]['path'] == '/tmp'
