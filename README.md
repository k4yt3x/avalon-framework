# Avalon Framework

## 1.8.0

- Replaced `.format` with f-string
- Added default return values for gets
  - If default value is set and user input is blank, default value is returned
- Added docstring for every staticmethod, including description for parameters and return values

## Description

Avalon framework makes printing messages and getting user input easier. It includes all UNIX terminal 16 bit colors, ans is also **compatible with Windows** environments with the help of `colorama`.

### Included Features

- All Linux terminal 16 bit foreground color
- All Linux terminal 16 bit background color
- Standardized printing for info, warning, debug, error and etc.
- The ability to log to syslog
- The ability to specify output pipe (stdout, stderr, etc.)
- Easiest way to get user True or False input

    ```python
    if Avalon.ask('Question?', True):  # Default is True
        print('True!')
    ```

### Screenshots (To be Updated)

![avlaon_framework](https://user-images.githubusercontent.com/21986859/31029604-56f3a1ec-a520-11e7-94fd-361ff9a43ed3.png)

## Usages Examples

### Printing Messages

Avalon Framework includes a few built-in static methods for printing information to terminal.

- Avalon.info
- Avalon.warning
- Avalon.error
- Avalon.debug
- Avalon.debug_info

All of these methods have the same parameters. `Avalon.info`, for example, works as the following.

```python
Avalon.info(msg, log=False, file=sys.stdout)
```

- `msg` is the message to be printed
- `log` is a boolean value, where `True` means to log information to syslog if the system supports syslog
- `file` is takes a `_io.TextIOWrapper` object, i.e. a pipe to write the message into if the user wants to overwrite the default values

### Getting User String Input

To get user input as a string, Avalon Framework provided the `Avalon.gets` method.

```python
Avalon.gets(msg, default=None, batch=False, file=sys.stdout)
```

- `msg` is the message to be printed
- `default` is the default value to return when `batch` is True, or when user input is empty
- `batch` tells the function to return its default value without asking the user for input
- `file` is takes a `_io.TextIOWrapper` object, i.e. a pipe to write the message into if the user wants to overwrite the default values

### Asking a Yes or No Question

Avalon Framework provides a simple way to ask users a Yes or No question with `Avalon.ask`.

```python
Avalon.ask(msg, default=False, batch=False)
```

- `msg` is the message to be printed
- `default` is the default value to return when user input is blank
- `batch` tells the function to return its default value without asking the user for input

### Thread-Safe Printing

You may create a thread lock to make multi-threaded printing thread-safe.

```python
import threading
Avalon.thread_lock = threading.Lock()
Avalon.info('Here\'s a message')
```
