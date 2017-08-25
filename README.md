# MassSPF-Scanner
Quick script to help scan through SPF records from an input file
Requires DNSPython (pip install dnspython), see http://www.dnspython.org/ 
uses a input file "domains.txt", one domain per line

- as well aslooking for "v=spf1" in a DNS TXT record the script counts the SPF Qalifiers too by quering the results for:
  - "+"	Pass
  - "-"	Fail
  - "~"	SoftFail
  - "?"	Neutral
- the script counts "Malformed" as a qualifier that doesnt meet one of the above
- Counts the number of domains with SPF records
- Provides a list of domains that are without SPF records

For fun I ran the script against the Alexa Top 500 Domains on 24 August 2017 and found the following
- 407 Domains with a SPF Record
  - "+"	Pass 0
  - "-"	HardFail 205
  - "~"	SoftFail 171
  - "?"	Neutral 18
  - Malformed 13
- 93 Domains without a SPF Record

