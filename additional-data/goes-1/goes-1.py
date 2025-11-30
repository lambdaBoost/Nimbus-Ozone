#!/usr/bin/env python
import urllib.request

################################################################################
#
# Title       : GOES1_d19790921t000000_d19790921t233000.py
# Description : This script will download the specified GOES-1 data from
#               the MCFETCH API.
# Author      : SSEC Satellite Data Services
# Date        : 2025-11-30 20:54 UTC
# Usage       : python GOES1_d19790921t000000_d19790921t233000.py
# Notes       : Run this script from the directory in which you want the data.
#               This script must be made executable in order to run.
#                 On linux and mac machines:
#                   chmod a+x GOES1_d19790921t000000_d19790921t233000.py
#
# For obtaining a free MCFETCH API key, please refer to the following link:
# https://mcfetch.ssec.wisc.edu/#register
#
# Search URL:
# https://inventory.ssec.wisc.edu/inventory/#search&start_time:1979-09-21%2000:00;end_time:1979-09-21%2023:59;
#
# DISCLAIMER: BY USING THIS SCRIPT, YOU WILL BE MAKING DATA REQUESTS TO THE
# MCFETCH SERVER THAT MAY IMPACT THE DATA QUOTA OF YOUR ACCOUNT. IF YOU EXCEED
# THIS QUOTA, YOUR ACCOUNT MAY BECOME LIMITED IN TERMS OF DATA REQUESTS AND
# YOU MIGHT LOSE THE ABILITY TO DOWNLOAD DATA FROM THIS SERVER.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
################################################################################

KEY="YOUR KEY HERE"

HTTP="https://mcfetch.ssec.wisc.edu/cgi-bin/mcfetch?dkey={0}&satellite=GOES1&output=JPG&size=2000+2000".format(KEY)

COMMANDS =[
"date=19790921&time=00:00:00&coverage=MODE-A&band=1",
"date=19790921&time=00:30:00&coverage=MODE-A&band=1",
"date=19790921&time=01:00:00&coverage=MODE-A&band=1",
"date=19790921&time=01:30:00&coverage=MODE-A&band=1",
"date=19790921&time=02:00:00&coverage=MODE-A&band=1",
"date=19790921&time=02:30:00&coverage=MODE-A&band=1",
"date=19790921&time=03:00:00&coverage=MODE-A&band=1",
"date=19790921&time=03:30:00&coverage=MODE-A&band=1",
"date=19790921&time=04:00:00&coverage=MODE-A&band=1",
"date=19790921&time=04:30:00&coverage=MODE-A&band=1",
"date=19790921&time=05:00:00&coverage=MODE-A&band=1",
"date=19790921&time=05:30:00&coverage=MODE-A&band=1",
"date=19790921&time=06:00:00&coverage=MODE-A&band=1",
"date=19790921&time=06:30:00&coverage=MODE-A&band=1",
"date=19790921&time=07:00:00&coverage=MODE-A&band=1",
"date=19790921&time=07:30:00&coverage=MODE-A&band=1",
"date=19790921&time=08:00:00&coverage=MODE-A&band=1",
"date=19790921&time=08:15:00&coverage=MODE-A&band=1",
"date=19790921&time=08:30:00&coverage=MODE-A&band=1",
"date=19790921&time=08:45:00&coverage=MODE-A&band=1",
"date=19790921&time=09:00:00&coverage=MODE-A&band=1",
"date=19790921&time=09:30:00&coverage=MODE-A&band=1",
"date=19790921&time=10:00:00&coverage=MODE-A&band=1",
"date=19790921&time=10:30:00&coverage=MODE-A&band=1",
"date=19790921&time=11:00:00&coverage=MODE-A&band=1",
"date=19790921&time=11:30:00&coverage=MODE-A&band=1",
"date=19790921&time=12:00:00&coverage=MODE-A&band=1",
"date=19790921&time=12:30:00&coverage=MODE-A&band=1",
"date=19790921&time=13:00:00&coverage=MODE-A&band=1",
"date=19790921&time=13:30:00&coverage=MODE-A&band=1",
"date=19790921&time=14:00:00&coverage=MODE-A&band=1",
"date=19790921&time=14:30:00&coverage=MODE-A&band=1",
"date=19790921&time=15:00:00&coverage=MODE-A&band=1",
"date=19790921&time=15:30:00&coverage=MODE-A&band=1",
"date=19790921&time=16:00:00&coverage=MODE-A&band=1",
"date=19790921&time=16:30:00&coverage=MODE-A&band=1",
"date=19790921&time=17:00:00&coverage=MODE-A&band=1",
"date=19790921&time=17:30:00&coverage=MODE-A&band=1",
"date=19790921&time=18:00:00&coverage=MODE-A&band=1",
"date=19790921&time=18:30:00&coverage=MODE-A&band=1",
"date=19790921&time=19:00:00&coverage=MODE-A&band=1",
"date=19790921&time=19:30:00&coverage=MODE-A&band=1",
"date=19790921&time=20:00:00&coverage=MODE-A&band=1",
"date=19790921&time=20:30:00&coverage=MODE-A&band=1",
"date=19790921&time=20:45:00&coverage=MODE-A&band=1",
"date=19790921&time=21:00:00&coverage=MODE-A&band=1",
"date=19790921&time=21:30:00&coverage=MODE-A&band=1",
"date=19790921&time=22:00:00&coverage=MODE-A&band=1",
"date=19790921&time=22:30:00&coverage=MODE-A&band=1",
"date=19790921&time=23:00:00&coverage=MODE-A&band=1",
"date=19790921&time=23:30:00&coverage=MODE-A&band=1"
]

