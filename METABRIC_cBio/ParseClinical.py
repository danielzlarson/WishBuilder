import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

#There are 5 header lines. We want to focus on the first one.
with open(inFilePath, "r") as inFile:
    with gzip.open(outFilePath, "w") as outFile:
        headerItems = inFile.readline().rstrip("\n").split("\t")
        headerItems[0] = "Sample"

        inFile.readline()
        inFile.readline()
        inFile.readline()
        inFile.readline()

        outFile.write(("\t".join(headerItems) + "\n").encode())

        for line in inFile:
            lineItems = line.rstrip("\n").split("\t")
            for i in range(1, len(lineItems)):
                if lineItems[i] == "":
                    lineItems[i] = "NA"

            outLine = "\t".join(lineItems) + "\n"
            outFile.write(outLine.encode())
