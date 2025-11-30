#!/usr/bin/env python
import urllib.request

################################################################################
#
# Title       : MET1_d19790921t013000_d19790921t203000.py
# Description : This script will download the specified MET-1 data from
#               the MCFETCH API.
# Author      : SSEC Satellite Data Services
# Date        : 2025-11-30 20:46 UTC
# Usage       : python MET1_d19790921t013000_d19790921t203000.py
# Notes       : Run this script from the directory in which you want the data.
#               This script must be made executable in order to run.
#                 On linux and mac machines:
#                   chmod a+x MET1_d19790921t013000_d19790921t203000.py
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

HTTP="https://mcfetch.ssec.wisc.edu/cgi-bin/mcfetch?dkey={0}&satellite=MET1&output=JPG&size=800+800".format(KEY)

COMMANDS =[
"date=19790921&time=01:30:00&coverage=FD&band=8",
"date=19790921&time=02:00:00&coverage=FD&band=8",
"date=19790921&time=06:00:00&coverage=FD&band=8",
"date=19790921&time=06:00:00&coverage=FD&band=8",
"date=19790921&time=07:30:00&coverage=FD&band=8",
"date=19790921&time=09:00:00&coverage=FD&band=8",
"date=19790921&time=09:00:00&coverage=FD&band=8",
"date=19790921&time=09:30:00&coverage=FD&band=8",
"date=19790921&time=09:30:00&coverage=FD&band=8",
"date=19790921&time=12:00:00&coverage=FD&band=8",
"date=19790921&time=12:30:00&coverage=FD&band=8",
"date=19790921&time=13:00:00&coverage=FD&band=8",
"date=19790921&time=13:00:00&coverage=FD&band=8",
"date=19790921&time=13:30:00&coverage=FD&band=8",
"date=19790921&time=13:30:00&coverage=FD&band=8",
"date=19790921&time=15:00:00&coverage=FD&band=8",
"date=19790921&time=15:00:00&coverage=FD&band=8",
"date=19790921&time=19:00:00&coverage=FD&band=8",
"date=19790921&time=19:00:00&coverage=FD&band=8",
"date=19790921&time=20:30:00&coverage=FD&band=8",
"date=19790921&time=20:30:00&coverage=FD&band=8"
]

FILENAMES=[
"MET1_d19790921_t013000_b08",
"MET1_d19790921_t020000_b08",
"MET1_d19790921_t060000_b08",
"MET1_d19790921_t060000_b08",
"MET1_d19790921_t073000_b08",
"MET1_d19790921_t090000_b08",
"MET1_d19790921_t090000_b08",
"MET1_d19790921_t093000_b08",
"MET1_d19790921_t093000_b08",
"MET1_d19790921_t120000_b08",
"MET1_d19790921_t123000_b08",
"MET1_d19790921_t130000_b08",
"MET1_d19790921_t130000_b08",
"MET1_d19790921_t133000_b08",
"MET1_d19790921_t133000_b08",
"MET1_d19790921_t150000_b08",
"MET1_d19790921_t150000_b08",
"MET1_d19790921_t190000_b08",
"MET1_d19790921_t190000_b08",
"MET1_d19790921_t203000_b08",
"MET1_d19790921_t203000_b08"
]

for i, command in enumerate(COMMANDS):
    urllib.request.urlretrieve("{0}&{1}".format(HTTP, command), FILENAMES[i])