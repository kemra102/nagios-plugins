# check_service

This Nagios check will check if a Linux service is running and supports the following init types:

* systemd
* upstart
* supervisord

The `systemd` & `upstart` init types are selected automatically based on the distro being ran.

The init type for a check can be overridden using the `-i` option.

> NOTE: This is the only way to check a `supervisord` service.

Example usage:

```
# ./check_service cron
OK - cron is running
# ./check_service sshd
CRITICAL - sshd is not running
```

This plugin reports the following Nagios plugin return types:

* 0 - OK - Service is running.
* 2 - CRITICAL - Service is not running.
* 3 - UNKNOWN - Service status cannot be determined.

> NOTE: The keen eyed observer will notice that there is no 1 AKA WARNING status like there is with other plugins.
