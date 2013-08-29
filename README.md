bandsaw
=======

A Python module for retrieving [Basis Band](http://www.mybasis.com/) data from the Basis website. It retrieves data from a date range and stores that data in a CSV file.

##Using Bandsaw
###Option 1
```
import bandsaw

create_csv()
for data in get_data('BASIS USER ID GOES HERE', datetime.datetime(2013, 8, 13), datetime.datetime(2013, 8, 28)):
  append_to_csv(data)
```

###Option 2
Edit the ```if __name__ == '__main__':``` section of bandsaw.py so that 'BASIS USER ID GOES HERE' is replaced with your user ID. Then, just run:

```
python bandsaw.py
```

##Finding your Basis user ID
See instructions in the [README for the PHP-based basis-data-export project](https://github.com/btroia/basis-data-export/blob/master/README.md).

