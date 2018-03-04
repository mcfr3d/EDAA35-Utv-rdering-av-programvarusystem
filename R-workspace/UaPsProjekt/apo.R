apo <- function(data, treshold){
  Variable <- colnames(data)
  noOutlier <- vector()
  means <- vector()
  i <- 1
  while(i <= length(data)){
    len <- length(data[data[,i] > treshold[i],i])
    noOutlier<- c(noOutlier,len)
    meany <- mean(data[data[,i] <= treshold[i],i])
    means <- c(means,meany)
    i <- i + 1
  }
  df<-data.frame(Variable,noOutlier,means)
  names(df)<-c("a1","a2","a3")
  df
}