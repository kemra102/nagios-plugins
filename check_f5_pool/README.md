# check_f5_pool

This Nagios check will check if members of an F5 pool are available.

Example usage:

```
# ./check_f5_pool -a https://f5.example.org -n ~partition-name_pool-name -u f5rouser -p myawesomempass
OK - All pool members in ~partition-name_pool-name are available.
# ./check_f5_pool -a https://f5.example.org -n ~partition-name_pool-name-broken -u f5rouser -p myawesomempass
WARNING - 2 pool members in ~partition-name_pool-name-broken are down!
```

This plugin reports the following Nagios plugin return types:

* 0 - OK - All pool memebers are up.
* 1 - WARNING - At least 1 pool member is down.
* 2 - CRITICAL - All pool members are down.
* 3 - UNKNOWN - Status of the pool members could not be determined.
