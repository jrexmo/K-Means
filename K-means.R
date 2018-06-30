cov <- matrix(c(3,0,0,3), nrow = 2)

mu1 <-matrix(c(10,10), nrow = 2)
mu2 <-matrix(c(5,0), nrow = 2)
mu3 <-matrix(c(-5,3), nrow = 2)

c1 <- mvrnorm(n = 100, mu1, cov)
c2 <- mvrnorm(n = 100, mu2, cov)
c3 <- mvrnorm(n = 100, mu3, cov)

red <- rep("red", 100)
blue <- rep("blue", 100)
green <- rep("green", 100)

plot(c(c1[,1],c2[,1], c3[,1]), c(c1[,2],c2[,2], c3[,2]))

plot(c(c1[,1],c2[,1], c3[,1]), c(c1[,2],c2[,2], c3[,2]), col = c(red, blue, green))

data <- cbind(c1,c2,c3)

colnames(data)<- c("c11","c12", "c21", "c22", "c31", "c32" )
centers <- 3

clustering <- kmeans(rbind(c1, c2, c3), 3, iter.max = 10, nstart = 1)

clustering$cluster

