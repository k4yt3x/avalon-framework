# AVALON FRAMEWORK

Current Version: 1.5.3

### Avalon Framework is a library that can make python printing in Linux much easier.

<b>It includes:</b> 
1. All Linux Terminal 16 bit Foreground Color
2. All Linux Terminal 16 bit Background Color
3. Beautiful printing such as 'Info', 'Warning', 'Error' and etc.

Easiest way to get user True or False input:
~~~~
if avalon.ask("Question?", True):  # Default is True
    print("True!")
~~~~

#
### Screenshots
This is how it looks like:
![avlaon_framework](https://user-images.githubusercontent.com/21986859/31029604-56f3a1ec-a520-11e7-94fd-361ff9a43ed3.png)


### Usages Examples
~~~~
import avalon_framework as avalon

avalon.info("Output green information here")
avalon.warning("This outputs yellow bold warnings")
avalon.error("This prints a red bold error")
avalon.subLevelTimeInfo("This prints detailed time and grey info")
avalon.ask("Returns true if user selects y, vice versa")
~~~~