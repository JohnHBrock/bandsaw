bandsaw
=======

A Python module for retrieving and processing [Basis Band](http://www.mybasis.com/) data.

## Using Bandsaw
```
import bandsaw

create_csv()
for data in get_data('BASIS USER ID GOES HERE', datetime.datetime(2013, 8, 13), datetime.datetime(2013, 8, 28)):
  append_to_csv(data)
```

## Finding your Basis user ID
See instructions in the [README for the PHP-based basis-data-export project](https://github.com/btroia/basis-data-export/blob/master/README.md).

