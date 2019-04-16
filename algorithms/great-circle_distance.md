# Great-circle distance

https://en.wikipedia.org/wiki/Great-circle_distance

```Python
# The [great-circle
# distance](https://en.wikipedia.org/wiki/Great-circle_distance) is the
# shortest distance between two points on the surface of a sphere.  In this
# example we create a user-defined function to compute the [haversine
# approximation](https://en.wikipedia.org/wiki/Haversine_formula) to
# the great-circle distance between the ride origin and destination.

# Define the haversine function (based on the code at
# [rosettacode.org](http://rosettacode.org/wiki/Haversine_formula#Python)):
from math import radians, sin, cos, sqrt, asin
def haversine(lat1, lon1, lat2, lon2):
  """
  Return the haversine approximation to the great-circle distance between two
  points (in meters).
  """
  R = 6372.8 # Earth radius in kilometers
 
  dLat = radians(lat2 - lat1)
  dLon = radians(lon2 - lon1)

  lat1 = radians(lat1)
  lat2 = radians(lat2)
 
  a = sin(dLat / 2.0)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2.0)**2
  c = 2.0 * asin(sqrt(a))
 
  return R * c * 1000.0
```
