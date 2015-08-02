require(ggplot2)

setwd("C:/Github/DataAnalystNanodegree/P1")

stroop <- read.csv("stroopdata.csv")

ggplot(stroop) + 
  geom_density(aes(x = Congruent), fill = "thistle3", col = "thistle4", alpha = .8, size = 1) + 
  geom_density(aes(x = Incongruent), fill = "lightsteelblue3", col = "lightsteelblue4", alpha = .8, size = 1) +
  xlab("Seconds") +
  ggtitle("Density plot of time take to complete test\nPurple: Congruent | Blue: Incongruent") +
  geom_vline(xintercept  = mean(stroop$Congruent), col = "thistle4", linetype = "longdash", size = 1)+
  geom_vline(xintercept  = mean(stroop$Incongruent), col = "lightsteelblue4", linetype = "longdash", size = 1)+
  annotate("text", label = paste("Congruent mean", round(mean(stroop$Congruent),2)), x =mean(stroop$Congruent) , y = .02, col = "thistle4") +
  annotate("text", label = paste("Incongruent mean", round(mean(stroop$Incongruent),2)), x =mean(stroop$Incongruent) , y = .01, col = "lightsteelblue4") 



stroop$difference <- stroop$Incongruent - stroop$Congruent
stroop.means <- apply(stroop,2, FUN = "mean"))

ggplot(stroop) +
  geom_density(aes(x = difference), fill = "coral3", col = "coral4", alpha = .8, size = 1)+
  xlab("Seconds")+
  ggtitle("Density plot of delta") +
  geom_vline(xintercept  = mean(stroop$difference), col = "coral4", linetype = "longdash", size = 1)+
  annotate("text", label = paste("Mean of difference", round(mean(stroop$difference),2)), x =mean(stroop$difference) , y = .01, col = "coral4") 


std.error <- function(x) sd(x) / sqrt(length(x))


stroop.means <- apply(stroop,2, FUN = "mean")
stroop.std.errors <- apply(stroop, 2, FUN = "std.error")

t.value <- (stroop.means$) / stroop.std.errors[3]

critical.value <- qt(.025, length(stroop$difference) -1, lower.tail =  T)


