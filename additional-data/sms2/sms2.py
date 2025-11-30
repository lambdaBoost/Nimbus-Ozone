#!/usr/bin/env python
import urllib.request

################################################################################
#
# Title       : SMS2_d19790922t001500_d19790922t234500.py
# Description : This script will download the specified SMS-2 data from
#               the MCFETCH API.
# Author      : SSEC Satellite Data Services
# Date        : 2025-11-30 20:16 UTC
# Usage       : python SMS2_d19790922t001500_d19790922t234500.py
# Notes       : Run this script from the directory in which you want the data.
#               This script must be made executable in order to run.
#                 On linux and mac machines:
#                   chmod a+x SMS2_d19790922t001500_d19790922t234500.py
#
# For obtaining a free MCFETCH API key, please refer to the following link:
# https://mcfetch.ssec.wisc.edu/#register
#
# Search URL:
# https://inventory.ssec.wisc.edu/inventory/#search&start_time:1979-09-22%2000:00;end_time:1979-09-22%2023:59;
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

KEY="<YOUR KEY HERE"

HTTP="https://mcfetch.ssec.wisc.edu/cgi-bin/mcfetch?dkey={0}&satellite=SMS2&output=JPG&size=2000+2000".format(KEY)

COMMANDS =[
"date=19790922&time=00:15:00&coverage=MODE-A&band=1",
"date=19790922&time=00:30:00&coverage=MODE-A&band=1",
"date=19790922&time=00:45:00&coverage=MODE-A&band=1",
"date=19790922&time=01:00:00&coverage=MODE-A&band=1",
"date=19790922&time=01:15:00&coverage=MODE-A&band=1",
"date=19790922&time=01:30:00&coverage=MODE-A&band=1",
"date=19790922&time=01:45:00&coverage=MODE-A&band=1",
"date=19790922&time=02:00:00&coverage=MODE-A&band=1",
"date=19790922&time=02:15:00&coverage=MODE-A&band=1",
"date=19790922&time=02:30:00&coverage=MODE-A&band=1",
"date=19790922&time=03:00:00&coverage=MODE-A&band=1",
"date=19790922&time=03:30:00&coverage=MODE-A&band=1",
"date=19790922&time=04:00:00&coverage=MODE-A&band=1",
"date=19790922&time=04:30:00&coverage=MODE-A&band=1",
"date=19790922&time=05:00:00&coverage=MODE-A&band=1",
"date=19790922&time=05:30:00&coverage=MODE-A&band=1",
"date=19790922&time=06:00:00&coverage=MODE-A&band=1",
"date=19790922&time=06:30:00&coverage=MODE-A&band=1",
"date=19790922&time=07:00:00&coverage=MODE-A&band=1",
"date=19790922&time=07:30:00&coverage=MODE-A&band=1",
"date=19790922&time=08:00:00&coverage=MODE-A&band=1",
"date=19790922&time=08:30:00&coverage=MODE-A&band=1",
"date=19790922&time=09:00:00&coverage=MODE-A&band=1",
"date=19790922&time=09:30:00&coverage=MODE-A&band=1",
"date=19790922&time=10:00:00&coverage=MODE-A&band=1",
"date=19790922&time=10:30:00&coverage=MODE-A&band=1",
"date=19790922&time=11:00:00&coverage=MODE-A&band=1",
"date=19790922&time=11:30:00&coverage=MODE-A&band=1",
"date=19790922&time=12:00:00&coverage=MODE-A&band=1",
"date=19790922&time=12:30:00&coverage=MODE-A&band=1",
"date=19790922&time=13:00:00&coverage=MODE-A&band=1",
"date=19790922&time=13:30:00&coverage=MODE-A&band=1",
"date=19790922&time=14:00:00&coverage=MODE-A&band=1",
"date=19790922&time=14:30:00&coverage=MODE-A&band=1",
"date=19790922&time=15:00:00&coverage=MODE-A&band=1",
"date=19790922&time=15:30:00&coverage=MODE-A&band=1",
"date=19790922&time=16:00:00&coverage=MODE-A&band=1",
"date=19790922&time=16:30:00&coverage=MODE-A&band=1",
"date=19790922&time=17:00:00&coverage=MODE-A&band=1",
"date=19790922&time=17:30:00&coverage=MODE-A&band=1",
"date=19790922&time=17:43:00&coverage=MODE-A&band=1",
"date=19790922&time=17:49:00&coverage=MODE-A&band=1",
"date=19790922&time=18:30:00&coverage=MODE-A&band=1",
"date=19790922&time=18:43:00&coverage=MODE-A&band=1",
"date=19790922&time=18:50:00&coverage=MODE-A&band=1",
"date=19790922&time=19:00:00&coverage=MODE-A&band=1",
"date=19790922&time=19:30:00&coverage=MODE-A&band=1",
"date=19790922&time=20:00:00&coverage=MODE-A&band=1",
"date=19790922&time=20:30:00&coverage=MODE-A&band=1",
"date=19790922&time=21:00:00&coverage=MODE-A&band=1",
"date=19790922&time=21:30:00&coverage=MODE-A&band=1",
"date=19790922&time=22:00:00&coverage=MODE-A&band=1",
"date=19790922&time=22:30:00&coverage=MODE-A&band=1",
"date=19790922&time=23:00:00&coverage=MODE-A&band=1",
"date=19790922&time=23:30:00&coverage=MODE-A&band=1",
"date=19790922&time=23:45:00&coverage=MODE-A&band=1"
]

