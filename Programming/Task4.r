setwd('C:/Users/chamb/PycharmProjects/Programming')
train<-read.csv('train.csv')
test<-read.csv('test.txt')
colnames(test)[1]='A'
library(rpart)
library(class)
install.packages('varhandle')
library(varhandle)
help(rpart)
library(e1071)
library(randomForest)

train_2<-which(train[,1]==2)
set.seed(1155092111)
order<-sample.int(51)
train_others<-train[order,]

#decision tree
correct=0
for (i in 1:3)
{
  cv_train<-rbind(train[train_2,],train_others[-(((i-1)*17+1):(i*17)),])
  cv_test<-train_others[(((i-1)*17+1):(i*17)),]
  decision_tree<-rpart(label~A+B+C+D,data=cv_train,method='class')
  ans<-predict(decision_tree,cv_test)
  now<-c()
  for (k in 1:17)
  {
    a=which(ans[k,]==max(ans[k,]))
    if (length(a)>1) {a=a[2]}
    now=c(now,a)
  }
  correct=correct+sum(now==cv_test[,1])
}
#correct=27
model_dt<-rpart(label~A+B+C+D,data=train,method='class')
result_dt<-predict(model_dt,test)


# K-nearest neighbor
lr<-glm(C~label+A+B+D,data=train[-27,])
predict(lr,train[27,])
train[27,4]<-predict(lr,train[27,])
train_others<-train[order,]
correct=0

for (j in 1:10){
  for (l in 0:(j-1)){
    correct=0
    for (i in 1:3)
      {
      
        cv_train<-rbind(train[train_2,],train_others[-(((i-1)*17+1):(i*17)),])
        cv_test<-train_others[(((i-1)*17+1):(i*17)),]
        now<-knn(cv_train[,2:5],cv_test[,2:5],cv_train[,1],j,l)
        ans<-unfactor(now)
        correct=correct+sum(ans==cv_test[,1])
      }
  }
}
#correct=37 k=3&l=1
result_KNN<-knn(train[,2:5],test,train[,1],3,1)



#SVM
correct=0
i=1
for (i in 1:3)
{
  
  cv_train<-rbind(train[train_2,],train_others[-(((i-1)*17+1):(i*17)),])
  cv_test<-train_others[(((i-1)*17+1):(i*17)),]
  now<-svm(label~A+B+C+D,data=cv_train,type='C-classification')
  ans<-predict(now,cv_test[,2:5])
  ans<-unfactor(ans)
  correct=correct+sum(ans==cv_test[,1])
}
#correct=43
model_svm<-svm(label~.,data=train,type='C-classification')
result_svm<-predict(model_svm,test)

#naiveBayes
correct=0
i=1
for (i in 1:3)
{
  
  cv_train<-rbind(train[train_2,],train_others[-(((i-1)*17+1):(i*17)),])
  cv_test<-train_others[(((i-1)*17+1):(i*17)),]
  now<-naiveBayes(as.factor(label)~A+B+C+D,data=cv_train)
  ans<-predict(now,cv_test)
  ans<-unfactor(ans)
  correct=correct+sum(ans==cv_test[,1])
}
#correct=40
model_nB<-naiveBayes(as.factor(label)~.,data=train)
result_nB<-predict(model_nB,test)


#randomForest
correct=0
i=1
for (i in 1:3)
{
  
  cv_train<-rbind(train[train_2,],train_others[-(((i-1)*17+1):(i*17)),])
  cv_test<-train_others[(((i-1)*17+1):(i*17)),]
  now<-randomForest(as.factor(label)~.,data=cv_train)
  ans<-predict(now,cv_test)
  ans<-unfactor(ans)
  correct=correct+sum(ans==cv_test[,1])
}
#correct=46
model_rF<-randomForest(as.factor(label)~.,data=train)
result_rF<-predict(model_rF,test)












