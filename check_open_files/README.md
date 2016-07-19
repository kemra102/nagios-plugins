# check_open_files

This Nagios check will check the number of files the specified user has open.

Example usage:

```
# ./check_open_files -u nrpe
OK - nrpe has 13185 open files.
# ./check_open_files -u myappuser
WARNING - myappuser has 113185 open files!
```

This plugin reports the following Nagios plugin return types:

* 0 - OK - User has not crossed the warning or critical thresholds for number of open files.
* 1 - WARNING - User has crossed the warning threshold for number of open files.
* 2 - CRITICAL - User has crossed the critical threshold for number of open files.
* 3 - UNKNOWN - Unable to determine the number of files the user has open.

## Requirements

The following packages must be installed:

* ruby
* sudo
* bash

The default thresholds are:

* Warning: 65%
* Critical: 85%
