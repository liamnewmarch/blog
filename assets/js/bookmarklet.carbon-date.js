javascript:(function(){var a,b;b={"1.0":[7,2006],"1.1":[0,2007],"1.2":[8,2007],"1.3":[0,2009],"1.4":[0,2010],"1.5":[0,2011],"1.6":[4,2011],"1.7":[10,2011],"1.8":[7,2012],"1.9":[0,2013],"2.0":[2,2013]};"jQuery"in window&&"fn"in jQuery&&"jquery"in jQuery.fn?(a=b[jQuery.fn.jquery.split(".").splice(0,2).join(".")],b=alert,a=4>a[0]?"early "+a[1]:7<a[0]?"late "+a[1]:"mid "+a[1],b("Found jQuery, version dated "+a)):alert("jQuery was not be found on this page")})()