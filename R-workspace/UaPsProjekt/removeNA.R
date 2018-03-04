removeNA <- function(data){
  data2 <- data[complete.cases(data),]
  data2
  }