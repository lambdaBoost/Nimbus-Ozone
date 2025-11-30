#!/usr/bin/env python
import urllib.request

################################################################################
#
# Title       : GOES3_d19790922t001500_d19790922t234500.py
# Description : This script will download the specified GOES-3 data from
#               the MCFETCH API.
# Author      : SSEC Satellite Data Services
# Date        : 2025-11-30 20:39 UTC
# Usage       : python GOES3_d19790922t001500_d19790922t234500.py
# Notes       : Run this script from the directory in which you want the data.
#               This script must be made executable in order to run.
#                 On linux and mac machines:
#                   chmod a+x GOES3_d19790922t001500_d19790922t234500.py
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

KEY="YOUR KEY HERE"

HTTP="https://mcfetch.ssec.wisc.edu/cgi-bin/mcfetch?dkey={0}&satellite=GOES3&output=JPG&size=2000+2000".format(KEY)

COMMANDS =[
"date=19790922&time=00:15:00&coverage=MODE-A&band=1",
"date=19790922&time=00:45:00&coverage=MODE-A&band=1",
"date=19790922&time=01:15:00&coverage=MODE-A&band=1",
"date=19790922&time=01:45:00&coverage=MODE-A&band=1",
"date=19790922&time=02:15:00&coverage=MODE-A&band=1",
"date=19790922&time=02:45:00&coverage=MODE-A&band=1",
"date=19790922&time=03:15:00&coverage=MODE-A&band=1",
"date=19790922&time=03:45:00&coverage=MODE-A&band=1",
"date=19790922&time=04:15:00&coverage=MODE-A&band=1",
"date=19790922&time=04:45:00&coverage=MODE-A&band=1",
"date=19790922&time=05:15:00&coverage=MODE-A&band=1",
"date=19790922&time=05:45:00&coverage=MODE-A&band=1",
"date=19790922&time=06:15:00&coverage=MODE-A&band=1",
"date=19790922&time=06:45:00&coverage=MODE-A&band=1",
"date=19790922&time=07:15:00&coverage=MODE-A&band=1",
"date=19790922&time=07:45:00&coverage=MODE-A&band=1",
"date=19790922&time=08:15:00&coverage=MODE-A&band=1",
"date=19790922&time=08:45:00&coverage=MODE-A&band=1",
"date=19790922&time=09:15:00&coverage=MODE-A&band=1",
"date=19790922&time=09:45:00&coverage=MODE-A&band=1",
"date=19790922&time=10:15:00&coverage=MODE-A&band=1",
"date=19790922&time=10:45:00&coverage=MODE-A&band=1",
"date=19790922&time=11:15:00&coverage=MODE-A&band=1",
"date=19790922&time=11:45:00&coverage=MODE-A&band=1",
"date=19790922&time=12:15:00&coverage=MODE-A&band=1",
"date=19790922&time=12:45:00&coverage=MODE-A&band=1",
"date=19790922&time=13:15:00&coverage=MODE-A&band=1",
"date=19790922&time=13:45:00&coverage=MODE-A&band=1",
"date=19790922&time=14:15:00&coverage=MODE-A&band=1",
"date=19790922&time=14:45:00&coverage=MODE-A&band=1",
"date=19790922&time=15:15:00&coverage=MODE-A&band=1",
"date=19790922&time=15:45:00&coverage=MODE-A&band=1",
"date=19790922&time=16:15:00&coverage=MODE-A&band=1",
"date=19790922&time=16:45:00&coverage=MODE-A&band=1",
"date=19790922&time=17:15:00&coverage=MODE-A&band=1",
"date=19790922&time=17:45:00&coverage=MODE-A&band=1",
"date=19790922&time=18:15:00&coverage=MODE-A&band=1",
"date=19790922&time=18:45:00&coverage=MODE-A&band=1",
"date=19790922&time=19:15:00&coverage=MODE-A&band=1",
"date=19790922&time=19:45:00&coverage=MODE-A&band=1",
"date=19790922&time=19:58:00&coverage=MODE-A&band=1",
"date=19790922&time=20:05:00&coverage=MODE-A&band=1",
"date=19790922&time=20:15:00&coverage=MODE-A&band=1",
"date=19790922&time=20:45:00&coverage=MODE-A&band=1",
"date=19790922&time=21:15:00&coverage=MODE-A&band=1",
"date=19790922&time=21:45:00&coverage=MODE-A&band=1",
"date=19790922&time=22:15:00&coverage=MODE-A&band=1",
"date=19790922&time=22:45:00&coverage=MODE-A&band=1",
"date=19790922&time=23:15:00&coverage=MODE-A&band=1",
"date=19790922&time=23:45:00&coverage=MODE-A&band=1"
]

FILENAMES=[
"GOES3_d19790922_t001500_b01",
"GOES3_d19790922_t004500_b01",
"GOES3_d19790922_t011500_b01",
"GOES3_d19790922_t014500_b01",
"GOES3_d19790922_t021500_b01",
"GOES3_d19790922_t024500_b01",
"GOES3_d19790922_t031500_b01",
"GOES3_d19790922_t034500_b01",
"GOES3_d19790922_t041500_b01",
"GOES3_d19790922_t044500_b01",
"GOES3_d19790922_t051500_b01",
"GOES3_d19790922_t054500_b01",
"GOES3_d19790922_t061500_b01",
"GOES3_d19790922_t064500_b01",
"GOES3_d19790922_t071500_b01",
"GOES3_d19790922_t074500_b01",
"GOES3_d19790922_t081500_b01",
"GOES3_d19790922_t084500_b01",
"GOES3_d19790922_t091500_b01",
"GOES3_d19790922_t094500_b01",
"GOES3_d19790922_t101500_b01",
"GOES3_d19790922_t104500_b01",
"GOES3_d19790922_t111500_b01",
"GOES3_d19790922_t114500_b01",
"GOES3_d19790922_t121500_b01",
"GOES3_d19790922_t124500_b01",
"GOES3_d19790922_t131500_b01",
"GOES3_d19790922_t134500_b01",
"GOES3_d19790922_t141500_b01",
"GOES3_d19790922_t144500_b01",
"GOES3_d19790922_t151500_b01",
"GOES3_d19790922_t154500_b01",
"GOES3_d19790922_t161500_b01",
"GOES3_d19790922_t164500_b01",
"GOES3_d19790922_t171500_b01",
"GOES3_d19790922_t174500_b01",
"GOES3_d19790922_t181500_b01",
"GOES3_d19790922_t184500_b01",
"GOES3_d19790922_t191500_b01",
"GOES3_d19790922_t194500_b01",
"GOES3_d19790922_t195800_b01",
"GOES3_d19790922_t200500_b01",
"GOES3_d19790922_t201500_b01",
"GOES3_d19790922_t204500_b01",
"GOES3_d19790922_t211500_b01",
"GOES3_d19790922_t214500_b01",
"GOES3_d19790922_t221500_b01",
"GOES3_d19790922_t224500_b01",
"GOES3_d19790922_t231500_b01",
"GOES3_d19790922_t234500_b01"
]

for i, command in enumerate(COMMANDS):
    urllib.request.urlretrieve("{0}&{1}".format(HTTP, command), FILENAMES[i])