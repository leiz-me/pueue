# Change Log

All notable changes to this project will be documented in this file.

## [1.0.1]
### Fixed
- Argparse help messages

### Added
- Script for checking remote status of pueue with ssh


## [1.0.0]
### Added
- Tests and travis support. Stable release


## [0.9.2]
### Changed
- Some additions and changes in the zsh auto-completion script

### Fixed
- Multi client socket handling.


## [0.9.0]
### Added
- `edit` subcommand.
    This command takes a key and opens your `$EDITOR` to update a command in the queue.

### Fixed
- Fixed logic bug, which showed all entries in the log data instead of only finished entries.
- Fixed wrong queue log path. Queues will now be restored properly after restart again.


## [0.8.7]
### Fixed
- Prevent daemon crash if subprocesses contain invalid UTF-8 characters in `stderr` or `stdout`.


## [0.8.6]
### Fixed
- Prevent a daemon crash, if the client dies while daemon sends data.
- Prevent endless loop if client dies while daemon receives data, because of unmanaged client socket.


## [0.8.5]
### Fixed
- Prevent a daemon crash, if the client dies while daemon receives data.


## [0.8.4]
### Fixed
- Fix default shell set function


## [0.8.3]
### Added
- Allow to set a custom shell instead of `/bin/sh`.
    This is done by callingthe `pueue config customShell`. Use `default` for `/bin/sh`.
    By setting a custom shell it's possible to use aliases or environment variables.
    Be careful! This probably causes some bugs, as every shell behaves differently.

## [0.8.2]
### Changed
- The `kill` command has been remodeled. Instead of always sending an `SigKill` it now allows you to specify the signal that should be sent (default is `SIGTERM`).  
    By default the signal will be sent to the processes spawned by the `shell` parent process. The new `-a/--all` flag is provided in case you want to send the signal to the parent process as well.  
    Available signals can be viewed with `pueue kill -h` under the `-s` flag. Either the int `15` the full name `sigterm/SIGTERM` or the abbreviation `term/TERM` can be used.  
    For now we support: SIGHUP, SIGINT, SIGQUIT, SIGKILL, SIGTERM, SIGCONT, SIGSTOP
- The `stop` command has been removed, as it is now covered by the `kill` command


## [0.8.1]
### Fixed
- Fixed missing return message for `send`.
- Write queue more often. This prevents entries from disappearing after reboot.
- Set `paused` entries to `queued` on restart.


## [0.8.0]
### Added
- Allow switching of `stashed` entries in queue.

### Changed
- `remove`, `restart`, `stash`, `enqueue` commands can receive multiple keys instead of a single key.
- `log`, `pause`, `start`, `kill`, `stop` commands don't have a `--key` parameter anymore. They can now receive a list of keys without providing a flag i.e. `pueue start 0 1` instead of `pueue start -k 0 && pueue start -k 1`. The default behavior if no key is provided stays the same for all commands.
- Daemon API now requires a `keys` parameter where `type(keys) == list` for the commands listed above.

### Fixed
- Fixed daemon crash when restarting a non-existing entry.
- Fixed client crash for empty queue with `show`.
- Fixed client crash for invalid key with `show`.
- Wrong daemon response for `kill` command.
- `stop` or `kill` sends the signal to all processes spawned by the shell process. This bug affected all command strings which caused the subprocess to spawn a `/bin/sh -c {command}` process.
- `pause` or `start` sends the signal to all processes spawned by the shell process. This bug affected all command strings which caused the subprocess to spawn a `/bin/sh -c {command}` process.