FILENAMES=[
"GOES1_d19790921_t000000_b01",
"GOES1_d19790921_t003000_b01",
"GOES1_d19790921_t010000_b01",
"GOES1_d19790921_t013000_b01",
"GOES1_d19790921_t020000_b01",
"GOES1_d19790921_t023000_b01",
"GOES1_d19790921_t030000_b01",
"GOES1_d19790921_t033000_b01",
"GOES1_d19790921_t040000_b01",
"GOES1_d19790921_t043000_b01",
"GOES1_d19790921_t050000_b01",
"GOES1_d19790921_t053000_b01",
"GOES1_d19790921_t060000_b01",
"GOES1_d19790921_t063000_b01",
"GOES1_d19790921_t070000_b01",
"GOES1_d19790921_t073000_b01",
"GOES1_d19790921_t080000_b01",
"GOES1_d19790921_t081500_b01",
"GOES1_d19790921_t083000_b01",
"GOES1_d19790921_t084500_b01",
"GOES1_d19790921_t090000_b01",
"GOES1_d19790921_t093000_b01",
"GOES1_d19790921_t100000_b01",
"GOES1_d19790921_t103000_b01",
"GOES1_d19790921_t110000_b01",
"GOES1_d19790921_t113000_b01",
"GOES1_d19790921_t120000_b01",
"GOES1_d19790921_t123000_b01",
"GOES1_d19790921_t130000_b01",
"GOES1_d19790921_t133000_b01",
"GOES1_d19790921_t140000_b01",
"GOES1_d19790921_t143000_b01",
"GOES1_d19790921_t150000_b01",
"GOES1_d19790921_t153000_b01",
"GOES1_d19790921_t160000_b01",
"GOES1_d19790921_t163000_b01",
"GOES1_d19790921_t170000_b01",
"GOES1_d19790921_t173000_b01",
"GOES1_d19790921_t180000_b01",
"GOES1_d19790921_t183000_b01",
"GOES1_d19790921_t190000_b01",
"GOES1_d19790921_t193000_b01",
"GOES1_d19790921_t200000_b01",
"GOES1_d19790921_t203000_b01",
"GOES1_d19790921_t204500_b01",
"GOES1_d19790921_t210000_b01",
"GOES1_d19790921_t213000_b01",
"GOES1_d19790921_t220000_b01",
"GOES1_d19790921_t223000_b01",
"GOES1_d19790921_t230000_b01",
"GOES1_d19790921_t233000_b01"
]

for i, command in enumerate(COMMANDS):
    urllib.request.urlretrieve("{0}&{1}".format(HTTP, command), FILENAMES[i])