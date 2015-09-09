install.packages('randomForest')
install.packages('reshape2')
library(reshape2)
library(ggplot2)
turn.data <- read.csv('C:/Udacity/Data Science/Data Visualizing/turnstile_data_master_with_weather.csv', row.names = NULL)
turn.data$X <- NULL

turn.data$DATEn <- as.Date(turn.data$DATEn)
turn.data$TIMEn <- format(strptime(as.character(turn.data$TIMEn), format = '%H:%M:%S'), format = '%H:%M:%S')
turn.data$weekday <- weekdays(turn.data$DATEn)
daily.entries <- aggregate(data = turn.data, ENTRIESn_hourly  ~ DATEn + rain, FUN = 'sum' )
daily.entries$rain <- as.factor(daily.entries$rain)


ggplot(daily.entries) + 
  geom_bar(aes(x = DATEn, y = ENTRIESn_hourly, fill = rain), stat = 'identity', col = NA, alpha = .5)


temp.agg <- aggregate(data = turn.data, ENTRIESn_hourly ~ meantempi + meanwindspdi+ rain, 'sum')
temp.agg$rain <- as.factor(temp.agg$rain)
ggplot(temp.agg) +
  geom_point(aes(x = meantempi, y = meanwindspdi, size = ENTRIESn_hourly, shape = rain))

ggplot(turn.data) + geom_histogram(aes(x = ENTRIESn_hourly), binwidth=1000) +facet_grid(rain ~.) + scale_x_continuous(limits = c(0, 10000))
#
#dcast(df_melt, year + month ~ variable, sum)
# junk====
date.dummy <- model.matrix(data = turn.data, ~ DATEn -1)
unit.dummy <- model.matrix(data = turn.data, ~ UNIT -1)
train.size <- nrow(turn.data)*.25
train.set.rows <- sample(nrow(turn.data), train.size, replace = F)
test.set.rows <- which(!(1:nrow(turn.data) %in% train.set.rows))
length(train.set.rows) + length(test.set) - nrow(turn.data)
train.data <- turn.data[train.set.rows,]
test.data <- turn.data[test.set.rows,]
mode.data <- cbind(tra)
turn.rf <- randomForest(ENTRIESn_hourly ~ . -X - UNIT -DATEn -TIMEn -Hour - DESCn, data = train.data, importance = T)
hist(test.data$ENTRIESn_hourly - predict(turn.rf, test.data))
predict(turn.rf, test.data)
plot(predict(turn.rf, test.data), type = 'l')
plot(test.data$ENTRIESn_hourly, type = 'l')
#model.matrix( ~ Species - 1, data=iris )