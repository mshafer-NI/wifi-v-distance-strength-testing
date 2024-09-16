## Reports/output

Take a look at [charts](charts.html) and [the source notebook](notebook.html) to see the graphs.

## Data

Raw data is stored in [https://github.com/mshafer-ni/wifi-v-distance-strength-testing/data_files](https://github.com/mshafer-ni/wifi-v-distance-strength-testing/data_files)

## Testing Methodology

1. A DIR-820L D-Link access point (AC1200 Dual Band - DIR-820LB1) was placed on the ground in an open park (powered by a Ryobi One+ 18V inverter)
1. A 200' tape measure was run out from the access point.
1. A Motorala Edge (2022) was used to run the Ubiquiti WiFiman app to take measurements.
1. The phone was placed with screen up, top-towards the the access point, on the ground, with the top at the measurement point.
1. The phone was given 10 Seconds to stabilize the reading
1. Numbers were hand recorded as they were reported until at least 5 reported values were all previously seen.

## Visualization method

1. To plot the data from this recording method, the median value from each reading was plotted with the `max(max(values) - median), median - min(values))` value used for error.



## Observed issues

1. The app/phone updated more frequently if the network was connected; however, maintaining that connection was difficult. It may be good to repeat without connecting to the network.
1. As many as 7 other 2.4GHz networks could be seen at times (too far away to connect, although the desired access point was no longer the strongest observed signal beyond 150')
1. The Access Point chose channel 3. 4 of the observed other networks were on channel 3 as well (in conflict).
