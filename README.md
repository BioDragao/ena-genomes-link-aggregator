# ena-genomes-link-aggregator

## STEP-1 : Aggregate the links using the excel file from Emilyn

- We did this via browser automation in `etaoin` and `clojure`

## STEP-2 : Download the links using an FTP enabled downloader

#### TRIAL-1 : Python script 

This didn't work since the speed of the Remote-database-server is not good at all!

#### TRIAL-2 : A Python package

https://github.com/julienc91/multidl

Didn't work in an assuring way.

#### TRIAL-3 : aria2

Have relied on `aria2` to download things in parallel.

```
 nohup aria2c -i urls.txt -j4 &
```


## STEP-3 : Upload all files in Emilyn's OneDrive


## License

Copyright © 2019 Abhinav Sharma ( @abhi18av )

Distributed under the Eclipse Public License either version 1.0 or (at
your option) any later version.
