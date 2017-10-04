import gzip, sys

inFilePath1 = sys.argv[1]
inFilePath2 = sys.argv[2]

inFile1 = gzip.open(inFilePath1)
inFile2 = gzip.open(inFilePath2)

lines1 = [line.rstrip("\n").split("\t") for line in inFile1]
lines2 = [line.rstrip("\n").split("\t") for line in inFile2]

inFile1.close()
inFile2.close()

samples1 = set([x[0] for x in lines1][1:])
samples2 = set([x[0] for x in lines2][1:])

commonSamples = samples1 & samples2

lines1 = [lineItems for lineItems in lines1 if lineItems[0] == "Sample" or lineItems[0] in commonSamples]
lines2 = [lineItems for lineItems in lines2 if lineItems[0] == "Sample" or lineItems[0] in commonSamples]

with gzip.open(inFilePath1, 'wb') as outFile1:
    for lineItems in lines1:
        outFile1.write("\t".join(lineItems) + "\n")

with gzip.open(inFilePath2, 'wb') as outFile2:
    for lineItems in lines2:
        outFile2.write("\t".join(lineItems) + "\n")
