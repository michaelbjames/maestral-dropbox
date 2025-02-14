[![PyPi Release](https://img.shields.io/pypi/v/maestral.svg)](https://pypi.org/project/maestral/)
[![Pyversions](https://img.shields.io/pypi/pyversions/maestral.svg)](https://pypi.org/pypi/maestral/)

# Maestral <img src="https://raw.githubusercontent.com/SamSchott/maestral-dropbox/master/maestral/gui/resources/Maestral.png" align="right" title="Maestral" width="110" height="110">

A light-weight and open-source Dropbox client for macOS and Linux.

## About

Maestral is an open-source Dropbox client written in Python. The project's main goal is to
provide a client for platforms and file systems that are no longer directly supported by
Dropbox.

Currently, Maestral does not support Dropbox Paper, the management of Dropbox teams and
the management of shared folder settings. If you need any of this functionality, please
use the Dropbox website or the official client. As of version 0.3.0, Maestral does
support the syncing of multiple Dropbox accounts.

The focus on "simple" file syncing does come with advantages: the Maestral App on macOS is
80% smaller than the official Dropbox app (50 MB vs 290 MB) and uses 70% less memory. The
app size and memory footprint can be further reduced when installing and running Maestral
without a GUI and using the Python installation provided by your OS. The Maestral code
itself and its Python dependencies take up less than 3 MB,  making an install without GUI
ideal for systems with little resources.

## Installation

A binary is provided for macOS High Sierra and higher and can be downloaded from the
Releases tab. On other platforms, download and install the Python package from PyPI:
```console
$ python3 -m pip install --upgrade maestral
```
You can also install the latest beta:
```console
$ python3 -m pip install --upgrade --pre maestral
```
If you intend to use the graphical user interface, you also need to install PyQt5, either
from PyPI or form your platforms package manager.

## Usage

Run `maestral gui` in the command line (or open the Maestral app on macOS) to start
Maestral with a graphical user interface. On its first run, Maestral will guide you
through linking and configuring your Dropbox and will then start syncing.

![screenshot macOS](https://raw.githubusercontent.com/SamSchott/maestral-dropbox/master/screenshots/macOS.png)
![screenshot Fedora](https://raw.githubusercontent.com/SamSchott/maestral-dropbox/master/screenshots/Ubuntu.png)

## Command line usage

After installation, Maestral will be available as a command line script by typing
`maestral` in the command prompt. Type `maestral --help` to get a full list of available
commands. The most important are:

- `maestral gui`: Starts Maestral with a GUI.
- `maestral daemon {start/stop}`: Starts or stops Maestral as a daemon.
- `maestral daemon {pause/resume}`: Pauses or resumes syncing.
- `maestral daemon status`: Gets the current sync status.
- `maestral daemon errors`: Lists all sync errors.
- `maestral set-dir`: Sets the location of your local Dropbox folder.
- `maestral dir-exclude`: Excludes a Dropbox folder from syncing.
- `maestral dir-inlcude`: Includes a Dropbox folder in syncing.
- `maestral ls`: Lists the contents of a directory on Dropbox.
- `maestral log`: Command group to show and clear logs, to set the log level, etc.

Maestral currently supports the syncing of multiple Dropbox accounts by running multiple
instances. This needs to be configured from the command line. For example, before running
`maestral gui`, one can set up a new configuration with `maestral config new`. The
configuration name should then be given as command line option `--config-name` before
running maestral. For example:

```shell
$ maestral config new "personal"
$ maestral config new "work"
$ maestral gui --config-name="personal"
$ maestral gui --config-name="work"
```
This will start two instances of Maestral, syncing a private and a work account,
respectively. Multiple Maestral daemons are supported as well.

By default, the Dropbox folder names will contain the capitalised config-name in braces.
In the above case, this will be "Dropbox (Personal)" and "Dropbox (Work)".

## Contribute

The following tasks could need your help:

- [ ] Write tests for Maestral.
- [ ] Detect and warn in case of unsupported Dropbox folder locations (network drives,
      external hard drives, etc).
- [ ] Native Cocoa and GTK interfaces. Maestral currently uses PyQt5.
- [ ] Packaging: improve packing for macOS (reduce app size) and package for other platforms.

## Warning:

- Maestral is still in beta status. Even though highly unlikely, using it may potentially
  result in loss of data.
- Network drives and some external hard drives are not supported as locations for the
  Dropbox folder.

## Dependencies

- macOS (10.13 or higher for binary) or Linux
- Python 3.6 or higher
- For the GUI only:
  - PyQt 5.9 or higher
  - [gnome-shell-extension-appindicator](https://github.com/ubuntu/gnome-shell-extension-appindicator)
    on Gnome 3.26 and higher

# Acknowledgements

- The config module uses code from the [Spyder IDE](https://github.com/spyder-ide).
- The MaestralApiClient is based on the work from [Orphilia](https://github.com/ksiazkowicz/orphilia-dropbox).
