
meansArray <- vector('numeric')

for(i in 1:100){
system ("java -Xint Lab data1.txt result1.txt 600")
data1 <- read.csv('result1.txt')
data1 <- data1[100:nrow(data1),2]
meansArray <- c(meansArray,mean(data1))
}
meanOfMean <- mean(meansArray)
ci1 <-confidenceInterval(meansArray)
print(meanOfMean)