FILENAMES=[
"SMS2_d19790922_t001500_b01",
"SMS2_d19790922_t003000_b01",
"SMS2_d19790922_t004500_b01",
"SMS2_d19790922_t010000_b01",
"SMS2_d19790922_t011500_b01",
"SMS2_d19790922_t013000_b01",
"SMS2_d19790922_t014500_b01",
"SMS2_d19790922_t020000_b01",
"SMS2_d19790922_t021500_b01",
"SMS2_d19790922_t023000_b01",
"SMS2_d19790922_t030000_b01",
"SMS2_d19790922_t033000_b01",
"SMS2_d19790922_t040000_b01",
"SMS2_d19790922_t043000_b01",
"SMS2_d19790922_t050000_b01",
"SMS2_d19790922_t053000_b01",
"SMS2_d19790922_t060000_b01",
"SMS2_d19790922_t063000_b01",
"SMS2_d19790922_t070000_b01",
"SMS2_d19790922_t073000_b01",
"SMS2_d19790922_t080000_b01",
"SMS2_d19790922_t083000_b01",
"SMS2_d19790922_t090000_b01",
"SMS2_d19790922_t093000_b01",
"SMS2_d19790922_t100000_b01",
"SMS2_d19790922_t103000_b01",
"SMS2_d19790922_t110000_b01",
"SMS2_d19790922_t113000_b01",
"SMS2_d19790922_t120000_b01",
"SMS2_d19790922_t123000_b01",
"SMS2_d19790922_t130000_b01",
"SMS2_d19790922_t133000_b01",
"SMS2_d19790922_t140000_b01",
"SMS2_d19790922_t143000_b01",
"SMS2_d19790922_t150000_b01",
"SMS2_d19790922_t153000_b01",
"SMS2_d19790922_t160000_b01",
"SMS2_d19790922_t163000_b01",
"SMS2_d19790922_t170000_b01",
"SMS2_d19790922_t173000_b01",
"SMS2_d19790922_t174300_b01",
"SMS2_d19790922_t174900_b01",
"SMS2_d19790922_t183000_b01",
"SMS2_d19790922_t184300_b01",
"SMS2_d19790922_t185000_b01",
"SMS2_d19790922_t190000_b01",
"SMS2_d19790922_t193000_b01",
"SMS2_d19790922_t200000_b01",
"SMS2_d19790922_t203000_b01",
"SMS2_d19790922_t210000_b01",
"SMS2_d19790922_t213000_b01",
"SMS2_d19790922_t220000_b01",
"SMS2_d19790922_t223000_b01",
"SMS2_d19790922_t230000_b01",
"SMS2_d19790922_t233000_b01",
"SMS2_d19790922_t234500_b01"
]

for i, command in enumerate(COMMANDS):
    urllib.request.urlretrieve("{0}&{1}".format(HTTP, command), FILENAMES[i])