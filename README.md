Insulware
========

#Overview#
This is just some scripts and config files for BGM / insulin pump auditing. 
Also contains scripts/config files for interacting with 3G modems. 
Any thing else that's small, self-contained, and should be shipped on the 'bone will be here if it doesn't fit somewhere else. 

# Blood Glucose Meter #

# Insulin pump #

# 3G/Modem/network #
There's a script in `/usr/bin/` to parse SMS config texts. 
It depends on cgmpy.

# Miscellany #
We are interested in low power stuff. 
There's a systemd style startup script to set some of the lower power params and load modules we'll need.

TODO:
http://www.compulab.co.il/workspace/mediawiki/index.php5/CM-T3530:_Linux:_Power_management
Look at sleep mode and using the internal timers.

some info on OMAP3 power management
http://elinux.org/OMAP_Power_Management


