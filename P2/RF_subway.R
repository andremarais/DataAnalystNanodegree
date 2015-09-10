
library(reshape2)
library(ggplot2)
turn.data <- read.csv('C:/Github/DataAnalystNanodegree/P2/Data Visualizing/turnstile_data_master_with_weather.csv', row.names = NULL)
turn.data$X <- NULL

turn.data$DATEn <- as.Date(turn.data$DATEn)
turn.data$TIMEn <- format(strptime(as.character(turn.data$TIMEn), format = '%H:%M:%S'), format = '%H:%M:%S')
turn.data$weekday <- weekdays(turn.data$DATEn)
turn.data$rain <- as.factor(turn.data$rain)
levels(turn.data$rain) <- c('No Rain', 'Rain')

daily.entries <- aggregate(data = turn.data, ENTRIESn_hourly  ~ DATEn + rain, FUN = 'sum' )
daily.exits <- aggregate(data = turn.data, EXITSn_hourly  ~ DATEn + rain, FUN = 'sum' )

daily.commute <- merge(daily.entries, daily.exits, by = 'DATEn')
daily.commute$rain.y <- NULL
colnames(daily.commute) <- c('Date', 'Rain','Entries_hourly', 'Exits_hourly')

graph1 <- ggplot(turn.data) + 
  geom_histogram(aes(x = ENTRIESn_hourly, fill = rain, col = rain), binwidth=500, alpha = .65) +facet_grid(.~rain) +
  scale_x_continuous(limits = c(0, 6000)) +
  theme(panel.background = element_blank(),
        legend.title = element_blank()) +
  xlab('Hourly entries') +
  ylab('Frequency')+
  ggtitle('Histogram of ridership on rainy and non-rainy days')

week.of.day <- aggregate(data = turn.data, ENTRIESn_hourly ~ weekday + Hour, 'sum')

ggplot(week.of.day) +
  geom_line(aes(x = Hour, y = ENTRIESn_hourly)) + 
  facet_grid(weekday ~.)



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