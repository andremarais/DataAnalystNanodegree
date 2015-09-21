library(scales)
library(reshape2)
library(ggplot2)
turn.data <- read.csv('C:/Github/DataAnalystNanodegree/P2/turnstile_data_master_with_weather_pred.csv', row.names = NULL)
turn.data$X <- NULL

turn.data$daten <- as.Date(turn.data$daten, format = "%Y-%m-%d")
turn.data$timen <- format(strptime(as.character(turn.data$timen), format = '%H:%M:%S'), format = '%H:%M:%S')
turn.data$weekday <- weekdays(turn.data$daten)
turn.data$rain <- as.factor(turn.data$rain)
levels(turn.data$rain) <- c('No Rain', 'Rain')

daily.entries <- aggregate(data = turn.data, entriesn_hourly  ~ daten + rain, FUN = 'sum' )
daily.exits <- aggregate(data = turn.data, exitsn_hourly  ~ daten + rain, FUN = 'sum' )

daily.commute <- merge(daily.entries, daily.exits, by = 'daten')
daily.commute$rain.y <- NULL
colnames(daily.commute) <- c('Date', 'Rain','Entries_hourly', 'Exits_hourly')

ggplot(turn.data) + 
  geom_histogram(aes(x = entriesn_hourly, fill = rain, col = rain), binwidth=500, alpha = .65) +facet_grid(.~rain) +
  scale_x_continuous(limits = c(0, 6000)) +
  theme(panel.background = element_blank(),
        legend.title = element_blank()) +
  xlab('Hourly entries') +
  ylab('Frequency')+
  ggtitle('Histogram of ridership on rainy and non-rainy days')

week.of.day <- aggregate(data = turn.data, entriesn_hourly ~ weekday + hour + rain, 'sum')

ggplot(week.of.day) +
  geom_line(aes(x = hour, y = entriesn_hourly), col = 'dodgerblue3') + 
  facet_grid(weekday ~ rain)+
  theme(panel.background = element_rect(fill = '#E7F1FA'),
        legend.title = element_blank()) +
  scale_y_continuous(labels = comma)+
  xlab('Hour of the day') +
  ylab('Hourly entries') +
  ggtitle('Ridership during the day for each day of the week on rainy and non-rainy days')



unit.rain <- aggregate(data = turn.data, ENTRIESn_hourly ~ UNIT + rain, 'mean')

ggplot(unit.rain) + geom_bar(aes(x = reorder(UNIT,-ENTRIESn_hourly), y=ENTRIESn_hourly, position = 'dodge', fill = rain, col = rain), stat ='identity') #+ facet_grid(rain ~.)


#turn.lm <- lm(ENTRIESn_hourly ~  rain + meanwindspdi + Hour + fog + maxtempi + meantempi + as.factor(UNIT), data = turn.data, importance = T)

turn.data.ecdf <- ecdf(turn.data$entriesn_hourly - turn.data$predictions)

ggplot() + 
  geom_line(aes(x =environment(turn.data.ecdf)$x, y = environment(turn.data.ecdf)$y), col = 'dodgerblue3')+
  theme(panel.background = element_rect(fill = '#E7F1FA'),
        legend.title = element_blank())+
  xlab('Risiduals')+
  ylab('Cumulative Probability')+
  ggtitle('Cumulative Probability of the Hourly Entries predictions')


ggplot(turn.data) + geom_histogram(aes(x = (turn.data$entriesn_hourly - turn.data$predictions)), binwidth = range(turn.data$entriesn_hourly - turn.data$predictions)/60)
  






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