# function for plotting data
plotresult = function ( file , start = 1) {
  data <- read.csv( file )
  data <- data [ start : nrow ( data ) ,]
  plot ( data , type = 'l')
}

system ("java Lab data1.txt result1.txt 600")
plotresult ("result1.txt") # plot to screen

pdf ("result1.pdf")
plotresult ("result1.txt") # plot to pdf file
dev.off ()