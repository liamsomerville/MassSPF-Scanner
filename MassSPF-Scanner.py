#!/usr/bin/python
#uses dnspython - http://www.dnspython.org/ - pip install dnspyton 
import sys, re, dns.resolver

file = "domains.txt"
domainswith = []
domainswithout = []
records = ''
resolver = dns.resolver.Resolver()
passcount = 0
failcount = 0
softfailcount = 0
neutralcount = 0

domains = open(file, 'r').read().splitlines()
for domain in domains:
    try:
        print , "Trying {}".format(domain)
        records = resolver.query(domain, "TXT")
        if records:
            for record in records.response.answer:
                for line in record.items:
                    converted = line.to_text()
                    if 'v=spf1' in converted:
                        domainswith.append(domain)
                        
                        if "+all" in converted:
                            passcount = passcount +1
                        if "-all" in converted:
                            failcount = failcount +1
                        if "~all" in converted:
                            softfailcount = softfailcount +1
                        if "?all" in converted:
                            neutralcount = neutralcount +1
                    else:
                        domainswithout.append(domain)
        else:
            domainswithout.append(domain)
    except Exception as e:
        domainswithout.append(domain)

#So we get unique domains convert to a set and back to a list
withset = set(domainswith)
domainswith = list(withset)
withoutset = set(domainswithout)
domainswithout = list(withoutset)


#Display the outputs
print 
print '=========================================='
print 'Domains with spf record: ', len(domainswith)
print '=========================================='
#for item in domainswith:
    #print item
print '=========================================='
print 'Domains without spf record:'
print '=========================================='
for item in domainswithout:
    if item not in domainswith:
        print item
print '=========================================='
print 'SPF Qualifiers:'
print '==========================================' 
print 'Pass', passcount
print 'Fail', failcount
print 'Softfail', softfailcount 
print 'Neutral', neutralcount 
malformed = len(domainswith) - passcount - failcount - softfailcount - neutralcount
print 'Malformed', malformed


